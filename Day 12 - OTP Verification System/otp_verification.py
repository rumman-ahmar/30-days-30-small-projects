import random
import smtplib


def send_otp_via_mail(otp):

    """
    Funtion to send OTP via email
    param otp: OTP to send on mail
    """

    # receiver email
    receiver_mail = input("Enter receiver email: ")

    # creates SMTP session
    smtp = smtplib.SMTP("smtp.gmail.com", 587)

    # start TLS
    smtp.starttls()

    # login to your account
    smtp.login("sender_email_id", "sender_email_id_password")

    # message to be sent
    message = f"Your OTP is {otp}"

    # send the mail
    smtp.sendmail("sender_email_id", receiver_mail, message)

    # terminate the session
    smtp.quit()

    # enter otp
    user_otp = input("Enter your OTP: ")
    return user_otp


def generate_n_verify_otp():

    """
    Function to generate and verify the OTP that has sent on user mail
    """

    # generate OTP
    otp = "".join(map(str, random.sample(range(0, 9), 6)))
    print(f"Generated OTP is: {otp}")

    # send OTP on user mail and get the user input
    user_otp = send_otp_via_mail(otp)
    print(f"OTP entered by the user is: {user_otp}")

    # check if the user has input the correct OTP
    if user_otp == otp:
        print("OTP Verified")
    else:
        print("OTP is not verified")

    return True


if __name__ == "__main__":
    generate_n_verify_otp()
