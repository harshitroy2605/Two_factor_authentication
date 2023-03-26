import socket
import time
import PIL
import threading
from tkinter import *
from email.message import EmailMessage
import smtplib
import random
import sqlite3


#------------------------------chat application ----------------------------------------------


def func(user_name):
	root=Tk()
	root.geometry("300x500")
	root.config(bg="white")
	print(user_name)
	def func():
		t=threading.Thread(target=recv)
		t.start()

	def recv():
		listensocket=socket.socket()
		port=3050
		maxconnection=99
		ip=socket.gethostname()
		print(ip)

		listensocket.bind(('',port))
		listensocket.listen(maxconnection)
		(clientsocket,address)=listensocket.accept()

		while True:
			sendermessage=clientsocket.recv(1024).decode()
			if not sendermessage=="":
				time.sleep(5)
				lstbx.insert(0,"Client : "+sendermessage)


	s=0

	def sendmsg():
		global s
		if s==0:
			s=socket.socket()
			hostname='DESKTOP-7C41EV3'
			port=4050
			s.connect((hostname,port))
			msg=messagebox.get()
			lstbx.insert(0,"You : "+msg)
			s.send(msg.encode())
		else:
			msg=messagebox.get()
			lstbx.insert(0,"You : "+msg)
			s.send(msg.encode())


	def threadsendmsg():
		th=threading.Thread(target=sendmsg)
		th.start()




	startchatimage=PhotoImage(file='start.png')

	buttons=Button(root,image=startchatimage,command=func,borderwidth=0)
	buttons.place(x=90,y=10)

	message=StringVar()
	messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
	messagebox.place(x=10,y=444)

	sendmessageimg=PhotoImage(file='send.png')

	sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
	sendmessagebutton.place(x=260,y=440)

	lstbx=Listbox(root,height=20,width=43)
	lstbx.place(x=15,y=80)

	user_name = Label(root,text =" Number" ,width=10)

	root.mainloop()


#--------------------------chat application ends ------------------------------------------











def email_verification(user_name):

#------------------send email --------------------------------------

	from email.message import EmailMessage
	import smtplib
	import random

	otp=str(random.randint(1000,9999))

	sender = ""
	recipient = ""
	message = otp

	email = EmailMessage()
	email["From"] = sender
	email["To"] = recipient
	email["Subject"] = "OTP"
	email.set_content(message)

	smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
	smtp.starttls()
	smtp.login(sender, "")
	smtp.sendmail(sender, recipient, email.as_string())
	smtp.quit()

#--------------send email complete--------------------------------#




#--------------otp verification gui---------------------------------
	root1=Tk()
	root1.geometry("300x500")
	root1.config(bg="white")
	
	otp_var=StringVar()
	otp_entry=Entry(root1,textvariable=otp_var,font=('calibre',10,'normal'),border=2,width=32)
	otp_entry.place(x=10,y=444)

	verify_button=Button(root1,text="verify",command=lambda: verifyotp(otp,otp_entry,user_name,root1),borderwidth=0)
	verify_button.place(x=260,y=440)


	root1.mainloop()






def verifyotp(otp,otp_entry,user_name,root1):
	otp = str(otp)
	otp_entry=str(otp_entry.get())
	print(otp)
	print(otp_entry)
	print(type(otp_entry))
	print(type(otp))
	if otp_entry == otp:
		root1.destroy()
		func(user_name)
	else:
		print("incorrect otp")












# ---------------otp verification gui ends --------------------------









## ------------------------------------  login page start level 1 ----------------------------------------------#


class Login_Form(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("700x600")
		self.resizable(False, False)

	def Labels(self):
		self.Background_Image=PhotoImage(file='background_img.png')

		self.Background_Image_Label=Label(self,image=self.Background_Image)   #Background image
		self.Background_Image_Label.place(x=0,y=0,relwidth=1,relheight=1)
		
		self.canvas=Canvas(self, width=400, height=450)                       #backgrounf canvas
		self.canvas.place(x=150,y=60)
		
		self.Login_Title=Label(self,text="Login",font="bold, 30")             #login Title on Top
		self.Login_Title.place(x=300,y=90)
		
		self.User_Name_Label=Label(self,text="Email",font="8")                 #User Name Label
		self.User_Name_Label.place(x=200,y=150)

		self.Password_label=Label(self,text="Password",font="8")               #Password Label
		self.Password_label.place(x=200,y=250)


	def Entry(self):

		self.User_Name_var=StringVar()
		self.User_Name=Entry(self,textvariable=self.User_Name_var,font=('calibre',10,'normal'),border=2,width=32)
		self.User_Name.place(x=200,y=185)

		
		self.password_var=StringVar()
		self.Password=Entry(self,textvariable=self.password_var,font=('calibre',10,'normal'),show='*',border=2,width=32)
		self.Password.place(x=200,y=285)



	def Buttons(self):
		self.Facebook_Button_Image=PhotoImage(file="facebook.png")
		self.Facebook_Button=Button(self,image=self.Facebook_Button_Image,command=self.Facebook_Function,border=0)
		self.Facebook_Button.place(x=278,y=440)


		self.Instagram_Button_Image=PhotoImage(file="instagram.png")
		self.Instagram_Button=Button(self,image=self.Instagram_Button_Image,command=self.Instagram_Function,border=0)
		self.Instagram_Button.place(x=328,y=440)


		self.Twitter_Button_Image=PhotoImage(file="twitter.png")
		self.Twitter_Button=Button(self,image=self.Twitter_Button_Image,command=self.Twitter_Function,border=0)
		self.Twitter_Button.place(x=380,y=440)


		self.Button_Image=PhotoImage(file="button.png")
		self.Button=Button(self,image=self.Button_Image,command=self.Execute_Function,border=0)
		self.Button.place(x=268,y=350)

	def Facebook_Function(self):
		print("facebook link inserted here")


	def Instagram_Function(self):
		print("instagram link inserted here")

	def Twitter_Function(self):
		print("twitter link inserted here")

	def Execute_Function(self):
		#print("working")
		#print(self.User_Name.get())
		conn=sqlite3.connect("users.db")
		cur=conn.cursor()
		cur.execute("SELECT * FROM Users WHERE email=? AND password=?",(self.User_Name.get(),self.Password.get()))
		row=cur.fetchall()
		conn.close()
		#print(row)
		if row!=[]:
			user_name=row[0][1]
			#print(user_name)
			self.destroy()
			email_verification(user_name)

		else:
			print("user not found ")



if __name__=="__main__":
	window=Login_Form()
	window.Labels()
	window.Entry()
	window.Buttons()
	window.mainloop()

#--------------------------login ends here -----------------------------
