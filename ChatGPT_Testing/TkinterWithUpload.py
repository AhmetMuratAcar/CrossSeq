import tkinter as tk
import tkinter.filedialog as filedialog

# Create the main window
window = tk.Tk()
window.title("FASTA Sequence Comparison")
window.geometry("500x300")


# Define the functions for the buttons
def input_seq():
    # Get the sequences from the user input
    seq1 = input_seq1.get()
    seq2 = input_seq2.get()
    # Perform the comparison
    compare_sequences(seq1, seq2)


def upload_seq():
    # Open a file dialog to get the file paths
    filepath1 = filedialog.askopenfilename()
    filepath2 = filedialog.askopenfilename()
    # Read the sequences from the files
    seq1 = read_fasta(filepath1)
    seq2 = read_fasta(filepath2)
    # Perform the comparison
    compare_sequences(seq1, seq2)


def compare_sequences(seq1, seq2):
    # Perform the comparison and display the result
    result = "The sequences are not identical."
    if seq1 == seq2:
        result = "The sequences are identical."
    result_label.config(text=result)


def read_fasta(filepath):
    # Read the sequence from a FASTA file
    with open(filepath) as file:
        seq = ""
        for line in file:
            if not line.startswith(">"):
                seq += line.strip()
    return seq


# Create the input fields and labels
input_seq1_label = tk.Label(window, text="Input sequence 1:")
input_seq1_label.pack()
input_seq1 = tk.Entry(window)
input_seq1.pack()

input_seq2_label = tk.Label(window, text="Input sequence 2:")
input_seq2_label.pack()
input_seq2 = tk.Entry(window)
input_seq2.pack()

# Create the buttons
input_button = tk.Button(window, text="Compare Input Sequences", command=input_seq, bg="#0077be", fg="white", font=("Arial", 12), padx=10, pady=5, border=0)
input_button.pack(pady=10)

upload_button = tk.Button(window, text="Upload Sequences", command=upload_seq, bg="#0077be", fg="white", font=("Arial", 12), padx=10, pady=5, border=0)
upload_button.pack(pady=10)

# Create the result label
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start the main loop
window.mainloop()
