import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import preprocess
from generate_report import generate_report
import pickle
nltk.download('punkt')


def create_response_df(text):
    sentences = sent_tokenize(text)
    response = pd.DataFrame(sentences)
    response_count = preprocess.preprocess_input_data(response)

    return response_count


def format_response(text):
    text = text.rstrip()
    q = [".", "?"]
    if text[-1:] not in q:
        text += ". "
        return text
    return text + " "


if __name__=="__main__":
    responses = ""

    print("These questions are to assess your mental health, please try and answer them truthfully\nDescribe what you feel using proper words instead of slangs and abbreviations, also make sure to properly describe the emotions that you are feeling.\nseperate each sentence with a full stop please.\nPlease answer truthfully!! This test is meant to help you.\n")

    responses += input('What do you think about the military and describe your experience here\n')
    responses = format_response(responses)
    responses += input('\nDo you have some health problems that you want to talk about?\n')
    responses = format_response(responses)
    responses += input('\nHow is your relationship with your fellow soldiers?\n')
    responses = format_response(responses)
    responses += input('\nDo you face any harrassment or bullying from superiors or your fellows?\n')
    responses = format_response(responses)
    responses += input('\nAre you satisfied with your compensation and your off times?\n')
    responses = format_response(responses)
    responses += input('\nDescribe your situation in your family, How do you feel about them?\n')
    responses = format_response(responses)
    responses += input('\nCan you explain why you joined the military?\n')
    responses = format_response(responses)
    responses += input('\nHow is life treating you?\n')
    responses = format_response(responses)
    responses += input('\nAre you able to sleep well at night?If not please explain what is bothering you\n')
    responses = format_response(responses)
    responses += input('\nHow do you spend your free time\n')
    responses = format_response(responses)
    responses += input('\nFinally is there any specific incident that affected you psychologically?\n')
    responses = format_response(responses)

    with open("model.pkl", 'rb') as file:
        lsvm = pickle.load(file)

    response_vector = create_response_df(responses)
    pred = lsvm.predict(response_vector)
    pred_perc = preprocess.cal_each_perc(pred)
    report = generate_report(pred_perc)

    print('\n')
    print(pred_perc)
    print(report)
