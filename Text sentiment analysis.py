import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Define a sample text
sample_text = "I love this product! It's amazing."

# Get the sentiment scores
scores = sid.polarity_scores(sample_text)

# Print the sentiment scores
print("Sentiment Scores:", scores)

# Determine the sentiment label
if scores['compound'] >= 0.05:
    sentiment = 'Positive'
elif scores['compound'] <= -0.05:
    sentiment = 'Negative'
else:
    sentiment = 'Neutral'

print("Sentiment:", sentiment)
