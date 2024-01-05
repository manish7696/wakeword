import speech_recognition as sr

def listen_and_recognize(wake_word):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for the wake word...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio_data)
        print("You said:", recognized_text)

        if wake_word.lower() in recognized_text.lower():
            print("Wake word detected!")
        else:
            print("Wake word not detected.")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    wake_word = "hello"  # Change this to your desired wake word
    listen_and_recognize(wake_word)
