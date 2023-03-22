import customtkinter
import webbrowser
from PIL import Image

DEL_IMAGE = customtkinter.CTkImage(light_image=Image.open("Images/trash_(light_mode).png"),
                                   dark_image=Image.open("Images/trash_(dark_mode).png"),
                                   size=(30, 30))

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class MainSeq:
    """Class that constructs the main sequence frame."""
    def __init__(self, master):
        # Frame for main sequence
        self.main_seq_frame = customtkinter.CTkFrame(master=master, corner_radius=0, fg_color="transparent")
        self.main_seq_frame.pack(side="top", fill="x", expand="true")

        # Label for main sequence
        self.main_seq_label = customtkinter.CTkLabel(master=self.main_seq_frame, text="Main Sequence", padx=20)
        self.main_seq_label.pack(anchor="w")

        # Text box
        self.main_seq_text = customtkinter.CTkTextbox(self.main_seq_frame)
        self.main_seq_text.pack(padx=(20, 0), pady=(0, 10), side="left", anchor="w", fill="both", expand="true")

        # Delete button
        self.main_del_button = customtkinter.CTkButton(master=self.main_seq_frame,
                                                       image=DEL_IMAGE,
                                                       text="",
                                                       command=self.main_seq_delete,
                                                       height=20,
                                                       width=20)
        self.main_del_button.pack(side="left", padx=10)

    def main_seq_delete(self):
        """Clears the main sequence textbox."""
        self.main_seq_text.delete('0.0', "end")


class SeqFrame:
    """Class that constructs the sequence frames after main sequence."""
    def __init__(self, master, count):
        # Frame for sequence
        self.new_text_frame = customtkinter.CTkFrame(master=master, corner_radius=0, fg_color="transparent")
        self.new_text_frame.pack(side="top", fill="x", expand="true")

        # Label for sequence
        self.seq_name = f"Sequence #{count}"
        self.new_label = customtkinter.CTkLabel(master=self.new_text_frame, text=self.seq_name, padx=20)
        self.new_label.pack(anchor="w")

        # Text box
        self.new_seq_box = customtkinter.CTkTextbox(master=self.new_text_frame)
        self.new_seq_box.pack(padx=(20, 0), pady=(0, 10), side="left", anchor="w", fill="both", expand="true")

        # Delete button
        self.new_del_button = customtkinter.CTkButton(master=self.new_text_frame,
                                                      image=DEL_IMAGE,
                                                      text="",
                                                      command=self.remove_frame,
                                                      height=20,
                                                      width=20)
        self.new_del_button.pack(side="left", padx=10)

    def remove_frame(self):
        """If text present in the textbox, delete text. Else, delete entire frame. Updates labels for all frames."""
        if len(self.new_seq_box.get("0.0", "end")) > 1:
            self.new_seq_box.delete('0.0', "end")
        else:
            self.new_text_frame.destroy()
            app.frame_list.remove(self)
            app.count = len(app.frame_list) + 1
            app.update_labels()


class ToolBar:
    """Constructs the toolbar on the right side of the window."""
    def __init__(self, master):
        # The frame itself
        self.toolbar_frame = customtkinter.CTkFrame(master=master, corner_radius=0, fg_color="transparent")
        self.toolbar_frame.pack(side="right", fill="both")

        # Instruction hyperlink button
        self.instruction_link_button = customtkinter.CTkButton(master=self.toolbar_frame,
                                                               text="Instructions and Examples",
                                                               command=self.instruction_callback)
        self.instruction_link_button.pack(padx=20, pady=(20, 10))

        # New sequence button
        self.newSeqBox = customtkinter.CTkButton(master=self.toolbar_frame,
                                                 text="New Sequence",
                                                 command=new_frame)
        self.newSeqBox.pack(padx=20, pady=10)

        # Sequence list
        self.seq_list = customtkinter.CTkScrollableFrame(master=self.toolbar_frame, label_text="Sequence List")
        self.seq_list.pack(padx=20, pady=10, fill="both", expand="true")
        main_seq_label = customtkinter.CTkLabel(master=self.seq_list, text="Main Sequence")
        main_seq_label.pack()

        # Theme changing dropdown
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.toolbar_frame,
                                                                values=["System", "Dark", "Light"],
                                                                fg_color=("gray90", "gray20"),
                                                                button_color=("gray90", "gray20"),
                                                                button_hover_color=("gray75", "gray28"),
                                                                text_color=("gray10", "gray90"),
                                                                anchor="center",
                                                                command=change_appearance_mode_event)
        self.appearance_mode_menu.pack(padx=20, pady=(10, 20), side="bottom")

        # Submit button
        self.submitButton = customtkinter.CTkButton(self.toolbar_frame,
                                                    fg_color="#FA8072",
                                                    hover_color="#CD5C5C",
                                                    text_color=("gray10", "gray90"),
                                                    text="Submit",
                                                    command=self.submission)
        self.submitButton.pack(padx=20, pady=10, side="bottom")

    def submission(self):
        pass

    @staticmethod
    def instruction_callback():
        """Opens README of GitHub repo."""
        webbrowser.open_new("https://github.com/AhmetMuratAcar/DNA-Comparer/blob/master/README.md")


class App:
    """Class that puts everything together. The main window."""

    def __init__(self, master):
        self.root = master
        self.root.title("DNA Comparer")
        self.frame_list = []
        self.count = len(self.frame_list) + 1

        # Bringing the toolbox frame into the main window
        self.toolbar_frame = ToolBar(self.root)

        # The scrollable frame in which all sequences are stored
        self.sequences_frame = customtkinter.CTkScrollableFrame(master=self.root,
                                                                width=700,
                                                                height=400,
                                                                corner_radius=0,
                                                                fg_color="transparent")
        self.sequences_frame.pack(side="left", fill="both", expand="true")

        # Bringing in the main sequence frame
        self.main_frame = MainSeq(self.sequences_frame)

    def update_labels(self):
        """Updates all labels after a sequence frame is deleted."""
        for i, frame in enumerate(self.frame_list):
            frame.new_label.configure(text=f"Sequence #{i+1}")


def change_appearance_mode_event(new_scaling: str):
    """Changes the theme of the app (Light, Dark, System)."""
    customtkinter.set_appearance_mode(new_scaling)


def new_frame():
    """Creates the new sequence frames"""
    app.frame_list.append(SeqFrame(master=app.sequences_frame, count=app.count))
    app.count += 1


root = customtkinter.CTk()
app = App(root)
root.mainloop()
