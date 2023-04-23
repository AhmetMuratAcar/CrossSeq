import customtkinter
import webbrowser
from PIL import Image
from functools import partial
from SequenceClass import Sequence
from script import seq_decompose

DEL_IMAGE = customtkinter.CTkImage(light_image=Image.open("Images/trash_(light_mode).png"),
                                   dark_image=Image.open("Images/trash_(dark_mode).png"),
                                   size=(30, 30))

UPLOAD_IMAGE = customtkinter.CTkImage(light_image=Image.open("Images/File_Upload_(dark_mode).png"),
                                      dark_image=Image.open("Images/File_Upload_(dark_mode).png"),
                                      size=(20, 20))

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
            app.toolbar_frame.seq_list_labels[-1].destroy()
            app.toolbar_frame.seq_list_labels.pop()
            app.count = len(app.frame_list) + 1
            app.update_labels()


class ToolBar:
    """Constructs the toolbar on the right side of the window."""

    def __init__(self, master):
        self.seq_list_labels = []

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
        main_seq_label.focus_set()
        main_seq_label.bind(sequence="<Button-1>", command=partial(pop_out, -1))
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

        # File upload button
        self.fileButton = customtkinter.CTkButton(self.toolbar_frame,
                                                  text="File Upload",
                                                  image=UPLOAD_IMAGE,
                                                  command=self.upload)
        self.fileButton.pack(pady=10)

        # Submit button
        self.submitButton = customtkinter.CTkButton(self.toolbar_frame,
                                                    fg_color="#FA8072",
                                                    hover_color="#CD5C5C",
                                                    text_color=("gray10", "gray90"),
                                                    text="Submit",
                                                    command=submission)
        self.submitButton.pack(padx=20, pady=10, side="bottom")

    def seq_list_update(self, count):
        new_label = customtkinter.CTkLabel(master=self.seq_list,
                                           text=f"Sequence #{count}")
        new_label.focus_set()
        new_label.bind(sequence="<Button-1>", command=partial(pop_out, count))
        new_label.pack()
        self.seq_list_labels.append(new_label)

    def upload(self):
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
        self.pop_out_window = None

        # Bringing the toolbar frame into the main window
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
        """Updates all sequence labels after a sequence frame is deleted."""
        for i, frame in enumerate(self.frame_list):
            frame.new_label.configure(text=f"Sequence #{i + 1}")


def pop_out(position, *args):  # I have no idea why *args is needed but when I take it out everything breaks.
    """On press of a sequence list label, creates a pop out window of the corresponding sequence frame."""

    # Checks if there is already a pop out window.
    if app.pop_out_window is not None:
        app.pop_out_window.focus()
        return

    top = customtkinter.CTkToplevel()
    top.geometry("650x250")
    app.pop_out_window = top

    # Setting title of pop out window.
    if position == -1:
        seq_name = "Main Sequence"
    else:
        seq_name = f"Sequence #{position}"
    top.title(seq_name)

    # Creating and placing the copies.
    label_copy = customtkinter.CTkLabel(master=top, text=seq_name, padx=20)
    label_copy.pack(anchor="w")
    textbox_copy = customtkinter.CTkTextbox(master=top)
    textbox_copy.pack(padx=20, pady=(0, 20), side="left", anchor="w", fill="both", expand="true")

    if position == -1:
        textbox_copy.insert("0.0", app.main_frame.main_seq_text.get("0.0", "end"))
    else:
        textbox_copy.insert("0.0", app.frame_list[position-1].new_seq_box.get("0.0", "end"))

    # Updating the text box in the main window from changes in the pop out window.
    def update_main_window(event):
        if position == -1:
            app.main_frame.main_seq_text.delete("0.0", "end")
            app.main_frame.main_seq_text.insert("0.0", textbox_copy.get("0.0", "end"))
        else:
            app.frame_list[position - 1].new_seq_box.delete("0.0", "end")
            app.frame_list[position - 1].new_seq_box.insert("0.0", textbox_copy.get("0.0", "end"))

    textbox_copy.bind("<KeyRelease>", update_main_window)

    # Resetting the presence of a pop out window.
    def reset_top(event):
        app.pop_out_window = None

    top.bind("<Destroy>", func=reset_top)


def change_appearance_mode_event(new_scaling: str):
    """Changes the theme of the app (Light, Dark, System)."""
    customtkinter.set_appearance_mode(new_scaling)


def new_frame():
    """Creates the new sequence frames and updates the sequence list."""
    app.frame_list.append(SeqFrame(master=app.sequences_frame, count=app.count))
    app.toolbar_frame.seq_list_update(count=app.count)
    app.count += 1


def submission():
    """Creates the main/compared Sequence class objects. Then creates the pop out window in which the results are
    shown."""

    app.seq_list = []
    del_indexes = []

    # Verifying correct submission format
    for frame in app.frame_list:
        curr_text = frame.new_seq_box.get("0.0", "end")
        if curr_text.startswith(">"):
            app.seq_list.append(curr_text)
        else:
            del_indexes.append(app.frame_list.index(frame))

    # Deleting incorrectly formatted submissions
    def submission_del(indexes):
        for index in indexes:
            app.frame_list[index].new_text_frame.destroy()
            app.frame_list[index] = None
            app.toolbar_frame.seq_list_labels[-1].destroy()
            app.toolbar_frame.seq_list_labels.pop()
            app.count = len(app.frame_list) + 1
        app.frame_list = [i for i in app.frame_list if i is not None]  # It works I guess.
        app.count = len(app.frame_list) + 1
        app.update_labels()
    submission_del(del_indexes)

    # Create Sequence class objects and append them into app.seq_list.
    app.main_seq = Sequence()
    main_seq_submission = app.main_frame.main_seq_text.get("0.0", "end")
    app.main_seq.parse_input(main_seq_submission)
    print(app.main_seq.completeFile)

    app.seq_objects = []
    for seq in app.seq_list:
        seq_object = Sequence()
        app.seq_objects.append(seq_object)
        seq_object.parse_input(seq)  # Write function in SequenceClass that parses the user input

    seq_decompose()

    # Creates pop out window containing results (2 tabs). For item in app.seq_list create a frame in which the result
    # for that sequence will be displayed.

    # Maybe use the tkinter text widget and the tag_add and tag_config commands for creating the highlighted text.


root = customtkinter.CTk()
app = App(root)
root.mainloop()
