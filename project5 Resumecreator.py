import tkinter
from tkinter import  messagebox
from PIL import ImageTk,Image, ImageDraw, ImageFont
import textwrap

def wrapt(textg,d,width,ipos,jpos,kdif,font1):
    wrap_text = textwrap.TextWrapper(width=width)
    lis = wrap_text.wrap(text=textg)
    i = ipos
    j= jpos
    k = kdif
    for line in lis:
        d.text((i, j), f"{line}", fill=(0, 0, 0), font=font1)
        j = j + k
    return d


def draw(m):
    image = Image.open("D:/resume_sample.jpeg")

    a1 = entry1.get()
    a2 = entry2.get()
    a3 = entry3.get()
    a4 = entry4.get()
    a5 = entry5.get()
    a6 = entry6.get()
    a7 = entry7.get()
    a8 = entry8.get()
    a9 = entry9.get()
    a10 = entry10.get()
    a11 = entry11.get()
    a12 = entry12.get()
    a13 = entry13.get()
    a14 = entry14.get()
    a15 = entry15.get()
    a16 = entry16.get()
    a17 = entry17.get()
    a18 = entry18.get()
    a19 = entry19.get()
    a20 = entry20.get()
    a21 = entry21.get()
    a22 = entry22.get()
    a23 = entry23.get()
    a24 = entry24.get()
    a25 = entry25.get()
    a26 = entry26.get()
    a27 = entry27.get()
    a28 = entry28.get()

    d = ImageDraw.Draw(image)
    fntBig = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',80)
    fntSmall = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 33)
    fntMedium = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
    fntJob = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 50)

    if (entry1.get()):
        d.text((90,50),f"{str(a1).capitalize()}",fill=(0,0,0),font=fntBig)
    if (entry2.get()):
        d.text((90,150), f"{str(a2).capitalize()}", fill=(0, 0, 0), font=fntBig)
    if (entry3.get()):
        d.text((46, 479), f"{a3}", fill=(0, 0, 0), font=fntSmall)
    if (entry4.get()):
        d.text((150, 607), f"{a4}", fill=(0, 0, 0), font=fntSmall)
    if (entry5.get()):
        d.text((10, 740), f"{str(a5).title()}", fill=(0, 0, 0), font=fntSmall)
    if(entry6.get()):
        d.text((7, 860), f"linked.com/in/{a6}", fill=(0, 0, 0), font=fntSmall)
    if (entry7.get()):
        a7 = str(a7).title()
        d = wrapt(a7,d,38,20,1620,30,fntSmall)
    if (entry8.get()):
        a8 = str(a8).title()
        d = wrapt(a8,d,38,20,1686,30,fntSmall)
    if (entry9.get()):
        d.text((20, 1760), f"(Session : {a9})", fill=(0, 0, 0), font=fntSmall)
    if (entry10.get()):
        d.text((20, 1812), f"{a10} CGPA in my Master's Degree", fill=(0, 0, 0), font=fntSmall)
    if (entry11.get()):
        d = wrapt(a11,d,38,20,1920,30,fntSmall)
    if (entry12.get()):
        d = wrapt(a12,d,38,20,1986,32,fntSmall)
    if (entry13.get()):
        d.text((20, 2060), f"(Session : {a13})", fill=(0, 0, 0), font=fntSmall)
    if (entry14.get()):
        d.text((20, 2112), f"{a14} CGPA in my Bachelor's Degree", fill=(0, 0, 0), font=fntSmall)
    if (entry15.get()):
        d.text((10, 2213), f"Completed higher education with {a15}%", fill=(0, 0, 0), font=fntSmall)
    if (entry16.get()):
        d.text((60, 1070), f" • {str(a16).title()}", fill=(0, 0, 0), font=fntMedium)
    if (entry17.get()):
        d.text((60, 1130), f" • {str(a17).title()}", fill=(0, 0, 0), font=fntMedium)
    if (entry18.get()):
        d.text((60, 1190), f" • {str(a18).title()}", fill=(0, 0, 0), font=fntMedium)
    if (entry19.get()):
        d.text((60, 1250), f" • {str(a19).title()}", fill=(0, 0, 0), font=fntMedium)
    if (entry20.get()):
        d.text((60, 1310), f" • ", fill=(0, 0, 0), font=fntMedium)
        d = wrapt(a20,d,28,100,1310,40,fntMedium)
    if (entry21.get()):
        d.text((20, 2450), f"Languages speak are :", fill=(0, 0, 0), font=fntMedium)
        d = wrapt(a21,d,25,100,2520,30,fntMedium)
    if (entry22.get()):
        d = wrapt(a22,d,70,680,700,60,fntMedium)
        d.text((680, 620), f"Job1/Internship : ", fill=(0, 0, 0), font=fntJob)
    if (entry23.get()):
        d = wrapt(a23,d,70,680,1040,60,fntMedium)
        d.text((680, 960), f"Job2/Internship : ", fill=(0, 0, 0), font=fntJob)
    if (entry24.get()):
        d = wrapt(a24,d,70,680,1380,60,fntMedium)
        d.text((680, 1300), f"Job3/Internship : ", fill=(0, 0, 0), font=fntJob)

    if (entry25.get()):
        d = wrapt(a25,d,70,680,1860,50,fntMedium)
        d.text((680, 1790), f"Project1 : ", fill=(0, 0, 0), font=fntJob)
    if (entry26.get()):
        d = wrapt(a26,d,70,680,2130,50,fntMedium)
        d.text((680, 2060), f"Project2 : ", fill=(0, 0, 0), font=fntJob)
    if (entry27.get()):
        d = wrapt(a27,d,70,680,2470,50,fntMedium)
        d.text((680, 2400), f"Project3 : ", fill=(0, 0, 0), font=fntJob)
    if (entry28.get()):
        d = wrapt(a28,d,70,680,180,40,fntMedium)

    if(m==0):
        image.show()
    elif(m==1):
        image.save("D:/Resume Creator 1.jpeg")
        msg("Image Saved","Thankyou for using Resume Creator. Your Image is Saved")

