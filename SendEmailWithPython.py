import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import date
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.title('SEND MAIL WITH YOUR GMAIL')
root.geometry("800x500")

topFrame = Frame(root)
topFrame.pack(side = TOP)
title = Label(topFrame , text="SEND AN EMAIL FROM YOUR GMAIL")
title.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
title.pack()
root.configure(background='#243665')


def openSendNowWindow():
	def afterNextSendNow():
		def getFile():
			getFile.fileName = '0'
			getFile.fileName = filedialog.askopenfilename(initialdir = "/" , title = "Select A File" , filetype = (("jpeg" , "*.jpg") , ("All Files" , "*.*")) )	
		def sendTheMail():
			senderFinal = myMail.get()
			passwordFinal = password.get()
			recieverFinal = otherMail.get()
			subjectFinal = subject.get()
			bodyFinal = body.get("1.0",END)

			try:
				x = sendEmailNow(senderFinal , passwordFinal , recieverFinal , subjectFinal , bodyFinal , getFile.fileName)
			except:
				x = sendEmailNow(senderFinal , passwordFinal , recieverFinal , subjectFinal , bodyFinal , '0')	
			window.destroy()
			window2.destroy()
			title.pack_forget()
			sendNowButton.pack_forget()
			sendLaterButton.pack_forget()
			footer.pack_forget()
			if(x):
				MailSentLabel =  Label(topFrame , text="mail sent successfully")
				MailSentLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
				MailSentLabel.pack()
				thankYouLabel = Label(topFrame , text="thank you for using our program")
				thankYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
				thankYouLabel.pack()
				seeYouLabel = Label(topFrame , text="see you")
				seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
				seeYouLabel.pack()
			else:
				MailNotSentLabel =  Label(topFrame , text="mail not sent")
				MailNotSentLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
				MailNotSentLabel.pack()
				seeYouLabel = Label(topFrame , text="please check the entered data and try again")
				seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
				seeYouLabel.pack()
					
		window2 = Toplevel(root)
		window2.geometry("400x400")
		window2.title('SEND MAIL NOW')
		window2.config(background = '#243665')
		subjectLabel = Label(window2 , text = "Subject:")
		subjectLabel.config(foreground = '#8BD8BD' , background = '#243665')
		subjectLabel.pack()
		subject = Entry(window2 , width = 65)
		subject.pack()
		sendButton = Button(window2 ,  command = sendTheMail , text = 'send' , background = '#8BD8BD' , foreground='#243665' , width = 40)
		sendButton.pack(side = BOTTOM)
		body = Text(window2 , height = 18,width = 65)
		body.pack(side = BOTTOM)
		bodyLabel = Label(window2 , text = "Body:")
		bodyLabel.config(foreground = '#8BD8BD' , background = '#243665')
		bodyLabel.pack(side = BOTTOM)
		attachmentButton = Button(window2 , text = 'attach file' ,  background = '#8BD8BD' , foreground='#243665', width = 30 , command = getFile)
		attachmentButton.pack(side = BOTTOM)

	window = Toplevel(root)
	window.geometry("200x200")
	window.title('SEND MAIL NOW')
	window.config(background = '#243665')
	myMailLabel = Label(window , text = "From:")
	myMailLabel.config(foreground = '#8BD8BD' , background = '#243665')
	myMailLabel.pack()
	myMail = Entry(window , width = 35)
	myMail.pack()
	passwordLabel = Label(window , text = 'Password:')
	passwordLabel.config(foreground = '#8BD8BD' , background = '#243665')
	passwordLabel.pack()
	password = Entry(window , show="*" ,  width = 35)
	password.pack()
	otherMailLabel = Label(window , text = 'To:       ')
	otherMailLabel.config(foreground = '#8BD8BD' , background = '#243665')
	otherMailLabel.pack()
	otherMail = Entry(window ,  width = 35)
	otherMail.pack()
	nextButton = Button(window ,  command = afterNextSendNow , text = 'next' , background = '#8BD8BD' , foreground='#243665')
	nextButton.pack(side = BOTTOM)


