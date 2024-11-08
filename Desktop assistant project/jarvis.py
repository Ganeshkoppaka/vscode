
from email import message
from re import S
from traceback import StackSummary
from winsound import MB_ICONQUESTION

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit



# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',25)
#     server.connect('smtp.gmail.com', 465)
#     server.ehlo
#     server.starttls
#     server.login('ganeshgunny444@gmail.com','password')
#     server.sendmail('ganeshgunny444@gmail.com',to,content)
#     server.close()





#this code is to listen by jarvis by using sapi api,windows have 2 inbuilt voice one male and female, we can also download externally   
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0],id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



#this below code is used to wish the user
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning! GAUNDU PRASAD")
    elif hour>=12 and hour<=18:
        speak("good afternoon!sir")
    else:
        speak("good evening!SIR")
    speak("hello! sir my name is jarvis,how can i help you sir?")    



def takecommand():
    #This function is used to take the command from the user(microphone input) and convert it into string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognising....')
        query=r.recognize_google(audio,language='en-in')#this is google engine which we use in mobile phones also
        print(f"user said:{query}")    
    except Exception as e:
        #print(e)
        print("say that again please.....")
        return "None"
    return query    
        



if __name__=='__main__':
    wishme()
    while True:
        query=takecommand().lower()
        #logic for executing tasks based on query

        if "wikipedia" in query:
            speak("searching wekipedia..")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'music' in query:
            music_dir="C:\\Users\\ganesh\\Music\\downloaded music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")    


        elif "time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strtime}")  

        elif "code" in query:
            vscode="C:\\Users\\ganesh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(vscode)


        elif "thank" in query:
            speak("welcome sir")
            exit()   

        elif "note" in query:
            with open ("note.txt","a") as op:
                speak("what should i write sir")
                note=takecommand()
                op.write(str([str(datetime.datetime.now())])+ ":"+ note +" ")
                speak("successfully written sir")


        elif "whatsapp" in query:
            whatsapp="C:\\Users\\ganesh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp.lnk"
            os.startfile(whatsapp)


        elif "message" in query:
            speak("whom do you want send message sir")
            whom=takecommand()
            speak("what do you want to send sir?")
            message=takecommand()
            timenow=datetime.datetime.now()
            hour=int(timenow.strftime("%H"))
            Minute=int(timenow.strftime("%M"))
            pywhatkit.sendwhatmsg("+8919455582",message,hour,Minute+1)
            speak("succesfully sent sir")   
        elif "play" in query:
            speak("what do you want to play sir")
            play=takecommand()
            pywhatkit.playonyt(play)
        elif "google " in query:
            speak("what should i search sir")
            search=takecommand()
            pywhatkit.search(search)    


        




        break




        # elif "email" in query:
        #     try:
        #         speak("what should i say?")
        #         content=takecommand()
        #         to="ganeshvenkat444@gmail.com"
        #         sendEmail(to,content)
        #         speak("email has been sent successfully")
        #     except Exception as e:
        #         print(e)
        #         speak("sorry i cant able to send email write now.please try again") 
                





