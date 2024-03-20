import pyttsx3
engine=pyttsx3.init()
while(True):
 x=input("enter what u wanna say")
 engine.say(f"{x}")
 engine.runAndWait()
 if x=="end":
     engine.say("by by")
     engine.runAndWait()
     break