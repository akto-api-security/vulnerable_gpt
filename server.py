from flask import Flask, request, jsonify
from privateGPT import init
import time
import uuid

app = Flask(__name__)
qa = None

@app.route("/query", methods=["GET"])
def query():
    req_id = str(uuid.uuid4())
    print(f"Request {req_id} received")
    q = request.args.get("q")

    if q is None or q == '':
        return jsonify(query=q, answer="Empty input")

    start = time.time()
    res = qa(q)
    answer, docs = res['result'], []
    end = time.time()
    print(f"Request {req_id} | Query: {q} | Answer: {answer} | Time: {end-start}")
    return jsonify(query=q, answer=res['result'])

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})


if __name__ == '__main__':
    qa = init()
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
