import speak
import inputs
import datetime
import webbrowser
import weather
import quick_question
import chem_qs
from time import ctime
import identify


def respond(voice_data):
    if 'your name' in voice_data:
        speak.jarvis_speak(
            'My name is Jarvis, just a rather very intelligent system, except a lobotomized version')

    if 'chemistry question' in voice_data:
        chem_element = inputs.record_audio(
            'I know the periodic table, what element do you want to know about?')
        chem_qs.el_lookup(chem_element)

    if 'time is it' in voice_data:
        speak.jarvis_speak(ctime())

    if 'search' in voice_data or 'can you find' in voice_data:
        search = inputs.record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak.jarvis_speak('Here is what i found for ' + search)

    if 'find location' in voice_data:
        location = inputs.record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak.jarvis_speak('Here is the location of ' + location)

    if 'exit' in voice_data or "good bye" in voice_data or "ok bye" in voice_data:
        speak.jarvis_speak('Always happy to help')
        exit()

    if 'weather' in voice_data:
        city_name = inputs.record_audio('whats the city name')
        report = weather.weather_report(city_name)
        speak.jarvis_speak(report)

    if 'quick question' in voice_data:
        question = inputs.record_audio('whats the question')
        answer = quick_question.ask(question)
        speak.jarvis_speak(answer)

    if 'say hello' in voice_data or 'introduce yourself' in voice_data:
        names = identify.identify(identify.peek())
        hour = datetime.datetime.now().hour
        for name in names:
            if hour >= 0 and hour < 12:
                speak.jarvis_speak('Hello, Good Morning ' + name)
            elif hour >= 12 and hour < 18:
                speak.jarvis_speak('Hello, Good Afternoon ' + name)
            else:
                speak.jarvis_speak('Hello, Good Evening ' + name)

    if 'open my email' in voice_data:
        url = 'https://mail.google.com/mail/u/0/#inbox'
        webbrowser.get().open(url)
        speak.jarvis_speak('Opening email')

    if 'play some music' in voice_data:
        url = 'https://www.youtube.com/playlist?list=PLBuxhzrxSigRFEI1WIMgsLvSUAMXr3-xX'
        webbrowser.get().open(url)
        speak.jarvis_speak('Dropping needle')
