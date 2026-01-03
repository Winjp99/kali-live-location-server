from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
latest = {}

@app.route("/update", methods=["POST"])
def update():
    global latest
    latest = request.json
    return {"status": "ok"}

@app.route("/location")
def location():
    return jsonify(latest)

@app.route("/")
def map_view():
    return send_from_directory("../web", "map.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
