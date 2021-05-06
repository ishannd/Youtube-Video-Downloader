from tkinter import *
from tkinter import messagebox

parent = Tk()

parent.title("Youtube Video Downloader")

parent.geometry("400x250")

video_url_temp = StringVar()

video_res_temp = IntVar()

def exitFunction():
    messagebox.showinfo("Hello","Video downloaded")
    parent.quit()
    

url_field = Label(parent,text="Video url").grid(row = 0 , column = 0)
url_entry = Entry(parent,textvariable=video_url_temp).grid(row=0,column=1)
res_field = Label(parent,text="Video Resolution").grid(row=1,column=0)
res_1 = Radiobutton(parent,text="240p",variable=video_res_temp,value=1).grid(row=2,column=1)
res_2 = Radiobutton(parent,text="360p",variable=video_res_temp,value=2).grid(row=3,column=1)
res_3 = Radiobutton(parent,text="480p",variable=video_res_temp,value=3).grid(row=4,column=1)
res_4 = Radiobutton(parent,text="720p",variable=video_res_temp,value=4).grid(row=5,column=1)

submitButton = Button(parent,text="Submit",command=exitFunction)
submitButton.place(x=150,y=170)

submitButton = Button(parent,text="Submit",command=exitFunction)
parent.mainloop()

if(video_res_temp.get()==1):
    video_res_temp = "240p"
elif(video_res_temp.get()==2):
    video_res_temp = "360p"
elif(video_res_temp.get()==3):
    video_res_temp = "480p"
else:
    video_res_temp="720p"

video_res = video_res_temp
video_url = video_url_temp.get()





