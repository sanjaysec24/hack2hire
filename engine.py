import rules
from models import InterviewState

class InterviewEngine:

    def __init__(self, data):
        self.data = data
        self.violations = 0
        self.time_overrun = False

    def start(self, result):
        result.state = InterviewState.IN_PROGRESS

        # MCQ Round
        mcq = self.data["mcq"]
        score, passed = rules.evaluate_mcq(
            mcq["correct"], mcq["wrong"]
        )
        result.total_score += score
        result.round_scores["MCQ"] = score

        terminate, reason = rules.check_termination(
            self.violations, self.time_overrun
        )
        if terminate or not passed:
            result.state = InterviewState.TERMINATED
            result.termination_reason = reason or "Failed MCQ"
            return result

        # Coding Round
        coding = self.data["coding"]
        score, passed = rules.evaluate_coding(
            coding["passed"], coding["total"]
        )
        result.total_score += score
        result.round_scores["CODING"] = score

        if not passed:
            result.state = InterviewState.TERMINATED
            result.termination_reason = "Failed Coding"
            return result

        result.state = InterviewState.COMPLETED
        return result
