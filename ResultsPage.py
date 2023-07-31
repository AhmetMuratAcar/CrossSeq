import customtkinter


class KeyElements(customtkinter.CTk):
    """Used to construct the key for interpreting graph results."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class TopFrame(customtkinter.CTkFrame):
    """Contains options that pertain to all results."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Key for result graphs.

        # GREEN
        self.greenFrame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.greenFrame.pack(side="top")
        self.green = customtkinter.CTkLabel(master=self.greenFrame,
                                            fg_color="#00FF00",  # Green
                                            width=26,
                                            height=26,
                                            text="",
                                            corner_radius=13)
        self.green.pack(side="left")
        self.greenText = customtkinter.CTkLabel(master=self.greenFrame,
                                                fg_color="transparent",
                                                text="= Matching Sequence",
                                                padx=2)
        self.greenText.pack(side="left")

        # GRAY
        self.grayFrame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.grayFrame.pack(side="left")
        self.gray = customtkinter.CTkLabel(master=self.grayFrame,
                                           fg_color="#A9A9A9",  # Gray
                                           width=26,
                                           height=26,
                                           text="",
                                           corner_radius=13)
        self.gray.pack(side="left")
        self.grayText = customtkinter.CTkLabel(master=self.grayFrame,
                                               fg_color="transparent",
                                               text="= Differing Sequence",
                                               padx=2, )
        self.grayText.pack(side="right")

        # RED
        self.redFrame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.redFrame.pack(side="right")
        self.red = customtkinter.CTkLabel(master=self.redFrame,
                                          fg_color="#FF0000",  # Red
                                          width=26,
                                          height=26,
                                          text="",
                                          corner_radius=13)
        self.red.pack(side="left")
        self.redText = customtkinter.CTkLabel(master=self.redFrame,
                                              fg_color="transparent",
                                              text="= Out of Scope",
                                              padx=2)
        self.redText.pack(side="left")

        # Yellow
        self.yellowFrame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.yellowFrame.pack(side="bottom")
        self.yellow = customtkinter.CTkLabel(master=self.yellowFrame,
                                             fg_color="#FF0000",  # Red
                                             width=26,
                                             height=26,
                                             text="",
                                             corner_radius=13)
        self.yellow.pack(side="left")
        self.yellowText = customtkinter.CTkLabel(master=self.yellowFrame,
                                                 fg_color="transparent",
                                                 text="= Out of Scope",
                                                 padx=2)
        self.yellowText.pack(side="left")


class ResultFrame:
    """Frame in which all results for one sequence are displayed."""

    def __init__(self, master):
        pass


class Results(customtkinter.CTk):
    """Full window in which all ResultFrames are displayed."""

    def __init__(self):
        super().__init__()
        self.title("Results")
        self.geometry("400x600")

        # Scrollable frame in which the result frames will be placed.
        self.completeFrame = customtkinter.CTkScrollableFrame(master=self)
        self.completeFrame.pack(side="bottom", fill="both", expand="true")
        self.frame_list = []

        # Bring in TopFrame
        self.topFrame = TopFrame(master=self, fg_color="transparent")
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
