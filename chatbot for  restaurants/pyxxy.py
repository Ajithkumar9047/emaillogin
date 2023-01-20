
import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()
import json
import time
time.clock = time.time

def restart():

    def con():
        try:
            with sr.Microphone() as source:
                print("speak....")
                audio_data = r.record(source, duration=5)
                print("Recognizing...")
                # convert speech to text
                text = r.recognize_google(audio_data)
                print(text)
                r1 = str(text.lower())
                return r1
        except:
            print("something wrong")
            restart()

    v = []

    def file():
        data_dict = {}
        for item in v:
            key, value = item.split(':')
            data_dict[key] = value
            with open('data.txt', 'w') as outfile:
                json.dump(data_dict, outfile)

    import re
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hi...Heartly welcome's you to Ajithkumar sekar 5 star Hotel  , I am sweety A..i chatBot")
    engine.say("Are you completed above 18 if completed say yes otherwise say no")
    engine.runAndWait()
    age = con()
    a = (f"age of 18:{age}")
    print(age)

    if re.findall("yes", age):
        v.append(a)
        engine.say("tell me your name")
        engine.runAndWait()
        name = con()
        na = (f"name:{name}")
        v.append(na)
        engine.say("tell me your mobile number")
        engine.runAndWait()
        num = con()
        nu = (f"mobile_number:{num}")
        v.append(nu)
        engine.say("tell me your address or location")
        engine.runAndWait()
        loc = con()
        lo = (f"address:{loc}")
        v.append(lo)
        engine.say("tell me your id proof type like adhaar, pan,etc..")
        engine.runAndWait()
        id_ty = con()
        it = (f"id_type:{id_ty}")
        v.append(it)

        engine.say(f"tell me your {id_ty} number")
        engine.runAndWait()
        id_proof = con()
        ip = (f"id_proof_number:{id_proof}")
        v.append(ip)
        engine.say("tell me your preferred room type example single or double")
        engine.runAndWait()
        room_ty = con()
        room_type = (f"room_type:{room_ty}")
        v.append(room_type)
        engine.say("tell me your arrival date fully")
        engine.runAndWait()
        arri = con()
        arrival = (f"Arrival date:{arri}")
        v.append(arrival)
        engine.say("tell me your depature date fully")
        engine.runAndWait()
        dep = con()
        depature = (f"Arrival date:{dep}")
        v.append(depature)

        print(v)
        engine.say("your room booking is under process , thank you for you patient")
        engine.runAndWait()
        file()
    elif age == "no":
        engine.say("you are not eligble to book rooms, sorry")
        engine.runAndWait()
    else:
        engine.say("retry")
        engine.runAndWait()
        restart()
restart()