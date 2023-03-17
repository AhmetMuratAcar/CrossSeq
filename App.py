import tkinter
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


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("DNA Comparer")
        # self.geometry(f"{1400}x{880}")

        # Theme changing menu. Position this in the top right.
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self,
                                                                values=["System", "Dark", "Light"],
                                                                fg_color=("gray90", "gray20"),
                                                                button_color=("gray90", "gray20"),
                                                                button_hover_color=("gray75", "gray28"),
                                                                text_color=("gray10", "gray90"),
                                                                anchor="center",
                                                                command=change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=2, column=1, padx=20, sticky="E")
        # self.appearance_mode_menu.place(rely=1.0, relx=1.0, anchor="e")

        # Instruction hyperlink button
        self.instruction_link_button = customtkinter.CTkButton(self,
                                                               text="Instructions and Examples",
                                                               command=instruction_callback)
        self.instruction_link_button.grid(row=0, column=0, padx=20, pady=10)

        # Text entry box
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter your main sequence")
        self.entry.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="wens")

        # Submission button
        self.submitButton = customtkinter.CTkButton(self,
                                                    fg_color="#FA8072",
                                                    hover_color="#CD5C5C",
                                                    text_color=("gray10", "gray90"),
                                                    text="Submit",
                                                    command=submission)
        self.submitButton.grid(row=2, column=0, padx=20, pady=10, sticky="w")


if __name__ == "__main__":
    app = App()
    app.mainloop()
