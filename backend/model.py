from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import nltk

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def get_answer(question, context):
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)
    return res['answer']