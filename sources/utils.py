def combine_with_or(left, right):
    """Distribute OR between two formulas already written in CNF."""
    result = []

    for left_clause in left:
        for right_clause in right:
            result.append(left_clause + right_clause)

    return result


def clauses_to_formula(clauses):
    """Convert a list of CNF clauses back to reverse polish notation."""
    formula_parts = []

    for clause in clauses:
        clause_formula = clause[0]
        for literal in clause[1:]:
            clause_formula += literal + "|"
        formula_parts.append(clause_formula)

    return "".join(formula_parts) + "&" * (len(formula_parts) - 1)
