from transformers import MarianMTModel, MarianTokenizer

def translate_to_french(english_text):
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer(english_text, return_tensors="pt")
    translation_ids = model.generate(**inputs)
    french_translation = tokenizer.batch_decode(translation_ids, skip_special_tokens=True)

    return french_translation[0]

if __name__ == "__main__":
    english_text = input("Enter the English text: ")
    french_translation = translate_to_french(english_text)
    print(french_translation)
