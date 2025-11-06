import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase # NEW: Import MIMEBase for attachments
from email import encoders # NEW: Import encoders for Base64 encoding
import os # NEW: Import os for path manipulation

from config import app_password, from_address

def send_gmail(to_address, subject, body, attachment_paths=None): # UPDATED: Added attachment_paths parameter
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # NEW: Logic to add attachments
        if attachment_paths:
            for attachment_path in attachment_paths:
                try:
                    with open(attachment_path, "rb") as attachment:
                        # Create a MIMEBase object for the attachment
                        # "application/octet-stream" is a generic type for binary data
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())
                    
                    # Encode the attachment with Base64
                    encoders.encode_base64(part)
                    
                    # Add header as key/value pair to attachment part
                    # os.path.basename extracts just the filename from the full path
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {os.path.basename(attachment_path)}",
                    )
                    
                    # Add attachment to message
                    msg.attach(part)
                except FileNotFoundError:
                    print(f"Warning: Attachment file not found at {attachment_path}. Skipping this attachment.")
                except Exception as e:
                    print(f"Warning: Could not attach {attachment_path} due to error: {e}. Skipping this attachment.")

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_address, app_password)
        server.send_message(msg) # Use send_message for MIMEMultipart objects
        server.quit()
        return True
    except Exception as e:
        print("Error sending email:", e) # Clarified error message
        return False