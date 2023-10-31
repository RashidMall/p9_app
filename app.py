from flask import Flask, render_template, request, flash
import requests as req
import pandas as pd

# URL of the remote API server for article recommendations.
SERVER_URL = "https://app-articlereco.azurewebsites.net/api/rec_articles?user_id="

def get_recommendations(user_id):
    response = req.get(SERVER_URL + str(user_id))
    response = response.json()
    return response


app = Flask(__name__, static_url_path='/')
app.secret_key = 'secret_key'

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/recommendations', methods=['POST', 'GET'])
def recommendations():
    if request.method == 'POST':
        user_id = request.form['user_id']
        recommendations = get_recommendations(user_id)
        flash(recommendations, 'recommendations')

        return render_template('index.html', recommendations=recommendations)


if __name__ == "__main__":
    app.run()
    #app.run(debug=True, host='127.0.0.1', port=5050)