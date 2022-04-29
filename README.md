# Legal.ly - _law for all_
**Team Hopium - Hackathon Coding Sprint**
<br/>
**Problem Statement - Chatbot - Legal, Tax, and Compliance**
<br/>

![legal.ly_main](https://github.com/sudo-logic/Project-Legal.ly/blob/main/forgithub.png)

<br/>**Legal.ly**, is a chatbot that provides factual and appropriate information to legal queries from central acts. 
<br/>
<br/>This chatbot can be effectively applied to the legal sector providing swift access to justice. Legal.ly is designed specifically to help individuals seek accurate legal information. Information is sourced directly from the Central Acts of India, hence eliminating any misinformation.

Our project aims at building a specialised task-oriented chatbot, named as Legal.ly, which will allow users to ask questions; thus,democratizing legal, tax and compliance. 

The prime objective is to structure an intelligent chatbot, which is not only data-driven but also incorporates machine learning and deep learning algorithms to map input sequences to output sequences.
<br/>Legal.ly provides 24-hour legal assistance and is reliable in emergencies too.
<br/>
<br/>Legal.ly responds to both voice and text for increased accessibility.

## For more information [Presentation](https://pitch.com/public/9c74e7cd-dc0f-4d6a-8659-0bdcf709b1fd)

# Methodology
This project is a hybrid of pure experimentation and a multitude of algorithms that we incorporated to ensure accuracy and conciseness.

Seq2Seq model was put under training, using diverse datasets and tensorlayer, spacy and pickle libraries. We used this to tackle problems like machine translation, text summarization and question-answering. But since it's generative we had to leave it midway. 
Along with that, we've used regex for information extraction. Applied lemmatization to provide context to the model. Currently, we are planning on implementing nearest keyword recognition. Once we find the nearest keywords, relevant information can be easily generated.  NearestNeighbours using sklearn is one way we've thought of.

Because of the time crunch, we couldn't train the model fully and add a few more functionalities for our chatbot to be conversational and knowledge-oriented.

Hence, we had to go with our second plan of using Fuzzy Query Matching to map the input to the most accurate topic in our dataset.
We now use roberta-base-squad2 (a Question Answering Model trained on the SQuAD2.0 dataset), which extracts answers from given inputs of Question and Context. Narrowing down on the topic helps us narrow down on the data that we send to roberta making the response more accurate.

GPT-3, Seq2Seq, reinforcement learning based chatbots and a hybrid of those are some of the methodologies we've tinkered around with.


## UI MOCKUPS
![Why_UPN](https://github.com/sudo-logic/Project-Legal.ly/blob/main/UI_Mockup.png)

## Deployment

To deploy this project run

```bash
  npm start
```


 


## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```
