import smtplib
import ConfigParser
import datetime
from email.mime.text import MIMEText

##--Beginning of Loading result.html##
# get folder name by timestamp MMddYY
folder_name = datetime.datetime.now().strftime("%Y%m%d")

cf = ConfigParser.ConfigParser()
cf.read("config.conf")
HTMLOUTPUT = cf.get("source_dir","LOGDIR")+folder_name+"/result.html"

# load html report
fp=open(HTMLOUTPUT, 'rb')
msg=MIMEText(fp.read(), 'html','utf-8');
fp.close()

##--Ending of Loading result.html##

# sendemail
file_dir="C:/Users/chuyu"
cfe=ConfigParser.ConfigParser()
file_ename=file_dir+"/test.txt"
cfe.read(file_ename)
uownum=cfe.get("UOW","UOW")
msg['Subject'] = 'UOW'+uownum+' '+'Impacted Automation Test Result'
msg['From'] =cf.get("mail_server","From")
mails= cfe.get("send_email","email")
emails=[]
emails.append(mails.split(','))
emails=tuple(emails)

msg['To'][0], msg.as_string())
s.quit()
