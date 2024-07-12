import pickle
import nltk;
import streamlit as st;
import string
from nltk.corpus import stopwords;
from nltk.stem import PorterStemmer;
# import sklearn;
nltk.download('punkt')

ps=PorterStemmer();

model=pickle.load(open('model.pkl','rb'));
tfidf=pickle.load(open('vectorizer.pkl','rb'));


def transform_text(text):
    l=[]
    text = text.lower()
    text = nltk.word_tokenize(text)


    for i in text:
        if i.isalnum():
            l.append(i)
    text=l[:]
    l.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            l.append(i)

    text=l[:]
    l.clear()
    for i in text:
        l.append(ps.stem(i));
    return " ".join(l);


st.title('Spam Detection Website')
input = st.text_area("")
if st.button("Check"):
    input=transform_text(input)
    input=tfidf.transform([input]);
    y=model.predict(input)
    print(y)
    if y==0:
        st.write("HAM")
    else:
        st.write("SPAM")


# input=transform_text("Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's")
# input=tfidf.transform([input]);
# y=model.predict(input)
# print(y)[0]