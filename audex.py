import pyaudio
import speech_recognition as s_r
import pyttsx3

def menu():
    print("\nOptions:")
    print("1. Convert audio to text")
    print("2. Convert text to audio")
    print("3. Quit")
    user_input = input("What would you like to do? ")
    return user_input

def audio_to_text():
    while True:
        print("\nSelect your input source: ")
        print("1. Select an mp3 file")
        print("2. Use the mic")
        choice = input(": ")

        match choice:
            case "1":
                source_file(input("Enter the name of the file: "))
                return
            case "2":
                source_mic()
                return
            case _ :
                print("Invalid choice. Try again.")
    
def source_mic():
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

def source_file(filename):
    r = s_r.Recognizer()
    print("Listening:.....")
    audio = r.listen(filename)
    print(audio)
    return

def text_to_audio():
    filename = input("Enter the filename of the file you want to narrate: ")
    with open(filename, 'r') as input_file:
        text = input_file.read()
        while True:
            print("\nOutput type: ")
            print("1. Narrate it")
            print("2. save as a .mp3 file")
            choice = input(": ")

            match choice:
                case "1":
                    text_speaker(text)
                    return
                case "2":
                    text_mp3(text)
                    return
                case _:
                    print("Invalid choice. Try again.") 

def text_speaker(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def text_mp3(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'sample.mp3')
    engine.runAndWait()

def audex():
    while True:
        
        match menu():
            case "1":
                audio_to_text()
            case "2":
                text_to_audio()
            case "3":
                return
            case _:
                print("Invalid choice try again.")

def main():
    audex()


if __name__ == "__main__":
    main()