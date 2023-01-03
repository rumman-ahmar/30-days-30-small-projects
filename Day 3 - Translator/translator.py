# pip install googletrans==3.1.0a0 to install the library

from googletrans import Translator
translator = Translator()

sentance = "Hello, I am learning Python and I am working on small projects"
language = translator.detect(sentance)
print(f'{language.lang} language has been detected.')

translated_sentance = translator.translate(sentance, dest='hi')
print(translated_sentance.text)
