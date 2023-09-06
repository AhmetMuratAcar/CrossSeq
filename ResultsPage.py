import customtkinter
from DownloadResults import results_download


class KeyElements(customtkinter.CTk):
    """Used to construct the key for interpreting graph results."""

    def __init__(self, master, color: str, text):
        super().__init__()

        # Frame for storing key color and definition
        self.colorFrame = customtkinter.CTkFrame(master=master, fg_color="transparent")

        # Color of the label
        self.keyElement = customtkinter.CTkLabel(master=self.colorFrame,
                                                 fg_color=color,
                                                 width=26,
                                                 height=26,
                                                 text="",
                                                 corner_radius=13)
        self.keyElement.pack(side="left")

        # Definition text
        self.colorDefinition = customtkinter.CTkLabel(master=self.colorFrame,
                                                      fg_color="transparent",
                                                      text=text,
                                                      padx=2)
        self.colorDefinition.pack(side="left")


class TopFrame(customtkinter.CTkFrame):
    """Contains options that pertain to all results."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # For results_download function
        self.main_seq = None
        self.sequences = None
        self.graphs = None

        # Key for result graphs.
        # GREEN
        self.greenFrame = KeyElements(master=self, text="= Matching Sequence", color="#00FF00")
        self.greenFrame.colorFrame.pack(side="left", padx=(20, 10), pady=10)

        # GRAY
        self.grayFrame = KeyElements(master=self, text="= Differing Sequence", color="#A9A9A9")
        self.grayFrame.colorFrame.pack(side="left", padx=10)

        # RED
        self.redFrame = KeyElements(master=self, text="= Out of Scope", color="#FF0000")
        self.redFrame.colorFrame.pack(side="left", padx=10)

        # Yellow
        self.yellowFrame = KeyElements(master=self, text="= Same Codon Encoded by Different Sequence", color="#FFFF00")
        self.yellowFrame.colorFrame.pack(side="left", padx=(10, 20))

        # Download Button
        self.DownloadResults = customtkinter.CTkButton(master=self,
                                                       text="Download Results",
                                                       command=self.download_creation)
        self.DownloadResults.pack(side="left", padx=(0, 20))

    def download_creation(self):
        """Calls results_download with proper items."""
        results_download(seq_objects=self.sequences, graphs=self.graphs, main_id=self.main_seq)


class StatsKey(customtkinter.CTkFrame):
    """Key for constructing stats for each graph."""

    def __init__(self, master, data):
        super().__init__(master)
        self.greenFrame = KeyElements(master=self, text=f": {data['G']}%", color="#00FF00")
        self.greenFrame.colorFrame.pack(side="left", padx=(20, 10), pady=10)

        self.grayFrame = KeyElements(master=self, text=f": {data['N']}%", color="#A9A9A9")
        self.grayFrame.colorFrame.pack(side="left", padx=10, pady=10)

        self.redFrame = KeyElements(master=self, text=f": {data['X']}%", color="#FF0000")
        self.redFrame.colorFrame.pack(side="left", padx=10, pady=10)

        if data["Y"]:
            self.yellowFrame = KeyElements(master=self, text=f": {data['Y']}%", color="#FFFF00")
            self.yellowFrame.colorFrame.pack(side="left", padx=10, pady=10)


class ResultFrame:
    """Frame in which all results for one sequence are displayed."""

    def __init__(self, master, seq_obj, graphs):
        # Frame everything goes in
        self.results_frame = customtkinter.CTkFrame(master=master, corner_radius=0)
        self.results_frame.pack(side="top", fill="x", expand="true")

        # Frame for sequence info
        self.info_frame = customtkinter.CTkFrame(master=self.results_frame, corner_radius=0, fg_color="transparent")
        self.info_frame.pack(side="top", fill="x", expand="true")

        # ID label
        self.seq_label = customtkinter.CTkLabel(master=self.info_frame, text=f"Sequence: {seq_obj.id}")
        self.seq_label.pack(side="left", padx=20)

        # Nucleotide and codon CDS length labels
        self.nucCDS_len = customtkinter.CTkLabel(master=self.info_frame,
                                                 text=f"Nucleotide CDS Length: {len(seq_obj.nucleotideResults)}")
        self.nucCDS_len.pack(side="left", padx=20)

        self.codonCDS_len = customtkinter.CTkLabel(master=self.info_frame,
                                                   text=f"Codon CDS Length: {len(seq_obj.codonResults)}")
        self.codonCDS_len.pack(side="left", padx=20)

        # Nucleotide graph and statistics
        self.nuc_graph_label = customtkinter.CTkLabel(master=self.results_frame, text="Nucleotide Graph")
        self.nuc_graph_label.pack(anchor="w", padx=20)
        self.nuc_graph = customtkinter.CTkImage(light_image=graphs[0], size=(seq_obj.graphLengths[0], 30))
        self.nuc_label = customtkinter.CTkLabel(master=self.results_frame, image=self.nuc_graph, text="")
        self.nuc_label.pack(anchor="w", padx=20, pady=(0, 10))

        self.nuc_stats = StatsKey(master=self.results_frame, data=seq_obj.nucleotideStats)
        self.nuc_stats.configure(fg_color="transparent")
        self.nuc_stats.pack(anchor="w", padx=20, pady=(0, 10))

        # Codon graph and statistics
        self.codon_graph_label = customtkinter.CTkLabel(master=self.results_frame, text="Codon Graph")
        self.codon_graph_label.pack(anchor="w", padx=20)
        self.codon_graph = customtkinter.CTkImage(light_image=graphs[1], size=(seq_obj.graphLengths[1], 30))
        self.codon_label = customtkinter.CTkLabel(master=self.results_frame, image=self.codon_graph, text="")
        self.codon_label.pack(anchor="w", padx=20, pady=(0, 10))

        self.codon_stats = StatsKey(master=self.results_frame, data=seq_obj.codonStats)
        self.codon_stats.configure(fg_color="transparent")
        self.codon_stats.pack(anchor="w", padx=20)


class SpacerFrame:
    """Spacers for visual clarity between ResultFrames"""
    def __init__(self, master):
        self.spacerFrame = customtkinter.CTkFrame(master=master, fg_color="#1a1a1a", corner_radius=0, height=5)
        self.spacerFrame.pack(side="top", fill="x")


class Results(customtkinter.CTkToplevel):
    """Full window in which all ResultFrames are displayed."""

    def __init__(self):
        super().__init__()
        self.title("Results")
        self.geometry("1050x600")

        # Main sequence ID
        self.main_seq_ID = customtkinter.CTkLabel(master=self, text="Main sequence ID: ")
        self.main_seq_ID.pack(side="top", pady=(5, 0))

        # Bring in TopFrame
        self.topFrame = TopFrame(master=self, fg_color="transparent")
        self.topFrame.pack(side="top")

        # Scrollable frame in which the result frames will be placed.
        self.completeFrame = customtkinter.CTkScrollableFrame(master=self)
        self.completeFrame.pack(side="bottom", fill="both", expand="true")
        self.frame_list = []

    def result_creation(self, main_seq, objects, graphs):
        """Creates all parts of results within app."""
        self.main_seq_ID.configure(text=f"Main sequence ID: {main_seq.id}")

        for i in range(0, len(graphs), 2):
            curr_graphs = (graphs[i], graphs[i+1])
            result_frame = ResultFrame(master=self.completeFrame, seq_obj=objects[int(i/2)], graphs=curr_graphs)
            self.frame_list.append(result_frame)

            # Creating spacers between all results
            if i != len(graphs)-2:
                SpacerFrame(master=self.completeFrame)

        # Updating topFrame elements for use in results_download
        self.topFrame.main_seq = main_seq.id
        self.topFrame.sequences = objects
        self.topFrame.graphs = graphs
