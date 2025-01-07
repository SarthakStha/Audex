import speech_recognition as s_r
import pyttsx3

#prints the user option menu
def menu():
    print("\nOptions:")
    print("1. Convert audio to text")
    print("2. Convert text to audio")
    print("3. Quit")
    user_input = input("What would you like to do? ")
    return user_input

# prints menu for audio to text and calls their respective functions as per the user
#input
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

#converts audio input from the mic to text on the terminal
def source_mic():
    r = s_r.Recognizer()
    mic = s_r.Microphone()
    while True:
        try:
            with mic as source:
                print("Listening:....")
                r.adjust_for_ambient_noise(source, duration= 0.2)
                audio = r.listen(source)

                print(r.recognize_google(audio))
            return
        except:
            print("Sorry, I did not get that, Try that again.")

#converts audio input from a audio file to text on the terminal
def source_file(filename):
    r = s_r.Recognizer()
    with s_r.AudioFile(filename) as source:
        audio = r.record(source)
        print(r.recognize_google(audio))
    return

# prints the menu for text to audio and handles the function call as per the user's input
def text_to_audio(filename):
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

# takes the name of the input file as the argument
# and narrates the text in the file
def text_speaker(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return

# takes the namr of the input file as the argument
# and ouputs an audio recording of the text file.
def text_mp3(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'sample.mp3')
    engine.runAndWait()
    return

def audex():
    while True:
        match menu():
            case "1":
                audio_to_text()
            case "2":
                text_to_audio(input("Enter the filename of the file you want to narrate: "))
            case "3":
                return
            case _:
                print("Invalid choice try again.")

def main():
    audex()


if __name__ == "__main__":
    main()