from tkinter import *
import math
import statistics
import numpy as np
from pygame import mixer
import speech_recognition
import pyttsx3

mixer.init()

is_pronoun = True

def click(value):
   
    ex = entryField.get()  # 789 ex[0:len(ex)-1]
    answer = ''

    try:
        if value == "voice":
            global is_pronoun
            is_pronoun = False
            if not is_pronoun:
                button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="mute", bg='dodgerblue3', fg='white',
                font=('arial', 18, 'bold'), activebackground='lime', command=lambda button=i: click(button))
                button.grid(row=0, column=0, pady=1)
            else:
                button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="voice", bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='lime', command=lambda button=i: click(button))
                button.grid(row=0, column=0, pady=1)
                is_pronoun = True
                
        elif value == 'C':
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)
            entryField.insert(0, ex)
            entryField2.delete(0, END)
            
            return

        elif value == 'CE':
            entryField.delete(0, END)
            entryField2.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'π':
            answer = math.pi
            entryField2.insert(0,ex)

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))
            entryField2.insert(0,ex)

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))
            entryField2.insert(0,ex)

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))
            entryField2.insert(0,ex)

        elif value == '2π':
            answer = 2 * math.pi
            entryField2.insert(0,ex)

        elif value == 'cosh':
            answer = math.cosh(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'tanh':
            answer = math.tanh(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'sinh':
            answer = math.sinh(eval(ex))
            entryField2.insert(0,ex)

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)
            entryField2.insert(0,ex)

        elif value == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')
            entryField2.insert(0,ex)
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3
            entryField2.insert(0,ex)

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2
            entryField2.insert(0,ex)

        elif value == 'ln':
            answer = math.log2(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'deg':
            answer = math.degrees(eval(ex))
            entryField2.insert(0,ex)

        elif value == "rad":
            answer = math.radians(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'e':
            answer = math.e
            entryField2.insert(0,ex)

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'x!':
            answer = math.factorial(ex)
            entryField2.insert(0,ex)

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            entryField2.insert(0,ex)
            return

        elif value == '=':
            entryField2.delete(0, END)
            answer = eval(ex)
            entryField2.insert(0,ex)

        elif value == 'fact':
            answer = math.factorial(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'round':
            answer = math.ceil(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'antilog':
            answer = math.exp(eval(ex))
            entryField2.insert(0,ex)

        elif value == "exp":
            answer = math.exp(eval(ex))
            entryField2.insert(0,ex)

        elif value == 'mean':
            answer = mean(ex)
            entryField2.insert(0,ex)

        elif value == 'median':
            answer = median(ex)
            entryField2.insert(0,ex)

        elif value == 'mode':
            answer = mode(ex)
            entryField2.insert(0,ex)
            
        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
                    
        if is_pronoun: 
          pronoun(ex,answer)

        entryField.insert(0, answer)

    except:
        pass

def mean(nums):
    if nums:
        num_list = [int(num) for num in nums.split(",")]
        mean = sum(num_list) / len(num_list)
    return mean

def median(nums):
    if nums:
        num_list = [int(num) for num in nums.split(",")]
        sorted_list = sorted(num_list)
        list_len = len(sorted_list)
        mid = list_len // 2

        if list_len % 2 == 0:
            median = (sorted_list[mid-1] + sorted_list[mid]) / 2
        else:
            median = sorted_list[mid]
        
        return median
    
def mode(nums):
    if nums:
        num_list = [int(num) for num in nums.split(",")]
        mode = statistics.mode(num_list)
    return mode

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a,b):
    l=math.lcm(a,b)
    return l

def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def pronoun(ex,answer):
     # Initialize text-to-speech engine
        engine = pyttsx3.init()
        
# Set properties for the engine
        engine.setProperty("rate", 150)  # Adjust the speaking rate
        engine.setProperty("volume", 1.0)  # Adjust the volume
        engine.say(ex)
        engine.runAndWait()
        eq="equalsto"
        engine.say(eq)
        engine.runAndWait()
        engine.say(answer)
        engine.runAndWait()
    

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1]) #mul(5.0,6.0)
                    entryField.delete(0,END)
                    entryField.insert(END,result)

                else:
                    pass
        except:
            pass



root = Tk()
root.title('Smart Calculator')
root.config(bg='dodgerblue3')
root.geometry('780x700+200+100')

logoLabel = Button(root, bg='dodgerblue3', width=5, height=2, bd=2, relief=SUNKEN, text='voice', fg='white',
                    font=('arial', 18, 'bold'), activebackground='lime', command=lambda button="voice": click(button))
logoLabel.grid(row=0, column=0, pady=10, padx=10)

entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

entryField2 = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
entryField2.grid(row=1, column=0, columnspan=8)

micImage = PhotoImage(file='microphone.png')
micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='tomato'
                   ,command=audio)
micButton.grid(row=0, column=7)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",                     
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",                    
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",                    
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",                    
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!",
                    "fact", "round", "antilog", "exp", ",", "mean", "median", "mode"]
                    

rowvalue = 2
columnvalue = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='lime', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=5, padx=5)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0


root.mainloop()
