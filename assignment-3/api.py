"""
Search API provided for Assignment 3.

@author: Krisztian Balog
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

AWS_ACCESS_KEY = ''  # REMOVED
AWS_SECRET_KEY = ''  # REMOVED
AWS_REGION = ''  # REMOVED
AWS_SERVICE = ''  # REMOVED
AWS_HOST = ''  # REMOVED
AWS_PORT = 443
AWS_AUTH = AWS4Auth(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, AWS_SERVICE)

DOC_TYPE = "doc"

es = Elasticsearch(
    hosts=[{'host': AWS_HOST, 'port': AWS_PORT}],
    http_auth=AWS_AUTH,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)


@app.route("/")
def index():
    return "This is the API for DAT630 Assignment 3"


@app.route("/<indexname>/_search")
def search(indexname):
    q = request.args.get('q')
    if q is None:
        return "Parameter q is missing"
    df = request.args.get('df')
    if df is None:
        return "Parameter df is missing"
    size = request.args.get('size')
    if size is None:
        size = 10

    return jsonify(es.search(index=indexname, q=q, df=df, _source=False, size=size))


@app.route("/<indexname>/<docid>/_termvectors")
def termvectors(indexname, docid):
    ts = (request.args.get('term_statistics') == "true")
    return jsonify(es.termvectors(index=indexname, doc_type=DOC_TYPE, id=docid, term_statistics=ts))


@app.route("/<indexname>/<docid>/_exists")
def exists(indexname, docid):
    return jsonify({"exists": es.exists(index=indexname, doc_type=DOC_TYPE, id=docid)})


@app.route("/<indexname>/_analyze")
def analyze(indexname):
    text = request.args.get('text')
    if text is None:
        return "Parameter text is missing"
    return jsonify(es.indices.analyze(index=indexname, body={"analyzer": "english", "text": text}, format="text"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
