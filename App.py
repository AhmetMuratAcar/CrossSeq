import customtkinter
import webbrowser
from PIL import Image

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
        self.new_frame = None
        self.new_label = None
        self.new_seq_box = None
        self.new_del_button = None

        self.text_boxes = []
        self.count = len(self.text_boxes) + 1

        # Image for the delete buttons
        self.trash_image = customtkinter.CTkImage(light_image=Image.open("Images/trash.png"),
                                                  dark_image=Image.open("Images/trash.png"),
                                                  size=(30, 30))

        # Frame for the main sequence
        self.main_seq_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color="transparent")
        self.main_seq_frame.pack(side="top", fill="x")

        # Main seq label
        self.main_label = customtkinter.CTkLabel(master=self.main_seq_frame, text="Main Sequence", padx=20)
        self.main_label.pack(anchor="w")

        # Main seq entry box
        self.mainSeq = customtkinter.CTkTextbox(self.main_seq_frame)
        self.mainSeq.pack(padx=(20, 0), pady=(0, 10), side="left", anchor="w", fill="both", expand="true")

        # Main seq delete button
        self.main_del_button = customtkinter.CTkButton(master=self.main_seq_frame,
                                                       image=self.trash_image,
                                                       text="",
                                                       command=self.delete,
                                                       height=20,
                                                       width=20)
        self.main_del_button.pack(side="left", padx=10)

    def new_textbox(self):
        """Creates a new label and textbox below the previous textbox."""
        # Frame for new text box
        self.new_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color="transparent")
        self.new_frame.pack(side="top", fill="x")

        # Label
        self.new_label = customtkinter.CTkLabel(master=self.new_frame, text=f"Sequence #{self.count}", padx=20)
        self.new_label.pack(anchor="w")

        # Text box
        self.new_seq_box = customtkinter.CTkTextbox(master=self.new_frame)
        self.new_seq_box.pack(padx=(20, 0), pady=(0, 10), side="left", anchor="w", fill="both", expand="true")
        self.text_boxes.append(self.new_seq_box)

        # Delete button
        self.new_del_button = customtkinter.CTkButton(master=self.new_frame,
                                                      image=self.trash_image,
                                                      text="",
                                                      command=self.delete,
                                                      height=20,
                                                      width=20)
        self.new_del_button.pack(side="left", padx=10)

        self.count += 1

    def delete(self):
        """Deletes the current text in the text box. If the textbox is clear, deletes the text box. Cannot delete the
        main sequence text box. If a text box is deleted, relabels the remaining text boxes to accurately represent the
        number present."""
        # Deleting

        # Relabeling
        pass


class App(customtkinter.CTk):
    """Class that contains the buttons and functionality of the GUI."""

    def __init__(self):
        super().__init__()
        self.title("DNA Comparer")

        # Bringing in the TextFrame class
        self.my_frame = TextFrame(master=self, width=700, height=400, corner_radius=0, fg_color="transparent")
        self.my_frame.pack(side="left", fill="both", expand="true")

        # Instruction hyperlink button
        self.instruction_link_button = customtkinter.CTkButton(self,
                                                               text="Instructions and Examples",
                                                               command=instruction_callback)
        self.instruction_link_button.pack(padx=20, pady=(20, 10))

        # Button for creating a textbox for a new sequence
        self.newSeqBox = customtkinter.CTkButton(self, text="New Sequence", command=self.new_textbox_call)
        self.newSeqBox.pack(padx=20, pady=10)

        # List of all sequences
        self.seq_list = customtkinter.CTkScrollableFrame(master=self)
        self.seq_list.pack(padx=20, pady=10, fill="both", expand="true")

        # Theme changing menu
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self,
                                                                values=["System", "Dark", "Light"],
                                                                fg_color=("gray90", "gray20"),
                                                                button_color=("gray90", "gray20"),
                                                                button_hover_color=("gray75", "gray28"),
                                                                text_color=("gray10", "gray90"),
                                                                anchor="center",
                                                                command=change_appearance_mode_event)
        self.appearance_mode_menu.pack(padx=20, pady=(10, 20), side="bottom")

        # Submission button
        self.submitButton = customtkinter.CTkButton(self,
                                                    fg_color="#FA8072",
                                                    hover_color="#CD5C5C",
                                                    text_color=("gray10", "gray90"),
                                                    text="Submit",
                                                    command=submission)
        self.submitButton.pack(padx=20, pady=10, side="bottom")

    def new_textbox_call(self):
        """Calls function in the Frame class that creates a new textbox below the previous textbox."""
        self.my_frame.new_textbox()


app = App()
app.mainloop()
