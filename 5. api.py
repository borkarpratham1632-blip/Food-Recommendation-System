from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend')
def recommend():
    user_id = int(request.args.get('user_id'))
    # dummy response
    return jsonify({"user_id": user_id, "recommendations": [101,102,103]})

if __name__ == "__main__":
    app.run(debug=True)