def openSendLaterWindow():
	title.pack_forget()
	sendNowButton.pack_forget()
	sendLaterButton.pack_forget()
	footer.pack_forget()
	ll =  Label(topFrame , text="sending in progress...")
	ll.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
	ll.pack()
	lll = Label(topFrame , text="please do not close this window")
	lll.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
	lll.pack()
	l = Label(topFrame , text="until you get a message that mail is sent")
	l.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
	l.pack()
	def afterNextSendNow():
		def getFile():
			getFile.fileName = '0'
			getFile.fileName = filedialog.askopenfilename(initialdir = "/" , title = "Select A File" , filetype = (("jpeg" , "*.jpg") , ("All Files" , "*.*")) )	
		def afterAfterNextSendNow():
			def sendMailLater():
				senderFinal = myMail.get()
				passwordFinal = password.get()
				recieverFinal = otherMail.get()
				subjectFinal = subject.get()
				bodyFinal = body.get("1.0",END)
				dateFinal = date.get()
				timeFinal = time.get()
				window.destroy()
				window2.destroy()
				window3.destroy()
				try:
					x = sendEmailInTime(senderFinal , passwordFinal , recieverFinal , subjectFinal , bodyFinal , getFile.fileName , dateFinal , timeFinal)
				except:
					x = sendEmailInTime(senderFinal , passwordFinal , recieverFinal , subjectFinal , bodyFinal , '0' , dateFinal , timeFinal)
				if(x == 'dateFormat'):
					lll.pack_forget()
					ll.pack_forget()
					l.pack_forget()
					MailSentLabel =  Label(topFrame , text="you you have entered a wrong date format")
					MailSentLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					MailSentLabel.pack()
					thankYouLabel = Label(topFrame , text="email not sent")
					thankYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					thankYouLabel.pack()
					seeYouLabel = Label(topFrame , text="please try again")
					seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					seeYouLabel.pack()

				elif(x == 'timeFormat'):
					lll.pack_forget()
					ll.pack_forget()
					l.pack_forget()
					MailSentLabel =  Label(topFrame , text="you you have entered a wrong time format")
					MailSentLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					MailSentLabel.pack()
					thankYouLabel = Label(topFrame , text="email not sent")
					thankYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					thankYouLabel.pack()
					seeYouLabel = Label(topFrame , text="please try again")
					seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					seeYouLabel.pack()

				elif(x == 'past'):
					lll.pack_forget()
					ll.pack_forget()
					l.pack_forget()
					root.geometry("1000x300")
					MailNotSentLabel =  Label(topFrame , text="“You can't go back and change the beginning,but you")
					MailNotSentLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					MailNotSentLabel.pack()
					MailNotSentLabel =  Label(topFrame , text="can start where you are and change the ending.”")
					MailNotSentLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					MailNotSentLabel.pack()
					seeYouLabel = Label(topFrame , text="― C. S. Lewis")
					seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					seeYouLabel.pack()
					seeYouLabel = Label(topFrame , text="we are sorry we can not do anything the past time")
					seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					seeYouLabel.pack()
					seeYouLabel = Label(topFrame , text="please try again and enter a date and time in the future")
					seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					seeYouLabel.pack()


				elif(x == 'notSent'):
					lll.pack_forget()
					ll.pack_forget()
					l.pack_forget()
					MailNotSentLabel =  Label(topFrame , text="mail not sent")
					MailNotSentLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					MailNotSentLabel.pack()
					seeYouLabel = Label(topFrame , text="please check the entered data and try again")
					seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					seeYouLabel.pack()

				elif(x == 'sent'):
					lll.pack_forget()
					ll.pack_forget()
					l.pack_forget()
					MailSentLabel =  Label(topFrame , text="mail sent successfully")
					MailSentLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					MailSentLabel.pack()
					thankYouLabel = Label(topFrame , text="thank you for using our program")
					thankYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					thankYouLabel.pack()
					seeYouLabel = Label(topFrame , text="see you")
					seeYouLabel.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 30, 'bold'))
					seeYouLabel.pack()
									
			

			window3 = Toplevel(root)
			window3.geometry("400x150")
			window3.title('SEND MAIL NOW')
			window3.config(background = '#243665')
			dateLabel = Label(window3 , text = "Date at which the mail will be sent (DD/MM/YYYY)")
			dateLabel.config(foreground = '#8BD8BD' , background = '#243665')
			dateLabel.pack()
			date = Entry(window3 , width = 45)
			date.pack()
			timeLabel = Label(window3 , text = "Time at which the mail will be sent (HH:MM)")
			timeLabel.config(foreground = '#8BD8BD' , background = '#243665')
			timeLabel.pack()
			timeLabel2 = Label(window3 , text = "(e.g. 21:10)")
			timeLabel2.config(foreground = '#8BD8BD' , background = '#243665')
			timeLabel2.pack()

			time = Entry(window3 , width = 45)
			time.pack()
			sendButton = Button(window3 , text = 'send' ,  background = '#8BD8BD' , foreground='#243665', width = 30 , command = sendMailLater)
			sendButton.pack(side = BOTTOM)
			


		window2 = Toplevel(root)
		window2.geometry("400x400")
		window2.title('SEND MAIL NOW')
		window2.config(background = '#243665')
		subjectLabel = Label(window2 , text = "Subject:")
		subjectLabel.config(foreground = '#8BD8BD' , background = '#243665')
		subjectLabel.pack()
		subject = Entry(window2 , width = 65)
		subject.pack()
		next2Button = Button(window2 ,  command = afterAfterNextSendNow , text = 'next' , background = '#8BD8BD' , foreground='#243665' , width = 40)
		next2Button.pack(side = BOTTOM)
		body = Text(window2 , height = 18,width = 65)
		body.pack(side = BOTTOM)
		bodyLabel = Label(window2 , text = "Body:")
		bodyLabel.config(foreground = '#8BD8BD' , background = '#243665')
		bodyLabel.pack(side = BOTTOM)
		attachmentButton = Button(window2 , text = 'attach file' ,  background = '#8BD8BD' , foreground='#243665', width = 30 , command = getFile)
		attachmentButton.pack(side = BOTTOM)


	window = Toplevel(root)
	window.geometry("200x200")
	window.title('SEND MAIL NOW')
	window.config(background = '#243665')
	myMailLabel = Label(window , text = "From:")
	myMailLabel.config(foreground = '#8BD8BD' , background = '#243665')
	myMailLabel.pack()
	myMail = Entry(window , width = 35)
	myMail.pack()
	passwordLabel = Label(window , text = 'Password:')
	passwordLabel.config(foreground = '#8BD8BD' , background = '#243665')
	passwordLabel.pack()
	password = Entry(window , show="*" ,  width = 35)
	password.pack()
	otherMailLabel = Label(window , text = 'To:       ')
	otherMailLabel.config(foreground = '#8BD8BD' , background = '#243665')
	otherMailLabel.pack()
	otherMail = Entry(window ,  width = 35)
	otherMail.pack()
	nextButton = Button(window ,  command = afterNextSendNow , text = 'next' , background = '#8BD8BD' , foreground='#243665')
	nextButton.pack(side = BOTTOM)




