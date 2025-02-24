from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from comparativeAdvantageEvaluator import ComparativeAdvantageEvaluator

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
