MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# Function to send an email to yourself to alert you that the ISS is above you in the sky
def send_to_email():
    # Connect to your email provider's SMTP server
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        # Start the Transport Layer Security (TLS) security protocol
        connection.starttls()
        # Login to your email account with your email address and password
        connection.login(email=MY_EMAIL, password=MY_PASSWORD)
        # Send the email to yourself
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:LOOK UP!!!\n\nTHE ISS IS ABOVE YOU IN THE SKY!!!")

