import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define a function to extract named entities and their relationships
def extract_named_entities(text):
    doc = nlp(text)
    
    # Extract named entities and their labels
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Extract relationships between named entities
    relationships = []
    for token in doc:
        if token.dep_ == "prep" and token.head.ent_type_ != 0:
            relationships.append((token.head.text, token.text, token.head.ent_type_))
    
    return named_entities, relationships

# Example usage
input_text = "Apple Inc. is headquartered in Cupertino, California. Tim Cook is the CEO."
entities, relationships = extract_named_entities(input_text)

print("Named Entities:")
for entity, label in entities:
    print(f"{entity} - {label}")

print("\nNamed Entity Relationships:")
for head, prep, obj_type in relationships:
    print(f"{head} - {prep} - {obj_type}")
