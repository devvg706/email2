import smtplib  # Library for sending emails via SMTP
from email.mime.text import MIMEText  # Library for formatting email content as plain text
from email.mime.multipart import MIMEMultipart  # Library for constructing multi-part emails
import os
# Define the function to send an email
def send_failure_email(repository_name, workflow_name, workflow_run_id,):
   
    # Sender email credentials (customize for your SMTP server)
    sender_email = os.getenv("sender_email") # Your email address
    sender_password = os.getenv("reciever_email")  # Your email password (use secure storage for real applications)
    reciever_email = os.getenv("reciever_email")
    # Construct the email content
    subject = f"Workflow Failure: {workflow_name}"  # Email subject
    body = f"""
    Dear User,

    The following workflow has failed:

    - Repository Name: {repository_name}
    - Workflow Name: {workflow_name}
    - Workflow Run ID: {workflow_run_id}

    Please check the details and take necessary actions.

    Best regards,
    Automated Notification System
    """

    # Create a MIME message object for the email
    message = MIMEMultipart()  # Multi-part email to support attachments if needed
    message["From"] = sender_email  # Specify the sender
    message["To"] = reciever_email  # Specify the recipient
    message["Subject"] = subject  # Specify the subject
    message.attach(MIMEText(body, "plain"))  # Attach the email body as plain text

    try:
        # Establish connection to the SMTP server
        server = smtplib.SMTP('smpt.gmail.com', 587)  # Connect to the SMTP server
        server.starttls()  # Upgrade the connection to a secure encrypted TLS/SSL connection
        server.login(sender_email, sender_password)  # Log in to the SMTP server

        # Send the email
        server.sendmail(sender_email, reciever_email, message.as_string())  # Send the email as a string

        print("Failure email sent successfully!")  # Log success
    except Exception as e:
        print(f"Error sending email: {e}")  # Log any errors encountered
    finally:
        server.quit()  # Close the connection to the SMTP server



send_failure_email(os.getenv('workflow_name'), os.getenv('rep_name'), os.getenv('workflow_run_id'))
