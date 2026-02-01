def check_termination(violations, time_overrun):
    if violations >= 3:
        return True, "Too many violations"
    if time_overrun:
        return True, "Time limit exceeded"
    return False, None


def evaluate_mcq(correct, wrong):
    score = (correct * 2) - wrong
    passed = score >= 40
    return score, passed


def evaluate_coding(passed_cases, total_cases):
    score = (passed_cases / total_cases) * 100
    passed = score >= 50
    return score, passed
