import smtplib
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from textwrap import indent

#The $list_of_target.txt should be file for your targets list
with open("list_of_targets.txt") as file:

    #Here, we're reading our file line by line and specifying each of our targets.
    targets = file.readlines()
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        #The $sender_email_address is the hacker's email address and $password is the password for hackers email.
        #We must log into our email address so we can send emails to our targets!
        smtp.login("sender_email_address", "password")
        for index, each_target in enumerate(targets):
            #The next line will split our target's information, so we can modify our email better (It's optional)
            list_of_targets_information = list(each_target.split(","))

            #The $phishing_html.html is the html file that contains the context of our phishing email.
            #You can specefy it as you want!
            html = Template(Path("phishing_html.html").read_text())
            email = EmailMessage()
            #The $email["from"] will contain the From section of our email.
            email["from"] = "Hacker"
            #The $email["to"] has been set to each of our targets.
            email["to"] = list_of_targets_information[0]
            #The $email["subject"] is obvious! It's the subject of our email.
            email["subject"] = "phishing email"

            #The $target_email and $name should be the same as our variables in $phishing_html.html file.
            email.set_content(html.substitute({"target_email": list_of_targets_information[0],
            "name": list_of_targets_information[1].strip()}),
            "html")

            smtp.send_message(email)
            print(f"Target {list_of_targets_information[1].strip()} is DONE !!!")
