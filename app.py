from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query", "")
    # Replace this with your AI logic
    result = f"You searched for: {query}"
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(debug=True)
