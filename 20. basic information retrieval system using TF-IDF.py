from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "TF-IDF stands for Term Frequency-Inverse Document Frequency.",
    "It is a numerical statistic used in information retrieval to reflect the importance of a word in a document.",
    "TF-IDF value increases proportionally to the number of times a word appears in a document and is offset by the number of documents in the corpus that contain the word.",
    "Cosine similarity measures the cosine of the angle between two non-zero vectors.",
    "It is used to measure how similar two documents are irrespective of their size."
]

# User query
query = "What is TF-IDF?"

# Combine documents and query
corpus = documents + [query]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Calculate TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(corpus)

# Calculate cosine similarity between the query and documents
cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

# Get document ranks
document_ranks = list(enumerate(cosine_similarities[0]))

# Sort documents by rank
document_ranks.sort(key=lambda x: x[1], reverse=True)

# Display ranked documents
print("Ranked Documents:")
for rank, similarity in document_ranks:
    print(f"Document {rank + 1}: Similarity = {similarity:.4f}")
    print(documents[rank])
    print()

# Get the most relevant document
most_relevant_document = document_ranks[0][0]
print(f"The most relevant document to the query is Document {most_relevant_document + 1}.")
