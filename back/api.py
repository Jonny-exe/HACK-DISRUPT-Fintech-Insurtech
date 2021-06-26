#!/usr/bin/python3
# importing the flask library files
from flask import Flask, json, request
from flask_cors import CORS
from searcher import search

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={r"/*": {"origins": "*"}})

ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "csv"])


# define http route
@app.route("/")
def index():
    # return "Hello World!"
    return json.dumps({"hello": "world"})


@app.route("/file", methods=["POST", "OPTIONS"])
def file():
    text = request.form["text"]
    words = text.split("\n")
    result = []
    for word in words:
        search_result, category = search(word)
        #              name                   kg co2            category
        result.append({"product": word, "co2": search_result, "category": category})
    return json.dumps(result)


@app.after_request  # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    return response


# run the app
if __name__ == "__main__":
    app.run(debug=True)
