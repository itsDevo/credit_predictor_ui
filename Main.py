import streamlit as st

st.set_page_config(page_title="Credit Score Predictor")


st.markdown(
    """
    ### Advanced Coding Group Project
    """)

st.markdown("In this project we have built a credit score predictor using several machine learning models." \
            "The dataset contains inconsistencies and biases, so we used several techniques to address and remove them." \
            "Afterward, we conducted a thorough EDA to understand the data better." \
            "Then, we trained several models and compared their performance." \
            "However, we noticed that there are 2 features which are causing biases."\
            "As an example, you can easily observe a bias between the two models by using the same input data and only changing the city."\
            "However, feel free to experiment with different input values to explore the model's behavior further.")

st.markdown("### Group Members")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Davoud Danish")

with col2:
    st.markdown("#### Janhvi Goje")

with col3:
    st.markdown("#### Ayham Alroumi")
