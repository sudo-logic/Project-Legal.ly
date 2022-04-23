
# Makeshift script for chatbot backend as the Model couldn't train in time :')
# Please read the README file to check our actual approach towards the problem

from email import header
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from matplotlib.pyplot import text
import pandas as pd
import difflib
import model

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
    msg = request.form['msg']

    match = difflib.get_close_matches(msg, topics, n=1)

    # print(difflib.get_close_matches(msg, greetings))
    
    if difflib.get_close_matches(msg, greetings):
        return "Hi There! Welcome to Legal.ly\nPlease type 'topics' to get a list of the topics I have knowledge on."
    
    # print(msg.lower().strip())
    
    if msg.lower().strip() in ['topics', 'topic']:
        response = 'You can ask me anything about the following topics:\n' + " | ".join(topics)
        return response

    if match:
        match = match[0]
        ans = model.get_answer(msg, text[topics.index(match)])
        return "I believe the answer to your query is: {}. \n For more context, please refer to the following text: {}".format(ans, text[topics.index(match)])
    else:
        return "Sorry, I didn't understand that."

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)