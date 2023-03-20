import customtkinter
import webbrowser

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


def instruction_callback():
    """Opens README of GitHub repo."""
    webbrowser.open_new("https://github.com/AhmetMuratAcar/DNA-Comparer/blob/master/README.md")


def change_appearance_mode_event(new_scaling: str):
    """Changes the theme of the app (Light, Dark, System)."""
    customtkinter.set_appearance_mode(new_scaling)


def submission():
    # Should check if the s
    print("joe")


class TextFrame(customtkinter.CTkScrollableFrame):
    """Frame class containing the input boxes."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.text_boxes = []

        # Main seq entry box
        self.mainSeq = customtkinter.CTkTextbox(self)
        self.mainSeq.pack(padx=(20, 20), pady=(20, 20), side="top", fill="both", expand="true")

    def new_textbox(self):
        """Creates a new textbox below the previous textbox."""
        new_seq_box = customtkinter.CTkTextbox(self)
        new_seq_box.pack(padx=(20, 20), pady=(20, 20), side="top", fill="both")
        self.text_boxes.append(new_seq_box)


class App(customtkinter.CTk):
    """Class that contains the buttons and functionality of the GUI."""
    def __init__(self):
        super().__init__()
        self.title("DNA Comparer")

        self.my_frame = TextFrame(master=self, width=700, height=400, corner_radius=0, fg_color="transparent")
        self.my_frame.pack(side="left", fill="both", expand="true")

        # Button for creating a textbox for a new sequence
        self.newSeqBox = customtkinter.CTkButton(self, text="New Sequence", command=self.new_textbox_call)
        self.newSeqBox.pack(padx=20, pady=(20, 10))

        # Submission button
        self.submitButton = customtkinter.CTkButton(self,
                                                    fg_color="#FA8072",
                                                    hover_color="#CD5C5C",
                                                    text_color=("gray10", "gray90"),
                                                    text="Submit",
                                                    command=submission)
        self.submitButton.pack(padx=20, pady=10)

        # Instruction hyperlink button
        self.instruction_link_button = customtkinter.CTkButton(self,
                                                               text="Instructions and Examples",
                                                               command=instruction_callback)
        self.instruction_link_button.pack(padx=20, pady=10)

        # Theme changing menu
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self,
                                                                values=["System", "Dark", "Light"],
                                                                fg_color=("gray90", "gray20"),
                                                                button_color=("gray90", "gray20"),
                                                                button_hover_color=("gray75", "gray28"),
                                                                text_color=("gray10", "gray90"),
                                                                anchor="center",
                                                                command=change_appearance_mode_event)
        self.appearance_mode_menu.pack(padx=20, pady=10)

    def new_textbox_call(self):
        """Calls function in the Frame class that creates a new textbox below the previous textbox."""
        self.my_frame.new_textbox()


app = App()
app.mainloop()
