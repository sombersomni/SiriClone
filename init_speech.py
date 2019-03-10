import speech_recognition as sr
from play_audio import play_audio

def init_speech():
    #initializes spech recognizer
    r = sr.Recognizer()
    print("Listening...")
    #play notification to start recording
    play_audio("./audio/start_rec.wav")

    #setups up audio recording
    with sr.Microphone() as source:
        print("Speak!")
        #recognizer listens to source input
        audio = r.listen(source)

    play_audio("./audio/end_rec.wav")

    command = ""

    try:
        #interpret speech into text
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand what you said!")

    print("Your command: ")
    return command