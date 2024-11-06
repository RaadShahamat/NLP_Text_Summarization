from flask import Flask, render_template, url_for
import requests
from flask import request as flask_request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])     

def Index():
    return render_template('index.html')

@app.route('/summarize', methods=['GET', 'POST'])
def Summarize():
    if flask_request.method == 'POST':
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}
        data = flask_request.form['text']

        maxL = 150
        minL = 30

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
        "inputs": data,
        "parameters": {'max_length': maxL, 'min_length': minL},
        })
        return render_template('index.html', output = output[0]["summary_text"])




if __name__ == '__main__':
    app.debug = True
    app.run()