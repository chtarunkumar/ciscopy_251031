import os # Import the os module

dir_path = r'C:\Users\ctarunku\OneDrive - Cisco\Desktop'
attachments = [
    os.path.join(dir_path, 'dhoni.jpg'),
    os.path.join(dir_path, 'jadeja.webp'),
]

# Corrected import statement:
from mail import send_gmail # <--- CHANGE THIS LINE

from config import to_address

# And then call the function with its correct name:
result = send_gmail(to_address, "Maheswaran - Test Subject from pystud19 - 06-11-2025 - Photos", "Hello from Python!", attachments) # <--- CHANGE THIS LINE
print("Mail sent successfully?", result)