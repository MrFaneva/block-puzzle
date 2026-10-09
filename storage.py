import json

FILE = "scores.json"

def load_scores():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_score(score):
    scores = load_scores()
    scores.append(score)
    with open(FILE, "w") as f:
        json.dump(scores, f)

def reset_scores():
    with open(FILE, "w") as f:
        json.dump([], f)
