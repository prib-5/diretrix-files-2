import os
import yagmail

receiver="reviever@gmail.com"
body="Attendace File"
filename="Attendance"+os.sep+"Attendance_2019-08-29_13-09-07.csv"

yag=yagmail.SMTP("your_gamail@gmail.com","your_password")

yag.send(
	to=receiver
	subject="Attendance Report"
	contents=body
	attachments=filename
	)