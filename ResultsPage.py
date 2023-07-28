import customtkinter


class TopFrame(customtkinter.CTkFrame):
    """Contains options that pertain to all results."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Key for result graphs.
        self.green = customtkinter.CTkLabel(master=self,
                                            fg_color="#00FF00",  # Green
                                            width=25,
                                            height=25,
                                            text="")
        self.green.pack(side="left")
        self.greenText = customtkinter.CTkLabel(master=self,
                                                fg_color="transparent",
                                                text="= Matching Sequence",
                                                padx=2)
        self.greenText.pack(side="left")

        self.gray = customtkinter.CTkLabel(master=self,
                                           fg_color=,  # Gray
                                           width=25,
                                           height=25,
                                           text="")
        # Probably should pack this outside of the Results scrollable frame.


class ResultFrame:
    """Frame in which all results for one sequence are displayed."""

    def __init__(self, master):
        pass


class Results(customtkinter.CTk):
    """Full window in which all ResultFrames are displayed."""

    def __init__(self):
        super().__init__()
        self.title("Results")

        # Scrollable frame in which the result frames will be placed.
        self.completeFrame = customtkinter.CTkScrollableFrame(master=self)
        self.completeFrame.pack(side="bottom", fill="both", expand="true")
        self.frame_list = []

        # Bring in TopFrame
        self.topFrame = TopFrame(master=self)
        self.topFrame.pack(side="top")
        # Bring in all ResultFrames through result_creation and new_result


def new_result(seq, graphs):
    """Creates a new ResultFrame and packs it in Result frame."""
    pass


def result_creation(objects, graphs):
    """Creates all parts of results within app."""
    pass


results_page = Results()
results_page.mainloop()

# To display the results you want a new window with frame for each sequence submitted.
# Top frame should be slim and have a download all button and maybe some other things.
# Each frame after initial one should contain the following buttons:
# Nucleotide results (toggles nucleotide results graph and respective stats)
# Codon results (toggles codon results graph and respective stats)
# Download results (downloads a formatted PDF containing both graphs and respective statistics)
