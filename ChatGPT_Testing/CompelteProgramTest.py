from Bio import SeqIO, Seq
import tkinter as tk
from tkinter import messagebox
import tempfile
import os

def compare():
    # Get the sequences from the text boxes
    seq1 = seq1_box.get("2.0", tk.END).strip()
    seq2 = seq2_box.get("2.0", tk.END).strip()

    # Write the sequences to temporary files
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as seq1_file:
        seq1_file.write(seq1)
        seq1_file.flush()
        seq1_record = SeqIO.read(seq1_file.name, "fasta")

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as seq2_file:
        seq2_file.write(seq2)
        seq2_file.flush()
        seq2_record = SeqIO.read(seq2_file.name, "fasta")

    # Extract the protein coding sequences
    seq1_cds = str(seq1_record.seq).upper()[3:]
    seq2_cds = str(seq2_record.seq).upper()[3:]

    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    # Find the start and stop codons in the sequences
    seq1_start = seq1_cds.find(start_codon)
    seq2_start = seq2_cds.find(start_codon)

    seq1_stop = None
    seq2_stop = None

    if seq1_start != -1:
        for stop_codon in stop_codons:
            stop_index = seq1_cds.find(stop_codon, seq1_start + 3)
            if stop_index != -1 and (seq1_stop is None or stop_index < seq1_stop):
                seq1_stop = stop_index

    if seq2_start != -1:
        for stop_codon in stop_codons:
            stop_index = seq2_cds.find(stop_codon, seq2_start + 3)
            if stop_index != -1 and (seq2_stop is None or stop_index < seq2_stop):
                seq2_stop = stop_index

    if seq1_start == -1 or seq2_start == -1 or seq1_stop is None or seq2_stop is None:
        tk.messagebox.showerror("Error", "Could not find start or stop codon")
        return

    seq1_cds = seq1_cds[seq1_start:seq1_stop+3]
    seq2_cds = seq2_cds[seq2_start:seq2_stop+3]

    seq1_cds = Seq.translate(seq1_cds)
    seq2_cds = Seq.translate(seq2_cds)

    # Compare the sequences and highlight the differences
    diff = []
    for i in range(len(seq1_cds)):
        if seq1_cds[i] != seq2_cds[i]:
            diff.append(i)

    # Highlight the differences in the text boxes
    seq1_box.tag_configure("highlight", background="yellow")
    seq2_box.tag_configure("highlight", background="yellow")

    for i in diff:
        seq1_box.tag_add("highlight", f"2.{i+3}", f"2.{i+4}")
        seq2_box.tag_add("highlight", f"2.{i+3}", f"2.{i+4}")

    # Remove the temporary files
    os.remove(seq1_file.name)
    os.remove(seq2_file.name)


# Create the main window
root = tk.Tk()
root.title("FASTA Sequence Comparison")

# Create the sequence entry boxes
seq1_label = tk.Label(root, text="Sequence 1:")
seq1_label.grid(row=0, column=0)
seq1_box = tk.Text(root, width=50, height=10)
seq1_box.grid(row=1, column=0)

seq2_label = tk.Label(root, text="Sequence 2:")
seq2_label.grid(row=2, column=0)
seq2_box = tk.Text(root, width=50, height=10)
seq2_box.grid(row=3, column=0)

# Create the submit button
compare_button = tk.Button(root, text="Compare", command=compare)
compare_button.grid(row=4, column=0)

# Run the main loop
root.mainloop()
