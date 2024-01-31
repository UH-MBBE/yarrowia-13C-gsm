import numpy as np

def get_gene_transcript_dictionary(transcriptomics_df, condition):
    transcript_dict = {}
    transcript_dict[''] = np.inf
    for _, row in transcriptomics_df.iterrows():
        transcript_dict[row['YALI0_id']] = row[condition]
    return transcript_dict