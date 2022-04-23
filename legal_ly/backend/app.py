# Flask app to accept chat messages and respond with a response


from email import header
from flask import Flask, request, render_template
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS, cross_origin
from matplotlib.pyplot import text
import pandas as pd

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# english_bot = ChatBot("Ron Obvious")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")

data = pd.read_csv('A2015-22.csv')

topics = list(data['title'])
text = list(data['text'])


# print(topics)

@app.route("/api", methods=['POST'])
@cross_origin()
def get_bot_response():
    msg = request.form['msg']
    print(msg)
    for i in topics:    
        print(i)
        if msg.lower().strip() == i.lower().strip():
            return text[topics.index(msg)]
    else:
        return "Sorry, I don't know that topic"

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)