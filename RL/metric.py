

def planner_metric(example, prediction, trace=None):
    score = 0.0
    if prediction.tool.strip().lower() == example.tool.strip().lower():
        score += 1.0
    if example.tool == "remember fact":
        if "|" in prediction.input:
            score += 0.5
    if prediction.input and prediction.input.strip():
        score += 0.3
    return score
