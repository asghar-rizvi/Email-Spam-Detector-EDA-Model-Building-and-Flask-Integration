import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
__model = None
__vectorizer = None
__text = None

def load_data():
    global __model
    global __vectorizer

    # print('start')
    with open('model/model.pickle','rb') as f:
        __model = pickle.load(f)
    with open('model/vectorizer.pickle','rb') as f:
        __vectorizer = pickle.load(f)
    # print('end')


def transform(text):
    # setting lower text
    text = text.lower()
    text = nltk.word_tokenize(text)
    list = []
    # checking if it is only alpha numeric
    for i in text:
        if i.isalnum():
            list.append(i)
    text = list[:]
    list.clear()

    ## removing stop words and punctuations
    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            list.append(i)

    text = list[:]
    list.clear()
    ps = PorterStemmer()
    for i in text:
        list.append(ps.stem(i))
    return " ".join(list)


def vectorize_text(text):
    transform_text= transform(text)
    x = __vectorizer.transform([transform_text]).toarray()
    return x
def predict(text):
    vectorized_text = vectorize_text(text)
    res = __model.predict(vectorized_text)
    if res[0] == 0:
        return 'HAM'
    else:
        return 'SPAM'

if __name__=='__main__':
    load_data()
    print(predict('Hello my name is asghar! i am 50% sure about that'))
    # print(transform('Hello my name is asghar! i am 50% sure about that'))