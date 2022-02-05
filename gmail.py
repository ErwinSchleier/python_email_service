import smtplib, ssl
import configparser

port = 587  # For starttls
smtp_server = "smtp.gmail.com"

parser = configparser.ConfigParser()
parser.read("credentials.conf")
sender_email = parser.get("email_credentails", "sender_email")
password = parser.get("email_credentails", "password")
receiver_email = parser.get("email_credentails", "receiver_email")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
