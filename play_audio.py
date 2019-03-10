import pyaudio
import wave

def play_audio(filename):
    CHUNK = 1024 #decimal version of 10bits
    wf = wave.open(filename, 'rb') #rb is read binary
    pa = pyaudio.PyAudio()

    #opens an audio stream from width of wav file sample width
    stream = pa.open( 
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    #reads first 10 bits and creates stream
    data_stream = wf.readframes(CHUNK)

    #play audio until complete
    while data_stream:
        #plays stream using pyaudio
        stream.write(data_stream)
        data_stream = wf.readframes(CHUNK)

    stream.close()
    pa.terminate()
