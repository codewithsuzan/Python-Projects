import smtplib
import os

# Set up your email server
try:
    # Establish connection
    ob = smtplib.SMTP('smtp.gmail.com', 587)
    ob.ehlo()  # Identify ourselves with the server
    ob.starttls()  # Secure the connection with TLS

    # Login using an environment variable for the password
    email_address = 'your_email_address'
    email_password = 'password' 
    
    # Email content
    subject = "Test Mailing"
    body = "This is a test email."
    msg = f"Subject: {subject}\n\n{body}"
    list_addresses = ['user1@gmail.com', 'user2@gmail.com', 'user3@gmail.com']

    # Send the email
    ob.sendmail(email_address, list_addresses, msg)
    print('Email sent successfully!')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the connection
    ob.quit()
    

#Steps to Fix the Issue

    """Enable Two-Factor Authentication (2FA) on Your Google Account
        Log in to your Google account.
        Go to Security settings.
        Enable 2-Step Verification by following the instructions.

    Generate an App Password
        After enabling 2FA:
            Navigate to Security > App Passwords in your Google account.
            Select the app type (e.g., "Mail") and device type (e.g., "Windows Computer").
            Generate the password. Google will provide a 16-character password (e.g., abcd efgh ijkl mnop).
            Copy the password.

    Replace Your Password with App password
    """