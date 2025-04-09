import streamlit as st

st.set_page_config(page_title="Credit Score Predictor")


st.markdown(
    """
    ### Advanced Coding Group Project
    """)

st.markdown("Here in this project we have built a credit score predictor using several machine learning models." \
            "The data was including inconsistencies and biases, so we used several techniques to remove them." \
            "Afterwards, we conducted a thorough EDA to understand the data better." \
            "Before we continue with the model training, we ran Variance Inflation Factor (VIF) to check for multicollinearity." \
            "Finally, we trained several models and compared their performance." \
            "However, we noticed that there are 2 feature which are causing biases."\
            "You can easily check the bias between the two models by using the same input data and only changing the city."\
            "However, don't forget that you are free to mess around and try different values for the input data. :D")

st.markdown("### Group Members")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Davoud Danish")

with col2:
    st.markdown("#### Janhvi Goje")

with col3:
    st.markdown("#### Ayham Alroumi")