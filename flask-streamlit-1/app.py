from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask is running"

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    processed_data = data['input_data'].upper()  # ????????????, ???? uppercase ???
    return jsonify({'processed_data': processed_data})

if __name__ == '__main__':
    app.run(debug=True)