import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#from PIL import Image, ImageTk

def book_ticket():
    name = entry_name.get()
    source = entry_source.get()
    destination = entry_destination.get()
    date = entry_date.get()
    train_class = class_var.get()
    seats = entry_seats.get()
    
    if not name or not source or not destination or not date or not train_class or not seats:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    ticket_details = f"""
    Train Ticket Booked Successfully!
    -----------------------------------
    Name: {name}
    From: {source}
    To: {destination}
    Date: {date}
    Class: {train_class}
    Seats: {seats}
    """
    messagebox.showinfo("Ticket Confirmation", ticket_details)

# Creating main application window
root = tk.Tk()
root.title("Train Ticket Booking")
root.geometry("500x600")
root.configure(bg="#F0E68C")  # Light yellow background

# Load and display logo
try:
    logo_img = Image.open("train_logo.png")  # Ensure you have an image named train_logo.png
    logo_img = logo_img.resize((120, 120))
    logo_photo = ImageTk.PhotoImage(logo_img)
    tk.Label(root, image=logo_photo, bg="#F0E68C").pack(pady=5)
except:
    pass  # If image not found, skip logo

# Labels and Entry fields
tk.Label(root, text="Name:", font=("Arial", 12, "bold"), bg="#F0E68C").pack(pady=5)
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)

tk.Label(root, text="From:", font=("Arial", 12, "bold"), bg="#F0E68C").pack(pady=5)
entry_source = tk.Entry(root, font=("Arial", 12))
entry_source.pack(pady=5)

tk.Label(root, text="To:", font=("Arial", 12, "bold"), bg="#F0E68C").pack(pady=5)
entry_destination = tk.Entry(root, font=("Arial", 12))
entry_destination.pack(pady=5)

tk.Label(root, text="Date (DD/MM/YYYY):", font=("Arial", 12, "bold"), bg="#F0E68C").pack(pady=5)
entry_date = tk.Entry(root, font=("Arial", 12))
entry_date.pack(pady=5)

# Train class selection
tk.Label(root, text="Class:", font=("Arial", 12, "bold"), bg="#F0E68C").pack(pady=5)
class_var = ttk.Combobox(root, values=["First Class", "Second Class", "Sleeper", "AC 3 Tier", "AC 2 Tier", "AC 1 Tier"], font=("Arial", 12))
class_var.pack(pady=5)

# Number of seats
tk.Label(root, text="Number of Seats:", font=("Arial", 12, "bold"), bg="#F0E68C").pack(pady=5)
entry_seats = tk.Entry(root, font=("Arial", 12))
entry_seats.pack(pady=5)

# Booking Button
tk.Button(root, text="Book Ticket", font=("Arial", 14, "bold"), bg="#4682B4", fg="white", command=book_ticket).pack(pady=20)

# Run the application
root.mainloop()












