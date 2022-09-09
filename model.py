import joblib
import streamlit as st
model = joblib.load('customer.pkl')


def web_app():

    st.write("""
    # Customer Behaviour Analysis with Machine Learning
    ## This app predicts to which category a customer belongs too
   """)
    st.image("https://contentsquare.com/wp-content/uploads/2020/03/customer-behavior-analysis-scaled.jpeg")
    st.header("User Details")
    st.subheader("Kindly Enter The following Details in order to make a prediction")

    INCOME = st.number_input("INCOME",1600,120000)
    AGE = st.number_input("AGE",22,80)
    Month_Customer = st.number_input("Month_Customer",10,50)
    TotalSpendings = st.number_input("TotalSpendings",200,3000)
    Children = st.number_input("Children",0,3)
    
    if st.button("Press here to make Prediction"):
        
        result = model.predict([[INCOME,AGE,Month_Customer,TotalSpendings,
                                Children]])
        if result == 0:
            result = "zero_group"
        elif result == 1: 
            result = "first_group"
        elif result == 2: 
            result = "second_group"
        else : 
            result = "third_group"
        
        
        st.text_area(label='Category belongs to:- ',value=result , height= 100)
         
    
    
run = web_app()


# In[ ]:


# In[ ]:




