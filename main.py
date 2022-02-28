# import required modules
import tkinter
from tkinter import *

import pandas as pd
import matplotlib.pyplot as plt

credentialOK=False
cancelFlag=False

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("600x250")

def testcredentials(user,password):
  if(user=="shino"):
    return True;
  else:
    return False;

def clear_cb():
  user.delete(0,END)
  password.delete(0,END)

def submit_cb():
  global messagebox
  print('user=',user.get())
  print('password=',password.get())
  if(testcredentials(user.get(),password.get())):
    win.destroy()
  else:
    messagebox.config(text='Login failed with user/password combination',fg='Red')

def cancel_cb():
  global exitflag 
  print('canceling and exiting')
  exitflag=True

  win.destroy()
  
def close_win():
  win.destroy()

def changed_cb(var, index, mode):
  global messagebox
  messagebox.config(text='',fg='Black')

  
rowpos=0
rowposinc=25
pady=10

#Create a text label
Label(win,text="DB Login", font=('Helvetica',20)).grid(row=rowpos,column=0,columnspan=2)

rowpos+=rowposinc
user_var=StringVar()
user_var.trace_add("write", changed_cb)
Label(win,text="Username").grid(row=rowpos,column=0,pady=pady)
user= Entry(win,textvariable=user_var)
user.grid(row=rowpos,column=1,pady=pady,columnspan=2)

rowpos+=rowposinc
password_var=StringVar()
password_var.trace_add("write", changed_cb)

Label(win,text="Password").grid(row=rowpos,column=0,pady=pady)
password= Entry(win,show="*",textvariable=password_var)
password.grid(row=rowpos,column=1,pady=pady,columnspan=2)

rowpos+=rowposinc

#Create a button to close the window
Button(win, text="Submit", font=('Helvetica bold',
10),command=submit_cb).grid(row=rowpos,column=0,pady=pady)
Button(win, text="Clear", font=('Helvetica bold',
10),command=clear_cb).grid(row=rowpos,column=1,pady=pady)
Button(win, text="Cancel", font=('Helvetica bold',
10),command=cancel_cb).grid(row=rowpos,column=2,pady=pady)



rowpos+=rowposinc
messagebox=Label(win,text="")
messagebox.grid(row=rowpos,column=0,columnspan=3)

win.mainloop()

if(cancelFlag!=True):
  
    
  # create 2D array of student details
  stdData = [['S1', 'M', 13, 123, 46],
          ['S2', 'M', 12, 134, 82],
          ['S3', 'F', 14, 114, 77],
          ['S4', 'M', 13, 136, 73],
          ['S5', 'F', 13, 107, 56],
          ['S6', 'F', 12, 121, 80],
          ['S7', 'M', 14, 113, 76],
          ['S8', 'F', 15, 123, 95],
          ['S9', 'F', 14, 112, 78],
          ['S10', 'M', 15, 100,60] ]
  # creating the dataframe from the above data 
  df = pd.DataFrame(stdData, columns = ['ID', 'Gender','Age', 'Height(cm)','Marks'] )
  df.hist()# create histogram for the numeric data(Age, Height,Marks)
  plt.show() #displaying the plot
