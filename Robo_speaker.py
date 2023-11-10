import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by JUNAID.")

    while True:
        
        text = input("Enter what you want to speak: ")

        if text == "q":
            break

        command = pyttsx3.init()
        command.say(text)
        command.runAndWait()
