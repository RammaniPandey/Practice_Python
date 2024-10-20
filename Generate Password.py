##import random

#passlen = int(input("Enter the length of password : "))

#S = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_*?{}"

    #P = "".join(random.sample(S,passlen))
#print(P)
import tkinter as tk
from tkinter import messagebox
import pyotp
import qrcode
from PIL import Image, ImageTk

class MFAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MFA Authentication Tool")

        # Generate and display TOTP secret and QR code
        self.secret = pyotp.random_base32()
        self.create_qr_code(self.secret)

        # GUI for Password and TOTP Entry
        self.create_widgets()

    def create_qr_code(self, secret):
        # Generate QR code
        uri = pyotp.totp.TOTP(secret).provisioning_uri(
            name="your_email@example.com", issuer_name="YourAppName"
        )
        qr = qrcode.make(uri)
        qr.save("qrcode.png")

        # Display QR code in GUI
        qr_img = Image.open("qrcode.png")
        qr_img = qr_img.resize((200, 200), Image.ANTIALIAS)
        self.qr_photo = ImageTk.PhotoImage(qr_img)

        qr_label = tk.Label(self.root, image=self.qr_photo)
        qr_label.pack()

    def create_widgets(self):
        # Password entry
        tk.Label(self.root, text="Enter Password:").pack(pady=10)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10)

        # TOTP entry
        tk.Label(self.root, text="Enter TOTP Code:").pack(pady=10)
        self.totp_entry = tk.Entry(self.root)
        self.totp_entry.pack(pady=10)

        # Authenticate button
        auth_button = tk.Button(self.root, text="Authenticate", command=self.authenticate)
        auth_button.pack(pady=20)

    def authenticate(self):
        # Example stored password
        stored_password = "password123"

        # Check password
        if self.password_entry.get() == stored_password:
            # Verify TOTP
            totp = pyotp.TOTP(self.secret)
            if totp.verify(self.totp_entry.get()):
                messagebox.showinfo("Success", "Authentication successful!")
            else:
                messagebox.showerror("Error", "Invalid TOTP code!")
        else:
            messagebox.showerror("Error", "Invalid password!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MFAApp(root)
    root.mainloop()
