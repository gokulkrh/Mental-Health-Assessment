import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import preprocess
import pickle


def get_training_data():
    df1 = pd.read_csv("train.csv")
    df1_1 = pd.read_csv("test.txt", sep=";")
    df1_2 = pd.read_csv("val.txt", sep=";")
    df1 = df1.rename(columns = {'emotions': 'sentiment'}, inplace = False)          #renaming columns to make all three datasets uniform
    df1_1 = df1_1.rename(columns = {'emotion': 'sentiment'}, inplace = False)
    df1_2 = df1_2.rename(columns = {'emotion': 'sentiment'}, inplace = False)
    df1 = pd.concat([df1, df1_1, df1_2])                                            #combine train, test, val of this particular dataset to include all

    df2 = pd.read_csv("text_emotion.csv")
    df2 = df2.drop(['tweet_id', 'author'], axis=1)
    df2 = df2.rename(columns = {'content': 'text'}, inplace = False)
    df2 = df2[['text', 'sentiment']]                                                # re-arranging columns to make all three datasets uniform

    df3 = pd.read_csv("Suicide_Detection.csv")
    df3 = df3.drop(df3[df3.sentiment == 'non-suicide'].index)                       #dropping unnecessary rows and columns
    df3 = df3.drop(['Unnamed: 0'], axis=1)

    df = pd.concat([df1, df2, df3])

    df = df.replace(['love', 'joy', 'fun', 'happiness', 'enthusiasm', 'relief'], 'happy')
    df = df.replace(['sadness', 'worry', 'fear', 'boredom'], 'sad')                 # this is for improving performance
    df = df.replace(['suicide', 'hate', 'anger', 'empty'], 'severe')

    df = df.drop(df[df.sentiment == 'neutral'].index)
    df = df.drop(df[df.sentiment == 'surprise'].index)

    return df


def training(df):
    label_num = preprocessing.LabelEncoder()  # assigning numerical value to each class
    y = label_num.fit_transform(df.sentiment.values)
    # train test splitting
    X_train, X_test, y_train, y_test = train_test_split(df.text.values, y, stratify=y, random_state=42, test_size=0.3,
                                                        shuffle=True)
    count_vect = CountVectorizer(analyzer='word')  # vectorizing words using count vectorizer
    count_vect.fit(df['text'])
    X_train_count = count_vect.transform(X_train)
    X_test_count = count_vect.transform(X_test)

    lsvm = SGDClassifier(alpha=0.001, random_state=5, max_iter=15,
                         tol=None)  # lsvm gave highest accuracy among the models tested.
    lsvm.fit(X_train_count, y_train)
    y_pred = lsvm.predict(X_test_count)
    print('lsvm using count vectors accuracy %s' % accuracy_score(y_pred, y_test))

    model_name = "model.pkl"
    with open(model_name, 'wb') as file:
        pickle.dump(lsvm, file)

    return None


if __name__ == "__main__":
    training_data = get_training_data()
    print(training_data['sentiment'].value_counts())
    print(training_data.head(), "\n")
    preprocessed_text_data = preprocess.preprocess_training_data(training_data)
    training(preprocessed_text_data)


