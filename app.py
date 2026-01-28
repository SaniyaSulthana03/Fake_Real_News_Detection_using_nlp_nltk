import streamlit as st
import pickle

# Load trained model
with open("fake_news_svm.pkl", "rb") as f:
    model = pickle.load(f)

# App title
st.set_page_config(page_title="Fake News Detection", layout="centered")

st.title("Fake News Detection App")
st.write(
    "Enter a news article below to classify whether it is **Fake** or **Real**."
)

# Text input
user_input = st.text_area(
    "News Article Text",
    height=250,
    placeholder="Paste the news article here..."
)

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]
        
        if prediction == 1:
            st.error("Fake News Detected")
        else:
            st.success("This is Real News")
