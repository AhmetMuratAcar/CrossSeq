import customtkinter


class TopFrame:
    """Contains options that pertain to all results."""
    def __init__(self, master):
        # Probably should pack this outside of the Results scrollable frame.
        pass


class ResultFrame:
    """Frame in which all results for one sequence are displayed."""
    def __init__(self, master):
        pass


class Results(customtkinter.CTk):
    """Full window in which all ResultFrames are displayed."""
    def __init__(self):
        super().__init__()
        # self.geometry("600x500")
        self.title("Results")
        self.frame_list = []

        # Bring in TopFrame

        # Bring in all ResultFrames through result_creation and new_result


def new_result(seq, graphs):
    """Creates a new ResultFrame and packs it in Result frame."""
    pass


def result_creation(objects, graphs):
    """Creates all parts of results within app."""
    pass


results_page = Results()
# results_page.mainloop()


# To display the results you want a new window with frame for each sequence submitted.
# Top frame should be slim and have a download all button and maybe some other things.
# Each frame after initial one should contain the following buttons:
# Nucleotide results (toggles nucleotide results graph and respective stats)
# Codon results (toggles codon results graph and respective stats)
# Download results (downloads a formatted PDF containing both graphs and respective statistics)
