import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Expense Tracker")
window.geometry("400x300")
window.configure(bg= "#f5f5f5")
content = tk.Frame(window, bg="#f5f5f5")
content.pack(fill="both", expand=True, padx=20, pady=20)


label = tk.Label(
    content,
    text="Personal Expense Tracker",
    bg="#f5f5f5",
    fg="#222222",
    font=("Helvetica", 18,"bold")
)
label.pack(pady=(0,20))

form = tk.Frame(content, bg="#ffffff")
form.pack(fill="x", pady=(0, 20))

name_label= tk.Label(
    form,
    text= "Expense Name",
    bg="#f5f5f5",
    fg="#222222",
    font=("Helvetica",12)
)
name_label.pack(anchor="w", padx=30)

name_entry = tk.Entry(
    form,
    font=("Helvetica", 12),
    width= 25,
    bd=2,
    relief="groove"
)
name_entry.pack(fill="x", pady=(0,10))

amount_label = tk.Label(
    form, text="Amount ($):", bg="#f5f5f5", fg="#222222", font=("Helvetica", 12)
)
amount_label.pack(anchor="w", padx=30)

amount_entry = tk.Entry(form, font=("Helvetica", 12),width=25, bd=2, relief="groove")
amount_entry.pack(fill="x", pady=(0, 10))

def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()
    if name == "" or amount == "":
        return 
    expense_table.insert(
        "", "end", values=(name,amount)
    )
    name_entry.delete(0,tk.END)
    amount_entry.delete(0, tk.END)

def delete_expense():
    selected = expense_table.selection()

    if not selected:
        return
    
    expense_table.delete(selected[0])

button_row = tk.Frame(content, bg="#f5f5f5")
button_row.pack(fill="x", pady=(0, 20))


delete_button = tk.Button(
        window,
        text= "Delete Selected",
        bg= "#e53935",
        fg= "white",
        font=("Helvetica", 11, "bold"),
        bd=0,
        padx=10,
        pady=5,
        command=delete_expense
)
delete_button.pack(in_=button_row, side="left", expand=True, fill="x")

add_button = tk.Button(
    window,
    text="Add Expense",
    bg="#4caf50",
    fg="white",
    font=("Helvetica", 12, "bold"),
    bd=0,
    padx=10,
    pady=5,
    command=add_expense
)
add_button.pack(in_=button_row, side="left", expand=True, fill="x", padx=(0, 10))
table_frame = tk.Frame(window, bg="#f5f5f5")
table_frame.pack(fill="both", expand=True, pady=(10, 0))


expense_table = ttk.Treeview(
    table_frame,
    columns=("Name", "Amount"),
    show="headings"
)

expense_table.heading("Name", text="Expense Name")
expense_table.heading("Amount", text="Amount")

expense_table.column("Name", anchor="w", width=200)
expense_table.column("Amount", anchor="center", width=100)
expense_table.pack(fill="both", expand=True)

expense_table.insert("", "end", values=("Groceries", "$5000"))
expense_table.insert("", "end", values=("Groceries", "$5000"))

expense_table.selection()

window.mainloop()