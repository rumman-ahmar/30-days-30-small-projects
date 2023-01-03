import smtplib

# creates SMTP session
smtp = smtplib.SMTP("smtp.gmail.com", 587)

# start TLS
smtp.starttls()

# login to your account
smtp.login("sender_email_id", "sender_email_id_password")

# message to be sent
message = "Message_you_need_to_send"

# send the mail
smtp.sendmail("sender_email_id", "receiver_email_id", message)

# terminate the session
smtp.quit()
