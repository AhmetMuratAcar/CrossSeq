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
        self.YellowFrame = KeyElements(master=self, text="= Same Codon Encoded by Different Sequence", color="#FFFF00")
        self.YellowFrame.colorFrame.pack(side="left", padx=(10, 20))

        # Download Button
        self.DownloadResults = customtkinter.CTkButton(master=self,
                                                       text="Download Results",
                                                       command=results_download)
        self.DownloadResults.pack(side="left", padx=(0, 20))


class ResultFrame:
    """Frame in which all results for one sequence are displayed."""

    def __init__(self, master, seq_obj, graphs):
        # Frame everything goes in
        self.results_frame = customtkinter.CTkFrame(master=master, corner_radius=0)
        self.results_frame.pack(side="top", fill="x", expand="true")

        # ID label
        self.seq_label = customtkinter.CTkLabel(master=self.results_frame, text=f"Sequence: {seq_obj.id}")
        self.seq_label.pack(anchor="w", padx=20)

        # Bringing in nucleotide and codon graphs
        self.nuc_graph = customtkinter.CTkImage(light_image=graphs[1], size=(seq_obj.graphLengths[0], 60))
        self.nuc_label = customtkinter.CTkLabel(master=self.results_frame, image=self.nuc_graph, text="")
        self.nuc_label.pack(anchor="w", padx=20, pady=(0, 10))

        self.codon_graph = customtkinter.CTkImage(light_image=graphs[0], size=(seq_obj.graphLengths[1], 60))
        self.codon_label = customtkinter.CTkLabel(master=self.results_frame, image=self.codon_graph, text="")
        self.codon_label.pack(anchor="w", padx=20)


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

        for i in range(0, len(objects)):
            curr_graphs = (graphs[(i*2)-1], graphs[i*2])  # incrementing graphs to make sure objects and graphs match.
            result_frame = ResultFrame(master=self.completeFrame, seq_obj=objects[i], graphs=curr_graphs)
            self.frame_list.append(result_frame)
