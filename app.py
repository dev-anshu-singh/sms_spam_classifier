import streamlit as st
import pickle
from text_transform import transform_text
import string

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter your message")


if st.button("Predict"):
    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]


    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
