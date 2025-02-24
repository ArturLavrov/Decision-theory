import numpy as np
class ComparativeAdvantageEvaluator:
    def __init__(self, evaluationData):
        self.evaluationData = evaluationData

    def evaluate(self):
        alternatives = self.evaluationData.get("alternatives", [])
        experts = self.evaluationData.get("experts", [])
        scores = self.evaluationData.get("scores", [])

        if len(scores) != len(alternatives) or any(len(row) != len(experts) for row in scores):
            return {"error": "Invalid input dimensions"}

        scores_array = np.array(scores, dtype=float)
        normalized_scores = np.zeros_like(scores_array)

        for j in range(scores_array.shape[1]):
            total = np.sum(scores_array[:, j])
            if total > 0:
                normalized_scores[:, j] = scores_array[:, j] / total

        mean_scores = np.mean(normalized_scores, axis=1)
        ranked_alternatives = sorted(zip(alternatives, mean_scores), key=lambda x: x[1], reverse=True)

        response = {
            "normalized_scores": {alt: score for alt, score in zip(alternatives, mean_scores)},
            "ranking": [{"alternative": alt, "score": score} for alt, score in ranked_alternatives]
        }
        return response