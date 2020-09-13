import requests
import os
import tkinter
from tkinter import *
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1 as nlu
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions
from watson_developer_cloud import ToneAnalyzerV3 as ta
from watson_developer_cloud import visual_recognition_v3 as vr
from tkinter.messagebox import *
import os
import random
import webbrowser


window=tkinter.Tk()
window.geometry("600x600")
window.resizable(0,0)
window.title("sign in")
window.configure(background="lightblue")

def save():

    print("------------------NATURAL LANGUAGE UNDERSTANDING--------------------------------")
    print(" ")
    inputvalue=txt.get("1.0","end-1c")
    print("THE TEXT VALUE : {}".format(inputvalue))
  
    
    #TRYING PART 1 NATURAL LANGUAGR PROCESSING
    
    
    instance=nlu(version='2018-09-28', url='https://gateway.watsonplatform.net/natural-language-understanding/api', username='4fec5c70-29b5-46ec-94d5-5d448397d74d',
             password='kdP3SLBxHdgJ', iam_apikey='TpBB8KBJl0R934T-zwxoz9RBpcK0MG-CqkHPAD9LO-pn')
    text_analysis=instance.analyze(text=inputvalue,features= Features(
        keywords=KeywordsOptions(
	 emotion=True,
	 sentiment=True,
	 limit=2))).get_result()
    #print(text_analysis)

    data=text_analysis
    nlux=data['keywords'][0]['emotion']
    print(nlux)

    #PART 2 TONE ANALYZER

    print("                                                   ")

    #PART 2 TONE ANALYZER

    print("------------------TONE ANALYZER--------------------------------")
    print(" ")

    inputvalue1=txt1.get("1.0","end-1c")
    print("THE INPUT VALUE : {}".format(inputvalue1))

    instance = ta(version='2017-09-21',iam_apikey='8hwsadQISk5c9fQhQsMZRdP8V93FnY57RVa37xCAVWbZ',username='5aa9fc7f-913a-49b9-be04-089f7e13adb8',password='TyvjadwzXHeX',url='https://gateway.watsonplatform.net/tone-analyzer/api')
    text=inputvalue1
    tone_analysis = instance.tone({'text': text},content_type='application/json').get_result()
    data=tone_analysis
    tone_analyzer=[]
    #print(data)
    for i in range(len(data['document_tone']['tones'])):
        tone_analyzer.append(data['document_tone']['tones'][i]['tone_name'])
    print(tone_analyzer)

    
    #PART 3 IMAGE PROCESSING
    #PART 3 IMAGE PROCESSING

    print("------------------VISUAL RECOGNITION--------------------------------")
    print(" ")
    inputvalue2=txt2.get("1.0","end-1c")
    print("THE PATH PROVIDED : {}".format(inputvalue2))


    url = 'https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19'
    files = {'images_file': open(inputvalue2,'rb')}
    resp = requests.post(url, auth=('apikey', 'OIZau-m5p-hdgly2PHmD-Dm2sqyipFeBAEaAVsLmm7J6'), files=files)

    print(resp.content)

    #DEMO TRAL EDISION

    t_a_ans=False
    nulx_ans=False

    
    for each in tone_analyzer:
        if each=="Sadness":
            t_a_ans=True

    if round(nlux['sadness'], 2)>0.30:
        nulx_ans=True
    

    if t_a_ans or nulx_ans:
        print("SIR,YOU NEED HELP :")
        print(" ")
        print("-------------------LET ME RECOMMEND YOU A FEW HELPFUL SUGGESTIONS--------------------------")
        print(" ")

        print("YOU ARE A BIT SAD AND LONELY, LETS HEAR A MOTIVATIONAL SONG OR VIDEO")

        webx = ["http://www.brainyquote.com/", "http://www.entrepreneur.com/", "http://www.dumblittleman.com/",
                "http://theinvisiblementor.com/", "http://tinybuddha.com/",
                "http://fiercegentleman.com/10-qualities-fierce-gentleman/"]

        lisx = ["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3", "video.mp4", "comedy.mp4"]

        valx = random.randint(0, 6)

        print(" ")
        print("PLEASE READ A MOTIVATIONAL QUOTE TO ENCOURAGE YOURSELF")
        os.system("1.mp3")
        os.system("quote.pdf")

        print(" ")
        print("LETS's VISIT A WEBISTE THAT MIGHT HELP YOU MY DEAR FRIEND")
        webbrowser.open(webx[valx])
 
    else:
        print("-------------------------------------------------------------")
        print("YOU ARE ABSOLUTLY MENTALLY FIT AND SOUND")

  

    


