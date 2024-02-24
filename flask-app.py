from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test():
    a = request.args.get("a", type=int, default=None)
    b = request.args.get("b", type=str)

    if b is None:
        return jsonify(
            {
                "error_code": "1",
                "error_message": "Parameter 'b' is missing",
                "reference": None,
            }
        )

    return jsonify({"error_code": "0", "error_message": "success", "reference": "111"})


if __name__ == "__main__":
    app.run(debug=True)
