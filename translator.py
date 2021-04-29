import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
her_lang = 'es'
try:
    with sr.Microphone() as source:
        print('Speak now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language= her_lang)
        print(text)
except:
    pass
translated = translator.translate(text, dest= her_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang= her_lang)
converted_audio.save('new.mp3')
playsound.playsound('new.mp3')
# print(googletrans.LANGUAGES)