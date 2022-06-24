# Email Spammer which spoofs emails and spams email using smtp
# Made By Coding With Uday
# Website - http://codeuday.cf/
# YouTube - https://youtube.com/c/codingwithuday
# Discord - </>IsntTaken#0999

# Importing required dependencies
import random
import smtplib
from email.mime.text import MIMEText

# Specifying sender and receivers
sender = 'example@example.com'
receivers = ['receiver@example.com', "receiver2@example.com"]

# Specifying smtp port
port = 587

# Specifying Smtp Address and Connecting to the server
with smtplib.SMTP('smtp-relay.sendinblue.com', port) as server:
    for i in range(10):  # You can change the value inside the range to the number of emails you wanna send
        randnum = random.randint(0, 999)  # Generating random number
        msg = MIMEText(f'this is the body of the email')  # Body of the email
        msg['Subject'] = 'Subject of the email'  # Subject Of the email
        # From of email again but i'm adding random number between so that in the inbox it stacks causing to flood the inbox
        msg['From'] = f'from{randnum}@example.com'
        msg['To'] = 'to@example.com' # To email again
        server.login('smtp-username', 'smtp-password') # SMTP Credentials
        server.sendmail(sender, receivers, msg.as_string()) # Composing the email
        print("Successfully sent email", i+1) # Printing Success Msg
