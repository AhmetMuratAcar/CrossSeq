import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title("FASTA Sequences")
window.geometry("500x300")
window.configure(bg="#f0f0f0")

# Create a style for the labels
label_style = ttk.Style()
label_style.configure("Bold.TLabel", font=("Helvetica", 14, "bold"), foreground="#333333", background="#f0f0f0")

# Create a label for the header
header_label = ttk.Label(text="Enter FASTA Sequences", style="Bold.TLabel")
header_label.grid(column=0, row=0, padx=20, pady=20, columnspan=2)

# Create a style for the entry fields
entry_style = ttk.Style()
entry_style.configure("Custom.TEntry", font=("Helvetica", 12), foreground="#333333", background="#f5f5f5", bordercolor="#e0e0e0", relief="flat")

# Create a label for the first sequence
label1 = ttk.Label(text="Sequence 1:", style="Bold.TLabel")
label1.grid(column=0, row=1, padx=20, pady=10)

# Create an entry field for the first sequence
entry1 = ttk.Entry(width=50, style="Custom.TEntry")
entry1.grid(column=1, row=1, padx=20, pady=10)

# Create a label for the second sequence
label2 = ttk.Label(text="Sequence 2:", style="Bold.TLabel")
label2.grid(column=0, row=2, padx=20, pady=10)

# Create an entry field for the second sequence
entry2 = ttk.Entry(width=50, style="Custom.TEntry")
entry2.grid(column=1, row=2, padx=20, pady=10)

# Define a function to submit the sequences
def submit_sequences():
    seq1 = entry1.get()
    seq2 = entry2.get()
    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)

# Create a style for the button
button_style = ttk.Style()
button_style.configure("Submit.TButton", font=("Helvetica", 12), background="#007bff", foreground="#ffffff", padding=10, relief="flat")

# Create a button to submit the sequences
submit_button = ttk.Button(text="Submit", command=submit_sequences, style="Submit.TButton")
submit_button.grid(column=1, row=3, padx=20, pady=20)

# Add some padding to the window
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(3, weight=1)
window.config(padx=20, pady=20)

# Run the window
window.mainloop()
