def make_rxn_expression(reaction_ids):
    or_split = [x.strip(' ') for x in reaction_ids.split(' or ')]

    if len(or_split) > 1:
        # Handle 'or' case
        reactions = []
        for index, reaction in enumerate(or_split):
            is_reverse = reaction.startswith('reverse_')
            reaction = reaction.replace('reverse_', '')
            sign = ' - ' if is_reverse else ' + '
            if index != 0:
                reactions.append(sign + reaction)
            else:
                reactions.append(reaction)
        expression = ''.join(reactions)

    else:
        and_split = [x.strip(' ') for x in or_split[0].split(' and ')]
        if len(and_split) > 1:
            # Handle 'and' case
            expressions = []
            for reaction in and_split:
                is_reverse = reaction.startswith('reverse_')
                reaction = reaction.replace('reverse_', '')
                sign = '-' if is_reverse else ''
                expressions.append(sign + reaction)
            expression = ' + '.join(expressions)
        else:
            # Handle single reaction case
            reaction = and_split[0]
            is_reverse = reaction.startswith('reverse_')
            reaction = reaction.replace('reverse_', '')
            expression = '-' + reaction if is_reverse else reaction

    return expression

# Example usage:
# expression = make_rxn_expression('PFK or reverse_FBP')
# print(f"Reaction expression: {expression}")