# Color key:
# UTRs: un-highlighted
# Different: red
# Same: green
# Same codon encoded by different nucleotides: yellow
#
# Goal 1: Write a program that returns the differences between two FASTA sequences.
# Goal 2: Grab the names of the sequences from the FASTA inputs.
# Goal 3: Determine if you are going to make this into an application or a website.
# Goal 4: Figure out how to obtain the inputs of the text areas when submit button is pressed.
# Goal 5: Figure out how to highlight according to the color key.
# Goal 6: Make a button that when pressed creates a section for another sequence. All sequences will be compared to 1st.
# Goal 7: Generate the horizontal bar graphs for visualization.
# Goal end: Make a sample page with an example showing how to use it with pictures.

from SequenceClass import Sequence
from App import App


# def comparer(seq1, seq2):
#     """Compares the two given sequences. Return differences between the two."""
#     # Maybe use zip function?
#     # pprint(list(zip(first_seq, second_seq)))
#     pass


main_file = "Testing Sequences/Oryza_sativa.fasta"
second_file = "Testing Sequences/Arabidopsis_thaliana.fasta"

main_seq = Sequence()
second_seq = Sequence()

# Main seq calls
# main_seq.parse_fasta(main_file)
# main_seq.id_retrieve()
# main_seq.seq_retrieve()
# main_seq.find_start_stop()

# Second seq calls
# second_seq.parse_fasta(second_file)
# second_seq.id_retrieve()
# second_seq.seq_retrieve()
# second_seq.find_start_stop()

# comparer(main_seq.codingSeq, second_seq.codingSeq)

screen = App()
screen.mainloop()
