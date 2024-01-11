import streamlit as st
import requests
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

st.title ("EmailGPT")
question = st.text_input("Enter the body of the email here.")
button = st.button("Check Spam")
ans = 0

raw_mail_data = pd.read_csv('mail_data.csv')
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')
mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1

X = mail_data['Message']
Y = mail_data['Category']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True)  
X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')
model = LogisticRegression()
model.fit(X_train_features, Y_train)


def checkSpam() :
    input_mail = [] 
    input_mail.append(question)
    input_data_features = feature_extraction.transform(input_mail)
    prediction = model.predict(input_data_features)
    if (prediction[0]==1):
      return 0
    else:
      #spammmmm
      return 1
 

if  question : 
    ans = checkSpam()
    st.header ("Answer")
    if ans == 1  :
        st.header("Spam Email\n No summary is being generated.")
    else :
        #if NOT spam
        st.header("Vaild Email\n Summary is being generated.")
        with st.spinner('Wait for Summaryy...'):
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            headers = {"Authorization": "Bearer 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"}
            wordlen = 30
            data = question
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()
            
            output = query({    
                "inputs": data,
                "parameters": {"min_length": min(30,len(question)), "max_length": len(question)}
            })[0]
            # aabhi print the summary 
        st.text("Summary of the Email is : \n")
        output["summary_text"]