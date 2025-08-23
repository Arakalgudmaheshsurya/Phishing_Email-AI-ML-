# Import necessary libraries
import pandas as pd                     # For handling data
import string                           # For text cleaning
import joblib                           # For saving model and vectorizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# === STEP 1: Load Dataset ===
# Load the CSV file containing email texts and their labels (phishing or not)
data = pd.read_csv('/Users/surya/Documents/Projects/phishing email/Data/phishing_email.csv')  # Adjust path as needed

# === STEP 2: Clean Email Text ===
# Define a simple function to clean the email text: lowercase and remove punctuation
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Apply the cleaning function to the email content
data['text'] = data['text_combined'].apply(clean_text)



# Extract the target labels (0 = legitimate, 1 = phishing)
labels = data['label']

# === STEP 3: Text Vectorization ===
# Use TF-IDF to convert text into numeric features
# This helps the model understand which words are important
tfidf = TfidfVectorizer(stop_words='english')  # Ignore common English stopwords
X = tfidf.fit_transform(data['text'])  # Transform text to TF-IDF features
y = labels

# === STEP 4: Split Data ===
# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === STEP 5: Train Logistic Regression Model ===
# Logistic Regression is a simple and effective classifier for binary tasks
model = LogisticRegression()
model.fit(X_train, y_train)

# === STEP 6: Evaluate the Model ===
# Predict on test set
y_pred = model.predict(X_test)

# Print the confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Print precision, recall, F1-score, and accuracy
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# === STEP 7: Save Model and Vectorizer ===
# Save the trained model and vectorizer to disk using joblib
joblib.dump(model, '/Users/surya/Documents/Projects/phishing email/models/phishing_model.pkl')
joblib.dump(tfidf, '/Users/surya/Documents/Projects/phishing email/models/vectorizer.pkl')

print("\nModel and vectorizer saved successfully.")
