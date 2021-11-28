from nltk.corpus import stopwords
from textblob import Word
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import training
import re
df = training.get_training_data()
nltk.download('stopwords')
stop = stopwords.words('english')
nltk.download('wordnet')
nltk.download('punkt')


def de_repeat(text):                                                            #removing repeated words
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)


def preprocess_training_data(df):
    df['text'] = df['text'].str.replace("@[A-Za-z0-9_]+", " ")  # The text in the datasets are from tweets that contain links, #hashtags and @mentions
    df['text'] = df['text'].str.replace("#[A-Za-z0-9_]+", " ")  # These have to be removed
    df['text'] = df['text'].str.replace("^https?:\/\/.*[\r\n]*", " ")
    df['text'] = df['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))  # changing text to lowercase
    df['text'] = df['text'].str.replace('[^\w\s]', " ")  # removing punctuation and digits
    df['text'] = df['text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))  # removing stopwords
    df['text'] = df['text'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))  # lemmatizing words
    df['text'] = df['text'].apply(lambda x: " ".join(de_repeat(x) for x in x.split()))  # removing repeated characters in words

    return df


def preprocess_input_data(text):
    text[0] = text[0].apply(lambda x: " ".join(x.lower() for x in x.split()))  # preprocessing text for testig and vectorizing
    text[0] = text[0].str.replace('[^\w\s]', " ")
    text[0] = text[0].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    text[0] = text[0].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    text[0] = text[0].apply(lambda x: " ".join(de_repeat(x) for x in x.split()))

    count_vect = CountVectorizer(analyzer='word')
    df_ = preprocess_training_data(df)
    count_vect.fit(df_['text'])
    text_count = count_vect.transform(text[0])

    return text_count


def cal_each_perc(predictions):
    percs = []
    predictions = list(predictions)
    for i in range(3):
        a = predictions.count(i)
        percs.append((a/len(predictions))*100)
    return percs