#-------------------------registration form----------------
def show():
    global txt
    global txt1
    global txt2
    global txt3
    global txt4
    global regwindow
    global tone_analyzer
    global nlux
    global vrx
    regwindow=tkinter.Tk()
    regwindow.geometry("1200x500")
    regwindow.resizable(0,0)
    regwindow.title("sign up")
    regwindow.configure(background="lightblue")
  





    
#------------------------name-------------------------------
    lb=tkinter.Label(regwindow,text="NATURAL LANGUAGE UNDERSTANDING(ENTER TEXT)",font=('Arial',14,'bold'),bd="10",fg="navy")
    lb.grid(row=0,column=0,padx=30,pady=30)

    txt=Text(regwindow,height=4,width=50)
    txt.grid(row=0,column=1,padx=20,pady=30)


    

    

#------------------LOGIN-------------------------------
    lb1=tkinter.Label(regwindow,text=" TONE ANALYZER(ENTER TEXT)",font=('Arial',14,'bold'),bd="10",fg="navy")
    lb1.grid(row=1,column=0,padx=30,pady=30)

    txt1=Text(regwindow,height=4,width=50)
    txt1.grid(row=1,column=1,padx=20,pady=30)
#--------------password box-----------------------------------
    lb2=tkinter.Label(regwindow,text="IMAGE PATH",font=('Arial',14,'bold'),bd="10",fg="navy")
    lb2.grid(row=2,column=0,padx=20,pady=30)

    txt2=Text(regwindow,height=4,width=50)
    
    txt2.grid(row=2,column=1,padx=20,pady=30)

#----------------URL LINk--------------------------------
    """lb3=tkinter.Label(regwindow,text="URL LINK",font=('Arial',14,'bold'),bd="10",fg="navy")
    lb3.grid(row=3,column=0,padx=30,pady=30)
    txt3=Text(regwindow,height=2,width=30)
    
    txt3.grid(row=3,column=1,padx=20,pady=30)"""

#----------------register button------------------------
    btn3=tkinter.Button(regwindow,text="Submit",font=('Arial',14,'bold'),bd="10",fg="navy",command=lambda: save())
    btn3.grid(row=4,column=0,columnspan=2)
    
def check():
    pass



#----------------window 1----------------------------

#----------- button------------------



"""btn=tkinter.Button(window,text="facebook",font=('Arial',14,'bold'),bd="10",fg="navy",command=show)
btn.grid(row=8,column=0,padx=10,pady=10,columnspan=2)
btn.place(relx=0.3,rely=0.5,anchor=CENTER)"""

btn1=tkinter.Button(window,text=" IBM ",font=('Arial',14,'bold'),bd="10",fg="navy",command=show)
btn1.grid(row=80,column=20,columnspan=8)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)






#--------------yotube button-----------------    

"""btn2=tkinter.Button(window,text="youtube",font=('Arial',14,'bold'),bd="10",fg="navy",command=show)
btn2.grid(row=8,column=4,padx=10,pady=10,columnspan=2)
btn2.place(relx=0.7,rely=0.5,anchor=CENTER)"""




lb=tkinter.Label(window,text="SENTIMENT ANALYSIS",font=('Italic',20,'bold'),bd=10,width=30)
lb.pack()
