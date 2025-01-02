import pyaudio

def menu():
    print("Options:")
    print("1. Convert audio to text")
    print("2. Convert text to audio")
    print("3. Quit")
    user_input = input("What would you like to do? ")
    return user_input


def audible():
    while True:
        
        match menu():
            case "1":
                print("You selected audio to text")
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