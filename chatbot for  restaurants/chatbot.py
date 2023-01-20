# import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()
import time

time.clock = time.time
# Import "chatbot" from
# chatterbot package.
from chatterbot import ChatBot

# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer

# Give a name to the chatbot “corona bot”
# and assign a trainer component.


# Reading Microphone as source
# listening the speech and store in audio_text variable
def con():

     try:
        with sr.Microphone() as source:
            print("speak....")
            audio_data = r.record(source, duration=5)
            print("Recognizing...")
            # convert speech to text
            text = r.recognize_google(audio_data)
            print(text)


        response = chatbot.get_response(r.recognize_google(audio_data))
        print(response)
        import win32com.client

        # Calling the Dispatch method of the module which
        # interact with Microsoft Speech SDK to speak
        # the given input from the keyboard

        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        while 1:
            print("Enter the word you want to speak it out by computer")
            s = response
            speaker.Speak(s)
            rep()
            break
     except:
        print("Sorry, I did not get that")
        con()
def rep():
    i = int(input("enter 1 to speech"))
    if i ==1:
      con()
chatbot = ChatBot('corona bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

rep()
