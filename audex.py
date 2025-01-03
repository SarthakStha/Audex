import pyaudio
import speech_recognition as s_r

def menu():
    print("Options:")
    print("1. Convert audio to text")
    print("2. Convert text to audio")
    print("3. Quit")
    user_input = input("What would you like to do? ")
    return user_input

def audio_te_text():
    r = s_r.Recognizer()
    mic = s_r.Microphone()

    while True:
        try:
            with mic as source:
                print("Listening:....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
        
        except KeyboardInterrupt:
            pass
    
        print(r.recognize_sphinx(audio))
        return


def audible():
    while True:
        
        match menu():
            case "1":
                audio_te_text()
                #print("You selected audio to text")
            case "2":
                print("You selected text to audio")
            case "3":
                return
            case _:
                print("Invalid choice try again.")

def main():
    audible()


if __name__ == "__main__":
    main()