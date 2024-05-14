from googletrans import Translator

def translate_to_english(words):
    translator = Translator()
    translations = {}
    for word in words:
        translation = translator.translate(word, dest='en')
        translations[word] = translation.text
    return translations

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
english_translations = translate_to_english(french_words)

print(english_translations)
