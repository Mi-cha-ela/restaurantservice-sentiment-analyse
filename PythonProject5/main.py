import re
import joblib

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "log_reg_model.pkl")
tfidf = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


def predict_sentiment(review):
    cleaned_review = clean_text(review)
    review_tfidf = tfidf.transform([cleaned_review])

    prediction = model.predict(review_tfidf)[0]
    probabilities = model.predict_proba(review_tfidf)[0]

    sentiment = "Positiv" if prediction == 1 else "Negativ"
    confidence = probabilities[prediction]

    return sentiment, confidence


review = input("Gib eine englische Restaurantbewertung ein: ")

sentiment, confidence = predict_sentiment(review)

print(f"\nVorhersage: {sentiment}")
print(f"Wahrscheinlichkeit: {confidence:.1%}")
