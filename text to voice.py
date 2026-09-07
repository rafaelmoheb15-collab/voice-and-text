from gtts import gTTS

lang = input("enter the language: ")

user_text = input("enter your text: ")

file_name = input("enter the file name: ")

tts = gTTS(text=user_text, lang=lang)

tts.save(file_name)