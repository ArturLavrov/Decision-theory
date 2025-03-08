import numpy as np

class UncertaintyEvaluator:
    def __init__(self, evaluationData, alpha=0.5):
        self.evaluationData = evaluationData
        self.alpha = alpha

    def evaluate(self):
        matrix = np.array(self.evaluationData)
        num_alternatives = matrix.shape[0]
        alternatives = [f"A{i+1}" for i in range(num_alternatives)]

        wald_values = np.min(matrix, axis=1).tolist()
        maxmax_values = np.max(matrix, axis=1).tolist()
        hurwicz_values = (self.alpha * np.max(matrix, axis=1) + (1 - self.alpha) * np.min(matrix, axis=1)).tolist()

        wald_result = dict(zip(alternatives, wald_values))
        maxmax_result = dict(zip(alternatives, maxmax_values))
        hurwicz_result = dict(zip(alternatives, hurwicz_values))

        best_wald = alternatives[np.argmax(wald_values)]
        best_maxmax = alternatives[np.argmax(maxmax_values)]
        best_hurwicz = alternatives[np.argmax(hurwicz_values)]

        return {
            "wald": {
                "values": wald_result,
                "best_alternative": best_wald
            },
            "maxmax": {
                "values": maxmax_result,
                "best_alternative": best_maxmax
            },
            "hurwicz": {
                "values": hurwicz_result,
                "best_alternative": best_hurwicz
            }
        }