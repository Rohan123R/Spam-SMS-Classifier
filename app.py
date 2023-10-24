import streamlit as st 
import pickle
import string
import nltk 

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


def transform_text1(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text :
        if(i.isalnum()):
            y.append(i)
    text = y[:]
    print(text)
    y.clear()
    

    for i in text:
        x = ps.stem(i)
        y.append(x)
    return y
def transform_text(text):
    text = transform_text1(text)
    y = []
    for i in text:
            if(i not in stopwords.words('english') and i not in string.punctuation):
               y.append(i)
    return y




tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))



input_sms = st.text_input("Enter the message")

if st.button("Predict"):
#preprocess text 
    transform_sms = transform_text(input_sms)
#vectorize 
    print(transform_sms)
    vector_input = tfidf.transform(transform_sms)
#predict 
    result = model.predict(vector_input)[0]

#display
    if result == 1:
        st.header("Spam")
    else :
        st.header("Not spam")