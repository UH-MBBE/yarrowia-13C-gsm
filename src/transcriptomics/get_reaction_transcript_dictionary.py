# convert a reaction's gpr to a set (connected by 'and' relationship) of gene sets (connected by 'or' relationships)
def get_gene_sets(gene_reaction_rule):
    # split the gpr by "and"
    and_split = gene_reaction_rule.split(" and ")

    # process each group to create a frozenset
    gene_sets = set()
    for gene_group in and_split:
        # remove parentheses if exist
        gene_group = gene_group.strip('()')

        # split the group by "or" if it's there
        or_split = gene_group.split(" or ")

        # add frozenset to the set
        gene_sets.add(frozenset(or_split))

    return gene_sets

# sum transcripts from genes that have 'or' relationships
def get_gene_set_transcript_sum(gene_set, transcript_dict):
    transcript_sum = 0
    for gene in gene_set:
        # # if gene ends with a 'p' switch it with a 'g' (g = gene id, p = protein id)
        if len(gene) > 0 and gene.endswith('p'):
            gene = gene[:-1] + 'g'

        # # if gene end with 'G' replace it with 'g' to match transcriptomics data
        if len(gene) > 0 and gene.endswith('G'):
            gene = gene[:-1] + 'g'

        # remove unnecessary characters
        gene = gene.strip('() ')

        # check if gene is in the transcript dictionary
        if gene not in transcript_dict:
            transcript_sum += np.inf

        # print(gene, transcript_dict[gene])
        transcript_sum += transcript_dict[gene]
    return transcript_sum

# get the minimum transcript level from the gene sets that have 'and' relationships
def get_reaction_transcript_level(gene_sets, transcript_dict):
    transcript_group_levels = [get_gene_set_transcript_sum(gene_set, transcript_dict) for gene_set in gene_sets]
    # print(transcript_group_levels)
    return min(transcript_group_levels)

# get a dictionary of reaction ids to transcript levels
def get_reaction_transcript_dictionary(model, gene_transcript_dictionary):
    transcript_dict = {}
    for r in model.reactions:
        reaction_gene_sets = get_gene_sets(r.gene_reaction_rule)
        transcript_level = get_reaction_transcript_level(reaction_gene_sets, gene_transcript_dictionary)

        transcript_dict[r.id] = transcript_level
   
    return transcript_dict
