# 📧 Phishing Email Classifier

A machine learning-based phishing detection system that uses NLP to classify emails as phishing or legitimate. This project includes both a command-line interface (CLI) and a web interface built with Streamlit.

---

Features

Classifies emails as **Phishing** or **Safe**
Uses **TF-IDF** for feature extraction
Logistic Regression model for classification
Preprocesses raw email content (lowercasing, punctuation removal)
Streamlit app for interactive user experience
Model and vectorizer are saved using `joblib`







## 📂 Project Structure

```
phishing-email-classifier/
├── app/
│   └── streamlit_app.py          # Web app using Streamlit
├── data/
│   └── phishing_emails.csv       # Dataset (from Kaggle or similar)
├── models/
│   ├── phishing_model.pkl        # Trained ML model
│   └── vectorizer.pkl            # TF-IDF vectorizer
├── src/
│   ├── train_model.py            # Train and evaluate model
│   └── predict.py                # CLI tool for predictions
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 📦 Requirements

Install the required packages:

bash
pip install -r requirements.txt


Contents of `requirements.txt`:


pandas
scikit-learn
joblib
streamlit






This project uses a labeled phishing email dataset. You can use the one from Kaggle:

**[Phishing Email Detection Dataset – Kaggle](https://www.kaggle.com/datasets/charlesherreraphishingemails)**

Ensure the CSV is saved as:


data/phishing_emails.csv


---

 Model Training

To train the model from scratch:


cd src
python train_model.py


This will:
- Load and clean the dataset
- Vectorize the email text using TF-IDF
- Train a logistic regression model
- Save the model and vectorizer in the `models/` folder

---

Run the CLI Predictor


cd src
python predict.py


Paste in email content, press Enter twice, and it will return:

- ✅ "SAFE"  
- ⚠️ "PHISHING"



 Launch the Streamlit App

From the project root:


streamlit run app/streamlit_app.py


Then open [http://localhost:8501](http://localhost:8501) in your browser.



 Example Input


Subject: Urgent - Verify Your Account

Dear user, your account has been locked. Please login immediately at http://phishy-link.com to restore access.

- IT Support


Output:

⚠️ This email is likely a PHISHING attempt.



## 📊 Model Performance (Test Data)

| Metric     | Score |
|------------|-------|
| Accuracy   | 98%   |
| Precision  | 98%   |
| Recall     | 99%   |
| F1-Score   | 98%   |

---

## 👨‍💻 Author

**Surya**  
Master’s Student | Cybersecurity & AI Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/surya-am/)  
💻 [GitHub](https://github.com/Arakalgudmaheshsurya)

> Replace links with your actual LinkedIn & GitHub profile



Disclaimer

This project is for **educational and demonstration purposes only**.  
Do not use it to make real-world security decisions without professional validation.

