from tkinter import filedialog
from mdutils.mdutils import MdUtils
import os
from SequenceClass import Sequence


def results_download(main_id, seq_objects, graphs):
    """Allows user to choose where graphs and statistics will be saved."""

    # Creating folder in user's desired path
    folder_name = f"{main_id}_vs_{len(seq_objects)}"
    path = filedialog.askdirectory()
    folder = os.path.join(path, folder_name)
    os.makedirs(folder, exist_ok=True)

    # Saving graphs
    for i in range(0, len(graphs), 2):
        nuc_graph_name = f"{seq_objects[int(i/2)].id}_Nucleotide_Graph.jpg"
        nuc_graph_file = os.path.join(folder, nuc_graph_name)
        graphs[i].save(nuc_graph_file, format="PNG")

        codon_graph_name = f"{seq_objects[int(i/2)].id}_Codon_Graph.jpg"
        codon_graph_file = os.path.join(folder, codon_graph_name)
        graphs[i+1].save(codon_graph_file, format="PNG")

    # Creating markdown file in folder above
    md_name = f"{folder_name}_statistics"
    md_file = os.path.join(folder, md_name)
    create_markdown(sequences=seq_objects, destination=md_file, title_id=main_id)


def create_markdown(title_id, sequences, destination):
    """Creates and saves markdown file containing generated statistics results."""
    file = MdUtils(file_name=destination, title=f"Main Sequence ID: {title_id}")
    file.create_md_file()  # Remember to move this command to the very end after all text is written.


# Test variables
main_ting = "joe"
graph_ting = [0, 1, 2, 3, 4, 5]

seq1 = Sequence()
seq1.id = "TEST 1"
seq1.nucleotideStats[0] = 10.0
seq1.nucleotideStats[1] = 20.0
seq1.nucleotideStats[2] = 30.0

seq1.codonStats[0] = 40.0
seq1.codonStats[1] = 50.0
seq1.codonStats[2] = 60.0
seq1.codonStats[3] = 70.0

seq2 = Sequence()
seq1.id = "TEST 2"
seq1.nucleotideStats[0] = 80.0
seq1.nucleotideStats[1] = 90.0
seq1.nucleotideStats[2] = 100.0

seq1.codonStats[0] = 110.0
seq1.codonStats[1] = 120.0
seq1.codonStats[2] = 130.0
seq1.codonStats[3] = 140.0

seq_list = [seq1, seq2]

# results_download(main_id=main_ting, graphs=graph_ting, seq_objects=seq_list)
