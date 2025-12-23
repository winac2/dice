from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)
random.seed(69969669)

dice_faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roll")
def roll():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)

    total = d1 + d2 + d3
    result = "Tài" if total > 10 else "Xỉu"

    return jsonify({
        "dice": dice_faces[d1-1] + dice_faces[d2-1] + dice_faces[d3-1],
        "result": result,
        "color": "red" if result == "Tài" else "green"
    })

if __name__ == "__main__":
    app.run(debug=True)
