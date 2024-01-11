from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template('index.html')

@app.route("/Summarize", methods=["POST"])
def Summarize():
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer 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"}

    if request.method == "POST":
        data = request.form["data"]
        min_length = 20
        max_length = int(request.form["max_len"])

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({    
            "inputs": data,
            "parameters": {"min_length": min_length, "max_length": max_length}
        })[0]

        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)