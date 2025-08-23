import joblib       # Used to load the saved model and vectorizer
import string       # For cleaning the email text (punctuation removal)

# === STEP 1: Load the trained model and vectorizer ===
# These were saved by train_model.py into the ../models/ folder
model = joblib.load('/Users/surya/Documents/Projects/phishing email/models/phishing_model.pkl')
vectorizer = joblib.load('/Users/surya/Documents/Projects/phishing email/models/vectorizer.pkl')

# === STEP 2: Define text cleaning function ===
# This helps standardize the input so it matches training format
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# === STEP 3: Collect email input from the user ===
# Multiline input until the user presses ENTER twice
print("📩 Paste the email content below (press ENTER twice to finish):")
email_lines = []
while True:
    line = input()
    if line.strip() == "":  # Stop when empty line is entered
        break
    email_lines.append(line)

# Join all lines into a single string (simulate full email)
email_text = "\n".join(email_lines)

# Clean the input email
cleaned_text = clean_text(email_text)

# Convert the email into the same TF-IDF vector format used in training
vectorized_input = vectorizer.transform([cleaned_text])

# === STEP 4: Make prediction ===
# 1 = phishing, 0 = safe
prediction = model.predict(vectorized_input)[0]

# === STEP 5: Output the result ===
if prediction == 1:
    print("\n⚠️ This email is likely a PHISHING attempt.")
else:
    print("\n✅ This email appears to be SAFE.")
