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
        self.DownloadResults.pack(side="right", padx=(0,20))


class ResultFrame:
    """Frame in which all results for one sequence are displayed."""

    def __init__(self, master):
        pass


class Results(customtkinter.CTkToplevel):
    """Full window in which all ResultFrames are displayed."""

    def __init__(self):
        super().__init__()
        self.title("Results")
        self.geometry("1050x600")

        # Bring in TopFrame
        self.topFrame = TopFrame(master=self, fg_color="transparent")
        self.topFrame.pack(side="top")

        # Scrollable frame in which the result frames will be placed.
        self.completeFrame = customtkinter.CTkScrollableFrame(master=self)
        self.completeFrame.pack(side="bottom", fill="both", expand="true")
        self.frame_list = []

    def result_creation(self, objects, graphs):
        """Creates all parts of results within app."""
        # For every object, call new_result by passing in the object and respective graphs. Pack the resulting frame
        # here.
        pass

    def new_result(self, seq, graphs):
        """Creates a new ResultFrame and packs it in Result frame."""
        # Call this in result_creation to create a new ResultFrame object. Pack the respective graphs and buttons here.
        # Remember to append self.frame_list with newly created frames.
        pass


# results_page = Results()
# results_page.mainloop()

# To display the results you want a new window with frame for each sequence submitted.
# Top frame should be slim and have a download all button and maybe some other things.
# Each frame after initial one should contain the following buttons:
# Nucleotide results (toggles nucleotide results graph and respective stats)
# Codon results (toggles codon results graph and respective stats)
# Download results (downloads a formatted PDF containing both graphs and respective statistics)
