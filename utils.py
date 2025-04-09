import pickle
import streamlit as st

path_rf_pre_bias_removal = "rf_pre_bias_removal.pkl" #Model A
path_xgb_after_bias_removal = "xgb_after_bias_removal.pkl" #Model C

# Load the models

try:
    with open(path_rf_pre_bias_removal, 'rb') as f:
        model_a = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please check the file paths.")
    print("Model file not found. Please check the file paths.")

try:
    with open(path_xgb_after_bias_removal, 'rb') as f:
        model_c = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please check the file paths.")
    print("Model file not found. Please check the file paths.")