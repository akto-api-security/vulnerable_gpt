from flask import Flask, request, jsonify
from privateGPT import init
import time

app = Flask(__name__)
qa = None

@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")

    if q is None or q == '':
        return jsonify(query=q, answer="Empty input")

    start = time.time()
    res = qa(q)
    answer, docs = res['result'], []
    end = time.time()
    print(f"Query: {q} | Answer: {answer} | Time: {end-start}")
    return jsonify(query=q, answer=res['result'])


if __name__ == '__main__':
    qa = init()
    app.run(debug=True)