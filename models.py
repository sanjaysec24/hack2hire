from enum import Enum

class InterviewState(Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    TERMINATED = "TERMINATED"
    COMPLETED = "COMPLETED"


class InterviewResult:
    def __init__(self):
        self.total_score = 0
        self.state = InterviewState.NOT_STARTED
        self.termination_reason = None
        self.round_scores = {}
