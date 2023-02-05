import speech_recognition as sr
from time import sleep as sec


#We are going to define a function for the speech recognition task

def listener():
    mic = sr.Microphone()
    rec = sr.Recognizer()
#Here the file to be read will be an argument for the AudioFile instance in this case the Izu.wav file.

    audio_input = sr.AudioFile('Izu.wav')
    with audio_input as source:
        rec.adjust_for_ambient_noise(source)
        from_rec = rec.record(source)
        print('Trying to read audio record')
        
    try:
        prompt = rec.recognize_google(from_rec)
        print("\n")
        return prompt
        
    except:
        print("Oops! Something went wrong, network anomaly or an invalid API.")
        return None

    with mic as source:
        mic.adjust_for_ambient_noise(source)
        from_mic = mic.listen(source)
        print("Listening to voice record...")

    try:
        prompt_two = rec.recognize_google(from_mic)
        print("\n")
        return prompt_two

    except:
        print("Oops! Something went wrong, unstable network or an invalid API")
        return None



result  = listener()
answer_one = result.prompt

outcome  = Listener()
answer_two = outcome.prompt_two

sec(3)
print("The application is now closed")
