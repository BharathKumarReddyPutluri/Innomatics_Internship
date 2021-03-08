import streamlit as st
import numpy as np
from sklearn.svm import SVC
from pickle import dump, load

def predict(arr):

    # Loading pretrained svm_rbf classifier from pickle file
    classifier = load(open('Pickle/svm_rbf.pkl','rb'))

    # Prediction
    prediction = classifier.predict(arr)

    return prediction

def main():
    Value_1=st.number_input('Enter Value_1 :')
    Value_2=st.number_input('Enter Value_2 :')
    arr = np.array([Value_1,Value_2]).reshape(1,-1)

    prediction = predict(arr)
    click = st.button("SUBMIT")

    if click:
        if(arr.any()):
            st.subheader("Prediction:")
        if(prediction == 0):
            st.write("Negative :cry:")
        else:
            st.write("Positive :sunglasses:")



if(__name__ == '__main__'):
    main()