def msg(str1,str2):
    messagebox.showinfo(str1,str2)

def resetbutton():
    entry1.delete("0","end")
    entry2.delete("0","end")
    entry3.delete("0", "end")
    entry4.delete("0", "end")
    entry5.delete("0", "end")
    entry6.delete("0", "end")
    entry7.delete("0", "end")
    entry8.delete("0", "end")
    entry9.delete("0", "end")
    entry10.delete("0", "end")
    entry11.delete("0", "end")
    entry12.delete("0", "end")
    entry13.delete("0", "end")
    entry14.delete("0", "end")
    entry15.delete("0", "end")
    entry16.delete("0", "end")
    entry17.delete("0", "end")
    entry18.delete("0", "end")
    entry19.delete("0", "end")
    entry20.delete("0", "end")
    entry21.delete("0", "end")
    entry22.delete("0", "end")
    entry23.delete("0", "end")
    entry24.delete("0", "end")
    entry25.delete("0", "end")
    entry26.delete("0", "end")
    entry27.delete("0", "end")
    entry28.delete("0", "end")



if __name__ == '__main__':
    a = tkinter.Tk()
    a.geometry("1500x770")
    canvas = tkinter.Canvas(a, width = 1500, height = 770)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("D:\watermarrk.jpg"))
    canvas.create_image(0, 0, anchor=tkinter.NW, image=img)
    label1 = tkinter.Label(a,text="First Name",bg="teal",padx=30,pady=7)
    label2 = tkinter.Label(a,text="Last Name",bg="teal",padx=30,pady=7)
    label3 = tkinter.Label(a,text="Email",bg="teal",padx=30,pady=7)
    label4 = tkinter.Label(a,text="Phone",bg="teal",padx=30,pady=7)
    label5 = tkinter.Label(a,text="Address",bg="teal",padx=30,pady=7)
    label6 = tkinter.Label(a,text="LinkedIn Url",bg="teal",padx=30,pady=7)
    label7 = tkinter.Label(a,text="Master's Degree",bg="teal",padx=30,pady=7)
    label8 = tkinter.Label(a,text="College/University Name",bg="teal",padx=30,pady=7)
    label9 = tkinter.Label(a,text="Duration (20XX-20XX)",bg="teal",padx=30,pady=7)
    label10 = tkinter.Label(a,text="CGPA",bg="teal",padx=30,pady=7)
    label11 = tkinter.Label(a,text="Bachelor's Degree",bg="teal",padx=30,pady=7)
    label12 = tkinter.Label(a,text="College/University Name",bg="teal",padx=30,pady=7)
    label13 = tkinter.Label(a,text="Duration (20XX-20XX)",bg="teal",padx=30,pady=7)
    label14 = tkinter.Label(a,text="CGPA",bg="teal",padx=30,pady=7)
    label15 = tkinter.Label(a,text="Class 12th Percentile",bg="teal",padx=30,pady=7)
    label16 = tkinter.Label(a,text="Language 1",bg="teal",padx=30,pady=7)
    label17 = tkinter.Label(a,text="Language 2",bg="teal",padx=30,pady=7)
    label18 = tkinter.Label(a,text="Language 3",bg="teal",padx=30,pady=7)
    label19 = tkinter.Label(a,text="Technical Knowledge",bg="teal",padx=30,pady=7)
    label20 = tkinter.Label(a,text="Other Skills",bg="teal",padx=30,pady=7)
    label21 = tkinter.Label(a,text="Languages Speak",bg="teal",padx=30,pady=7)
    label22 = tkinter.Label(a,text="Job1/Internship",bg="teal",padx=30,pady=7)
    label23 = tkinter.Label(a,text="Job2/Internship",bg="teal",padx=30,pady=7)
    label24 = tkinter.Label(a,text="Job3/Internship",bg="teal",padx=30,pady=7)
    label25 = tkinter.Label(a,text="Project 1",bg="teal",padx=30,pady=7)
    label26 = tkinter.Label(a,text="Project 2",bg="teal",padx=30,pady=7)
    label27 = tkinter.Label(a,text="Project 3",bg="teal",padx=30,pady=7)
    label28 = tkinter.Label(a,text="Describe Yourself",bg="teal",padx=30,pady=7)
    entry1 = tkinter.Entry(a)
    entry2 = tkinter.Entry(a)
    entry3 = tkinter.Entry(a)
    entry4 = tkinter.Entry(a)
    entry5 = tkinter.Entry(a)
    entry6 = tkinter.Entry(a)
    entry7 = tkinter.Entry(a)
    entry8 = tkinter.Entry(a)
    entry9 = tkinter.Entry(a)
    entry10 = tkinter.Entry(a)
    entry11 = tkinter.Entry(a)
    entry12 = tkinter.Entry(a)
    entry13 = tkinter.Entry(a)
    entry14 = tkinter.Entry(a)
    entry15 = tkinter.Entry(a)
    entry16 = tkinter.Entry(a)
    entry17 = tkinter.Entry(a)
    entry18 = tkinter.Entry(a)
    entry19 = tkinter.Entry(a)
    entry20 = tkinter.Entry(a)
    entry21 = tkinter.Entry(a)
    entry22 = tkinter.Entry(a)
    entry23 = tkinter.Entry(a)
    entry24 = tkinter.Entry(a)
    entry25 = tkinter.Entry(a)
    entry26 = tkinter.Entry(a)
    entry27 = tkinter.Entry(a)
    entry28 = tkinter.Entry(a)
    button1 = tkinter.Button(a,text="Make The Resume",padx=30,pady=7,bg="orange",command=lambda : draw(1))
    button2 = tkinter.Button(a,text="Preview",command=lambda : draw(0),padx=30,pady=7,bg="lime")
    button3 = tkinter.Button(a,text="Reset",command=resetbutton,padx=30,pady=7,bg="grey")
    button4 = tkinter.Button(a,text="Exit",command=a.destroy,padx=20,pady=5,bg="red")
    str1 = "Important"
    str2 = "You dont need too add the whole URL.Just add after https://www.linked.com/in/"
    button5 = tkinter.Button(a,text="i",command=lambda : msg(str1,str2),padx=5,pady=2,bg="blue")
    label1.place(x=30,y=40)
    entry1.place(x=245,y=40,width=170,height=30)
    label2.place(x=30,y=110)
    entry2.place(x=245,y=110,width=170,height=30)
    label3.place(x=30,y=180)
    entry3.place(x=245,y=180,width=170,height=30)
    label4.place(x=30,y=250)
    entry4.place(x=245,y=250,width=170,height=30)
    label5.place(x=30,y=320)
    entry5.place(x=245,y=320,width=170,height=30)
    label6.place(x=30,y=390)
    entry6.place(x=245,y=390,width=170,height=30)
    label7.place(x=30,y=460)
    entry7.place(x=245,y=460,width=170,height=30)
    label8.place(x=30,y=530)
    entry8.place(x=245,y=530,width=170,height=30)
    label9.place(x=30,y=600)
    entry9.place(x=245,y=600,width=170,height=30)
    label10.place(x=30,y=670)
    entry10.place(x=245,y=670,width=170,height=30)
    label11.place(x=480,y=40)
    entry11.place(x=715,y=40,width=170,height=30)
    label12.place(x=480,y=110)
    entry12.place(x=715,y=110,width=170,height=30)
    label13.place(x=480,y=180)
    entry13.place(x=715,y=180,width=170,height=30)
    label14.place(x=480,y=250)
    entry14.place(x=715,y=250,width=170,height=30)
    label15.place(x=480,y=320)
    entry15.place(x=715,y=320,width=170,height=30)
    label16.place(x=480,y=390)
    entry16.place(x=715,y=390,width=170,height=30)
    label17.place(x=480,y=460)
    entry17.place(x=715,y=460,width=170,height=30)
    label18.place(x=480,y=530)
    entry18.place(x=715,y=530,width=170,height=30)
    label19.place(x=480,y=600)
    entry19.place(x=715,y=600,width=170,height=30)
    label20.place(x=480,y=670)
    entry20.place(x=715,y=670,width=170,height=30)
    label21.place(x=950,y=40)
    entry21.place(x=1150,y=40,width=170,height=30)
    label22.place(x=950,y=110)
    entry22.place(x=1150,y=110,width=170,height=30)
    label23.place(x=950,y=180)
    entry23.place(x=1150,y=180,width=170,height=30)
    label24.place(x=950,y=250)
    entry24.place(x=1150,y=250,width=170,height=30)
    label25.place(x=950,y=320)
    entry25.place(x=1150,y=320,width=170,height=30)
    label26.place(x=950,y=390)
    entry26.place(x=1150,y=390,width=170,height=30)
    label27.place(x=950,y=460)
    entry27.place(x=1150,y=460,width=170,height=30)
    label28.place(x=950,y=530)
    entry28.place(x=1150,y=530,width=170,height=30)
    button1.place(x=1050,y=600)
    button2.place(x=1250,y=600)
    button3.place(x=1050,y=670)
    button4.place(x=1250,y=670)
    button5.place(x=160,y=390)

    a.mainloop()
