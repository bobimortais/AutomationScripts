import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from datetime import datetime
import time

while True:
	server = smtplib.SMTP('smtp.live.com', 587)
	server.starttls()
	server.login('testtest@hotmail.com', 'xxxxxxxxxxxxx')
	msg = MIMEMultipart('alternative')
	text = 'Trouble Tickets Report'
	html = '<html><head></head><body><table><tr><th>Case ID</th><th>Description</th><th>Status</th></tr><tr><td>1</td><td>Broken Nose</td><td>Open</td></tr><tr><td>2</td><td>Car Crash</td><td>Closed</td></tr></table></body></html>'
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')
	msg.attach(part1)
	msg.attach(part2)
	msg['Subject'] = 'Trouble Tickets Report ' + datetime.now().strftime('%c')
	msg['From'] = 'testtest@hotmail.com'
	msg['To'] = 'testtest@hotmail.com'
	server.send_message(msg)
	server.quit()
  	time.sleep(1800)
