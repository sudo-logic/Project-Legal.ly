
# Makeshift script for chatbot backend as the Model couldn't train in time :')
# Please read the README file to check our actual approach towards the problem

from email import header
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from matplotlib.pyplot import text
import pandas as pd
import difflib
import model
import nltk

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


data = pd.read_csv('A2015-22.csv')

topics = list(data['title'])
text = list(data['text'])


greetings = ['Hi', 'Hello', "Hey There", 'hi']


@app.route("/api", methods=['POST'])
@cross_origin()
def get_bot_response():
    query = request.form['msg']

    cleaned = " ".join([word for word in query.split()
                       if word not in nltk.corpus.stopwords.words('english')])

    if difflib.get_close_matches(query, greetings):
        return "Hi There! Welcome to Legal.ly\nPlease type 'topics' to get a list of the topics I have knowledge on."

    if query.lower().strip() in ['topics', 'topic']:
        response = 'You can ask me anything about the following topics:\n' + \
            " | ".join(topics)
        return response

    match = difflib.get_close_matches(cleaned, topics, n=1)
    if match:
        match = match[0]
        ans = model.get_answer(query, text[topics.index(match)])
        return "I believe the answer to your query is: {}. \n For more context, please refer to the following text: {}".format(ans, text[topics.index(match)])
    else:
        return "Sorry, I didn't understand that."


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
