## Installation
Install all required dependencies
```bash
pip install -r requirements.txt
```

create a file called credentials.conf
```bash
touch credentials.conf
```

add your gmail address and password into credentials.conf from where you want send out your mails in the following structure:
```conf
[email_credentails]
sender_email = <your gmail address>
password = <your gmail password>
```

## Local SMTP Server
For testing and debugging it's handy to run a local SMTP server. Python supports it natively and you can start a local SMTP server with the command
```bash
sudo python3 -m smtpd -c DebuggingServer -n localhost:1024
```
You can choose a port which is free but be aware if you change it here you also have to update the port number in local.py. Now you can run the script local.py
```bash
python local.py
```

## Sending Mails through GMail
In production you most likely use a common email provider like Gmail. So as a first step I recommend to create a new Gmail address. The reason is that you have to change some security settings on which shouldn't be active on your main email address.

Next you have to activate the option allow less secure apps to ON with the following link:
https://myaccount.google.com/lesssecureapps

If you don't want to lower the security settings, check out Google's documentation on how to gain access credentials for your Python script using OAuth2.

Add your Gmail credentials to the file credentials.conf as described in the installation section. For testing purposes GMail provides a nice feature where you can create different email addresses by adding +someText behind the @ symbol of your email address. Like myEmail@gmail.com and myEmail+personA@gmail.com. Both example mails will be sent into the same inbox.

Now you can run the gmail.py script.
```bash
python gmail.py
```