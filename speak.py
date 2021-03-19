import pyttsx3

jartard = pyttsx3.init()


def jarvis_speak(audio_string):
    jartard.say(audio_string)
    jartard.runAndWait()
