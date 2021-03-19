import inputs
import time
import speak
import time
import outputs


time.sleep(1)
speak.jarvis_speak('How can i help you?')
while 1:
    voice_data = inputs.record_audio()
    outputs.respond(voice_data)
