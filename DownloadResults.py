from tkinter import filedialog
from mdutils.mdutils import MdUtils
import os


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
    stats_file = MdUtils(file_name=destination)
    stats_file.new_header(level=1, title=f"Main Sequence ID: {title_id}")
    stats_file.new_header(level=2, title="")

    # Creating formatted markdown section for each sequence
    for sequence in sequences:
        stats_file.new_header(level=3, title=f"ID: {sequence.id}")
        stats_file.new_header(level=4, title="Nucleotide Statistics")

        nucleotide_table_data = ["Result", "Percentage"]
        nucleotide_table_data.extend(["Matching", sequence.nucleotideStats["G"]])
        nucleotide_table_data.extend(["Differing", sequence.nucleotideStats["N"]])
        nucleotide_table_data.extend(["Out of Scope", sequence.nucleotideStats["X"]])
        stats_file.new_table(columns=2, rows=4, text_align="center", text=nucleotide_table_data)

        stats_file.new_header(level=4, title="Codon Statistics")
        stats_file.new_paragraph("SCEDS = same codon encoded by different sequence")

        codon_table_data = ["Result", "Percentage"]
        codon_table_data.extend(["Matching", sequence.codonStats["G"]])
        codon_table_data.extend(["Differing", sequence.codonStats["N"]])
        codon_table_data.extend(["SCEDS", sequence.codonStats["Y"]])
        codon_table_data.extend(["Out of Scope", sequence.codonStats["X"]])
        stats_file.new_table(columns=2, rows=5, text_align="center", text=codon_table_data)

        # Divider
        stats_file.new_paragraph("---")

    stats_file.create_md_file()
