from googletrans import Translator

translator = Translator()

sentence = "HELLO"

detected = translator.detect(sentence)

print(detected) 
print(detected.lang)  