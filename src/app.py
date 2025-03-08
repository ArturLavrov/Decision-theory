from flask import Flask, request, jsonify
from flask_cors import CORS
from Evaluators.comparativeAdvantageEvaluator import ComparativeAdvantageEvaluator
from Evaluators.uncertaintyEvaluator import UncertaintyEvaluator

app = Flask(__name__)
CORS(app)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json

    evaluator = ComparativeAdvantageEvaluator(data)
    evaluation_result = evaluator.evaluate()

    if hasattr(evaluation_result, 'error'):
        return jsonify(evaluation_result, 400)

    return jsonify(evaluation_result)

@app.route('/evaluate_lab2', methods=['POST'])
def evaluate_lab2():
    data = request.json

    evaluator = UncertaintyEvaluator(evaluationData=data["matrix"], alpha=data["alpha"])
    evaluation_result = evaluator.evaluate()

    if hasattr(evaluation_result, 'error'):
        return jsonify(evaluation_result, 400)

    return jsonify(evaluation_result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
