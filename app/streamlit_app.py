# === Import required libraries ===
import streamlit as st          # Streamlit for the web app interface
import joblib                   # To load the trained model and vectorizer
import string                   # To help clean punctuation from text

# === Load the trained model and TF-IDF vectorizer ===
# These files were saved earlier using train_model.py
model = joblib.load('/Users/surya/Documents/Projects/phishing email/models/phishing_model.pkl')         # Logistic Regression model
vectorizer = joblib.load('/Users/surya/Documents/Projects/phishing email/models/vectorizer.pkl')        # TF-IDF vectorizer

# === Function to clean email input ===
def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    return text

# === Streamlit App Interface ===

# App title at the top of the web page
st.title("📧 Phishing Email Classifier")

# Helpful description below the title
st.markdown("Enter an email message below and click **Check Email** to see if it's phishing or safe.")

# Create a text box for the user to paste email content
# 'height=200' gives the box more vertical space
email_input = st.text_area("Paste Email Content Here", height=200)

# When the user clicks the button, the following block runs
if st.button("Check Email"):

    # Check if the user entered any text
    if not email_input.strip():
        st.warning("⚠️ Please enter some email content.")
    
    else:
        # === STEP 1: Clean the input text ===
        cleaned = clean_text(email_input)

        # === STEP 2: Vectorize the cleaned text using TF-IDF ===
        vectorized = vectorizer.transform([cleaned])

        # === STEP 3: Predict with the trained model ===
        prediction = model.predict(vectorized)[0]  # 0 = safe, 1 = phishing

        # === STEP 4: Show the result to the user ===
        if prediction == 1:
            st.error("⚠️ This email is likely a **PHISHING** attempt.")
        else:
            st.success("✅ This email appears to be **SAFE**.")