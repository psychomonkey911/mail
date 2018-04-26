#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
import getpass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import mimetypes

import email.mime.application

msg = MIMEMultipart()

# mail + password
gmail_user = 'you@gmail.com'
gmail_pwd = 'pasw'

# collect emails from emails.txt  # TO = list of emails
error = True
while error == True:
	try:
		emails_path = '\mails.txt'
		with open (emails_path, "r") as emails_file:
			emails = emails_file.read()
			TO = emails.split("\n")
			error = False
	except:
		print("invalid path")

# msg subject
msg = MIMEMultipart('mixed')
msg['Subject'] = 'Заголовок письма'
# msg sender
msg['From'] = gmail_user
# msg body
content = 'тело письма'
TEXT = content
body = MIMEText(TEXT)
msg.attach(body)

# msg attachment
error = True
while error == True:
	try:
		filename = '\kp.jpg'
		fp=open(filename,'rb')
		att = email.mime.application.MIMEApplication(fp.read(),_subtype="jpg")
		fp.close()
		att.add_header('Content-Disposition','attachment',filename='kp.jpg')
		msg.attach(att)
		error = False
	except:
		print('invalid path')
#begin
try:
	#connect to server
	server = smtplib.SMTP("smtp.gmail.com", 25)
	server.ehlo()
	server.starttls()
	#connect gmail account
	try:
		server.login(gmail_user, gmail_pwd)
		print("Login succesfully")
	except:
		print("Failed to login, verify your email and password")
	#send separatly emails
	for email in TO:
		msg['To'] = email
		print ("sending to : " + email)
		try:
			#send email
			server.sendmail(email,[email], msg.as_string())
			print ('successfully sent the mail to : ' + email)
			del msg['To']
		except:
			#error
			print ('failed sending the mail to : ' + email)
			del msg['To']
	#close server
	server.close()
except:
	print ("Error")