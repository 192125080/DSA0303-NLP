import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample text data and corresponding labels
text_data = ["This is a positive sentence.", "Negative sentiment in this one.", "Another positive example.", "Feeling sad today."]
labels = [1, 0, 1, 0]  # 1 for positive, 0 for negative

# Step 1: Feature Extraction
vectorizer = CountVectorizer()  # You can also use TfidfVectorizer for TF-IDF features
X = vectorizer.fit_transform(text_data)

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Step 3: Train a classifier (Naive Bayes in this example)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = classifier.predict(X_test)

# Step 5: Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))
