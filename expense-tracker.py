import tkinter as tk
from tkinter import messagebox

def save_data():
    with open("expenses.txt", "w") as file:
        for item in listbox.get(0, tk.END):
            file.write(item + "\n") 

def load_data():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    listbox.insert(tk.END, line)
        if listbox.size() > 0:
            current_total = sum(float(i.split(": $")[1]) for i in listbox.get(0, tk.END))
            label_total.config(text=f"${current_total:.2f}")
    except FileNotFoundError:
        pass

def add_expense():
    description = entry_description.get()
    amount = entry_amount.get()
    
    if description and amount:
        try:
            amount_float = float(amount)
            expense_entry = f"{description}: ${amount_float:.2f}"
            listbox.insert(tk.END, expense_entry)
            
            # Update total
            current_total = sum(float(i.split(": $")[1]) for i in listbox.get(0, tk.END))
            label_total.config(text=f"${current_total:.2f}")
            
            # Clear entries
            entry_description.delete(0, tk.END)
            entry_amount.delete(0, tk.END)
            entry_description.focus()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for amount")
    else:
        messagebox.showwarning("Missing Data", "Please enter both description and amount")

def delete_expense():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        
        # Update total
        if listbox.size() > 0:
            current_total = sum(float(i.split(": $")[1]) for i in listbox.get(0, tk.END))
            label_total.config(text=f"${current_total:.2f}")
        else:
            label_total.config(text="$0.00")
    except IndexError:
        messagebox.showwarning("No Selection", "Please select an expense to delete")

def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all expenses?"):
        listbox.delete(0, tk.END)
        label_total.config(text="$0.00")

# Create main window
root = tk.Tk()
root.title("💰 Expense Tracker")
root.geometry("600x550")
root.configure(bg="#1a1a2e")
root.resizable(False, False)

# Modern color scheme
PRIMARY_COLOR = "#0f3460"
SECONDARY_COLOR = "#16213e"
ACCENT_COLOR = "#e94560"
TEXT_COLOR = "#eaeaea"
ENTRY_BG = "#16213e"
BUTTON_HOVER = "#533483"

# Header
header_frame = tk.Frame(root, bg="#0f3460", height=80)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

title_label = tk.Label(header_frame, text="💰 EXPENSE TRACKER", 
                       font=("Helvetica", 24, "bold"), 
                       bg="#0f3460", fg="#eaeaea")
title_label.pack(pady=20)

# Main container
main_container = tk.Frame(root, bg="#1a1a2e")
main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Input frame with modern styling
input_frame = tk.Frame(main_container, bg="#16213e", relief=tk.FLAT, bd=2)
input_frame.pack(fill=tk.X, pady=(0, 15))

# Description input
desc_container = tk.Frame(input_frame, bg="#16213e")
desc_container.pack(side=tk.LEFT, padx=15, pady=15)

tk.Label(desc_container, text="Description", 
         font=("Helvetica", 10, "bold"), 
         bg="#16213e", fg="#eaeaea").pack(anchor=tk.W)
entry_description = tk.Entry(desc_container, width=25, 
                             font=("Helvetica", 11),
                             bg="#0f3460", fg="#eaeaea",
                             insertbackground="#eaeaea",
                             relief=tk.FLAT, bd=0)
entry_description.pack(ipady=8, pady=(5, 0))

# Amount input
amount_container = tk.Frame(input_frame, bg="#16213e")
amount_container.pack(side=tk.LEFT, padx=15, pady=15)

tk.Label(amount_container, text="Amount ($)", 
         font=("Helvetica", 10, "bold"), 
         bg="#16213e", fg="#eaeaea").pack(anchor=tk.W)
entry_amount = tk.Entry(amount_container, width=15, 
                        font=("Helvetica", 11),
                        bg="#0f3460", fg="#eaeaea",
                        insertbackground="#eaeaea",
                        relief=tk.FLAT, bd=0)
entry_amount.pack(ipady=8, pady=(5, 0))

# Add button in input frame
add_btn_container = tk.Frame(input_frame, bg="#16213e")
add_btn_container.pack(side=tk.LEFT, padx=15, pady=15)

tk.Label(add_btn_container, text=" ", 
         font=("Helvetica", 10), 
         bg="#16213e").pack(anchor=tk.W)  # Spacer

btn_add = tk.Button(add_btn_container, text="➕ Add Expense", 
                    command=add_expense,
                    font=("Helvetica", 11, "bold"),
                    bg="#e94560", fg="white",
                    relief=tk.FLAT, bd=0,
                    cursor="hand2",
                    padx=20, pady=10)
btn_add.pack(pady=(5, 0))

# Action buttons frame
button_frame = tk.Frame(main_container, bg="#1a1a2e")
button_frame.pack(fill=tk.X, pady=(0, 15))

btn_delete = tk.Button(button_frame, text="🗑️ Delete Selected", 
                       command=delete_expense,
                       font=("Helvetica", 10, "bold"),
                       bg="#533483", fg="white",
                       relief=tk.FLAT, bd=0,
                       cursor="hand2",
                       padx=15, pady=8)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="🔄 Clear All", 
                      command=clear_all,
                      font=("Helvetica", 10, "bold"),
                      bg="#533483", fg="white",
                      relief=tk.FLAT, bd=0,
                      cursor="hand2",
                      padx=15, pady=8)
btn_clear.pack(side=tk.LEFT, padx=5)

# Listbox frame with modern styling
list_frame = tk.Frame(main_container, bg="#16213e", relief=tk.FLAT)
list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

scrollbar = tk.Scrollbar(list_frame, bg="#0f3460", 
                         troughcolor="#16213e",
                         relief=tk.FLAT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, 
                     width=60, 
                     height=10,
                     font=("Courier", 11),
                     bg="#0f3460", 
                     fg="#eaeaea",
                     selectbackground="#e94560",
                     selectforeground="white",
                     relief=tk.FLAT,
                     bd=0,
                     highlightthickness=0,
                     yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)
scrollbar.config(command=listbox.yview)

# Total display with modern card design
total_frame = tk.Frame(main_container, bg="#e94560", relief=tk.FLAT)
total_frame.pack(fill=tk.X)

tk.Label(total_frame, text="TOTAL EXPENSES", 
         font=("Helvetica", 10, "bold"), 
         bg="#e94560", fg="white").pack(pady=(15, 5))

label_total = tk.Label(total_frame, text="$0.00", 
                       font=("Helvetica", 28, "bold"),
                       bg="#e94560", fg="white")
label_total.pack(pady=(0, 15))

# Hover effects
def on_enter(e, button, color):
    button['background'] = color

def on_leave(e, button, color):
    button['background'] = color

btn_add.bind("<Enter>", lambda e: on_enter(e, btn_add, "#d63851"))
btn_add.bind("<Leave>", lambda e: on_leave(e, btn_add, "#e94560"))

btn_delete.bind("<Enter>", lambda e: on_enter(e, btn_delete, "#6b4596"))
btn_delete.bind("<Leave>", lambda e: on_leave(e, btn_delete, "#533483"))

btn_clear.bind("<Enter>", lambda e: on_enter(e, btn_clear, "#6b4596"))
btn_clear.bind("<Leave>", lambda e: on_leave(e, btn_clear, "#533483"))

# Bind Enter key to add expense
entry_description.bind("<Return>", lambda e: entry_amount.focus())
entry_amount.bind("<Return>", lambda e: add_expense())

# Load data on startup
load_data()

# Save data on close
root.protocol("WM_DELETE_WINDOW", lambda: [save_data(), root.destroy()])

# Focus on description field
entry_description.focus()

root.mainloop()