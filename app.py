import streamlit as st
import pickle
import numpy as np


mod = pickle.load(open('mod6.pkl', 'rb'))
df = pickle.load(open('df1.pkl', 'rb'))


st.title("LOAN PREDICTOR")


# select gender
Gender = st.selectbox('Gender', df['Gender'].unique())

# Married or not
Married = st.selectbox('Married', df['Married'].unique())

# Education, graduation or not graduation
Education = st.selectbox('Education', df['Education'].unique())

# are you self employeed:
Self_Employed = st.selectbox('Self Employed',df['Self_Employed'].unique())

# income of applicant
ApplicantIncome = st.number_input("Applicant Income in 1000's")
ApplicantIncome = float(ApplicantIncome)

#income of co-applicant
CoapplicantIncome = st.number_input("Co-Applicant Income in 1000's")
CoapplicantIncome = float(CoapplicantIncome)

# how much amount you want as a loan
LoanAmount = st.number_input("Loan Amount in 1000's")
LoanAmount = int(LoanAmount)

# how much you'll take time to clear the loan
Loan_Amount_Term = st.number_input('Loan Amount Term in years')
Loan_Amount_Term = int(Loan_Amount_Term)

# your credit history
Credit_History = st.selectbox('Credit History', df['Credit_History'].unique())
Credit_History = int(Credit_History)

# your property area
Property_Area = st.selectbox('Property Area',['Urban', 'Rural', 'Semiurban'])


# predict
if st.button('PREDICT APPROVAL'):
    # Convert categorical to numerical
    # for gender to binary
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0

    # for married
    if Married == "Yes":
        Married = 1
    else:
        Married = 0


    if Education == "Graduate":
        Education = 1
    else:
        Education = 0


    if Self_Employed == "Yes":
        Self_Employed = 1
    else:
        Self_Employed = 0


    if Property_Area == "Urban":
        Property_Area = 2
    elif Property_Area == "Rural":
        Property_Area = 0
    else:
        Property_Area = 1

    # Query point :
    Query = np.array([Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,
                      LoanAmount, Loan_Amount_Term, Credit_History, Property_Area])
    Query = Query.reshape(1, 10)


    #st.title(mod.predict(Query)[0])
    if mod.predict(Query)[0] == 1:
        st.title('Your loan will be APPROVED')
    else:
        st.title('Sorry! you are not eligible to get loan')
