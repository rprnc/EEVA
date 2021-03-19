import speech_recognition as sr
import speak


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak.jarvis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak.jarvis_speak('Sorry, I did not get that')
        except sr.RequestError:
            speak.jarvis_speak('Sorry, my speech recognition service is down')
        return voice_data
