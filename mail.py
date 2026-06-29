import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_automated_email():

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    
    sender_email = "abc@gmail.com" 
    sender_password = "password@123" 
    receiver_email = "abc@gmail.com"
    
   
    subject = ""# write your subject here
    
    
    body = """ """# write you body here

    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject


    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    
    try:
        print("Connecting to the server...")

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
        
        print("Logging in...")
        server.login(sender_email, sender_password)
        
        print("Sending email...")
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        
    finally:
        
        server.quit()


if __name__ == "__main__":
    send_automated_email()
