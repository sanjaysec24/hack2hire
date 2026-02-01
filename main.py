import json
from engine import InterviewEngine
from models import InterviewResult

with open("input.json") as f:
    data = json.load(f)

engine = InterviewEngine(data)
result = InterviewResult()

final = engine.start(result)

print("Final Score:", final.total_score)
print("State:", final.state.value)
print("Termination Reason:", final.termination_reason)
print("Round Scores:", final.round_scores)
