import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.linear_model import LogisticRegression

# ✅ Import custom feature class
from features import URLFeatures

# Load dataset
df = pd.read_csv("../emails.csv")
df['label'] = df['label'].map({'safe': 0, 'phishing': 1})

# Features
tfidf = TfidfVectorizer(stop_words='english')

features = FeatureUnion([
    ('text', tfidf),
    ('url', URLFeatures())
])

X = df['text']
y = df['label']

X_features = features.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_features, y)

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(features, open("vectorizer.pkl", "wb"))

print("Model trained and saved!")