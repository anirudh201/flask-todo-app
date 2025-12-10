from flask import Flask, jsonify,render_template
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

@app.route('/api')
def api():
    with open(DATA_FILE) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
@app.route('/todo')
def todo_page():
    return render_template('todo.html')