sendNowButton = Button(topFrame, text = "send an Email now", command = openSendNowWindow ,foreground='#243665', background = '#8BD8BD' , height= '10' , width = '15' ,  font=('times', 20))
sendNowButton.pack(side = LEFT)
sendLaterButton = Button(topFrame , text = "send an Email Later" ,command = openSendLaterWindow,foreground = '#243665',background = '#8BD8BD', height= '10' , width = '15' ,  font=('times', 20))
sendLaterButton.pack(side = RIGHT)
topFrame.config(background = '#243665')


bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)
bottomFrame.config(background = '#243665')
footer = Label(bottomFrame , text="make sure that you turn the Button in that link: https://myaccount.google.com/lesssecureapps to ON to be able to use this program")
footer.config(foreground = '#8BD8BD' , background = '#243665' , font =  ('times', 10, 'bold'))
footer.pack()






def sendEmail(sender , password , reciever , subject1 , body1 , file):
	try:
		email_user = sender
		email_password = password
		email_send = reciever
		subject = subject1
		msg = MIMEMultipart()
		msg['From'] = email_user
		msg['To'] = email_send
		msg['Subject'] = subject
		body = body1
		msg.attach(MIMEText(body,'plain'))
		if(file != '0'):
			try:
				filename= file
				attachment  =open(filename,'rb')
				part = MIMEBase('application','octet-stream')
				part.set_payload((attachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(filename))
				msg.attach(part)
			except:
				print('invalid directory when you do not want to attach a file enter "0" when you are asked to enter a directory')	

		text = msg.as_string()
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(email_user,email_password)
		server.sendmail(email_user,email_send,text)
		server.quit()
		print('mail sent')
		return True
	except:
		print('mail not sent')
		print('wrong mail or password')
		print('please check your entered data and try again')
		return False


def sendEmailInTime(sender1 , password1 , reciever1 , subject1 , body1 , file1 , date1 , time1):
	print("enter your email address")
	sender = sender1
	print('enter your password')
	password = password1
	print('enter the email address that you want to send an email to')
	reciever = reciever1
	print('enter the subject of the email')
	subject = subject1
	print('enter the body of the email')
	body = body1
	print('enter the directory of the file you wanna attach. In case you do not want to attach file enter 0')
	fileDic = file1
	print("enter the date you want to send the email at in that form DD/MM/YYYY")
	dateToSend = date1
	print("enter the time you want to send the email at in that form HH:MM and in the 24 hours system not am and pm system")
	timeToSend = time1
	today = date.today()
	heute = today.strftime("%d/%m/%Y")
	t = time.localtime()
	currentTime = time.strftime("%H:%M", t)
	if(checkCorrectDateForm(dateToSend) == False):
		print("you have entered a wrong date form")
		print("email not sent")
		print("please try again")
		return 'dateFormat'
	if(checkTimeFormat(timeToSend) == False):
		print("you have entered a wrong time form")
		print("email not sent")
		print("please try again")
		return 'timeFormat'
	if(isTheGivenTimeInTheFuture(heute , dateToSend , currentTime , timeToSend) == False):
		print("“Yesterday is gone. Tomorrow has not yet come. We have only today. Let us begin.”")	
		print("― Mother Theresa")
		print("we are sorry we can not do anything the past time")
		print("email not sent")
		print("please try again and enter a date and time in the future")
		return 'past'
	while True:
			today = date.today()
			heute = today.strftime("%d/%m/%Y")
			if(heute == dateToSend):
				break
			else:
				time.sleep(86300)		
	while True:
			t = time.localtime()
			currentTime = time.strftime("%H:%M", t)
			if(timeToSend == currentTime):
				if sendEmail(sender , password , reciever , subject , body , fileDic) == False:
					return 'notSent'	
				else:
					return 'sent'
			else:
				time.sleep(55)
								


def sendEmailNow(sender1 , password1 , reciever1 , subject1 , body1 , file1):
	sender = sender1
	password = password1
	reciever = reciever1
	subject = subject1
	body = body1
	fileDic = file1
	return sendEmail(sender , password , reciever , subject , body , fileDic)


	

def checkCorrectDateForm(date):
	if(len(date) != 10):
		return False
	if(not (date[0] == '0' or date[0] == '1' or date[0] == '2' or date[0] == '3')):
		return False
	secondDigitInDate = int(date[1])
	if(not (secondDigitInDate <= 9 and secondDigitInDate >=0)):
		return False
	if(not (date[2] == "/" and date[5] == "/" )):
		return False
	month = int(date[3:5])
	if(month <= 0 or month > 12):
		return False
	year = int(date[6:])
	if(year < 1000):
		return False
	return True	

def isTheGivenTimeInTheFuture(today , date, now ,time):
	heute = str(today)
	if(heute == date):
		return checkTime(now , time)
	year = int(date[6:])
	currentYear = int(heute[6:])
	if(currentYear > year):
		return False
	if(currentYear < year):
		return True	
	month = int(date[3:5])
	currentMonth = int(heute[3:5])
	if(currentMonth < month):
		return True
	if(currentMonth > month):
		return False
	day = int(today[0:2])
	currentDay = int(heute[0:2])
	if(currentDay < day):
		return True
	if(currentDay > day):
		return  False
	return checkTime(now , time)



def checkTimeFormat(time):
	if(len(time) != 5):
		return False
	if(int(time[0:2]) >= 24 or int(time[0:2]) < 0):
		return False
	if(int(time[3:]) >= 60 or int(time[3:]) < 0):
		return False
	if(time[2] != ':'):
		return False
	return True				

def checkTime(now  , time):
	hour = int(time[0:2])
	currentHour = int(now[0:2])
	if(hour > currentHour):
		return True
	if(hour < currentHour):
		return False
	minute = int(time[3:])
	currentMinute = int(now[3:])
	if(currentMinute < minute):
		return True
	return False		
				
		
			


root.mainloop()