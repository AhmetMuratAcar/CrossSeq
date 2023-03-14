import tkinter as tk

# Create a window
window = tk.Tk()
window.title("FASTA Sequences")

# Create a label for the first sequence
label1 = tk.Label(text="Sequence 1:")
label1.grid(column=0, row=0, padx=10, pady=10)

# Create an entry field for the first sequence
entry1 = tk.Entry(width=50)
entry1.grid(column=1, row=0, padx=10, pady=10)

# Create a label for the second sequence
label2 = tk.Label(text="Sequence 2:")
label2.grid(column=0, row=1, padx=10, pady=10)

# Create an entry field for the second sequence
entry2 = tk.Entry(width=50)
entry2.grid(column=1, row=1, padx=10, pady=10)

# Define a function to submit the sequences
def submit_sequences():
    seq1 = entry1.get()
    seq2 = entry2.get()
    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)

# Create a button to submit the sequences
submit_button = tk.Button(text="Submit", command=submit_sequences)
submit_button.grid(column=1, row=2, padx=10, pady=10)

# Run the window
window.mainloop()
