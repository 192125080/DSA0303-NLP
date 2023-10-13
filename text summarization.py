from summa import summarizer

# Sample text for summarization
text = """
Your long, detailed text goes here. Summarization algorithms are useful for condensing lengthy documents, 
articles, or any text into shorter, more manageable summaries. They can help users quickly grasp the key 
points and main ideas of a text. In this example, we will use the Summa library to perform extractive text summarization.
"""

# Extractive Summarization
summary = summarizer.summarize(text)

print("Original Text:")
print(text)
print("\nExtractive Summary:")
print(summary)

