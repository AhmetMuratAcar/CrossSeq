import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("DNA Comparer")
        self.geometry(f"{1100}x{580}")

        # Theme changing menu. Position this in the top right.
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self,
                                                                values=["System", "Dark", "Light"],
                                                                fg_color=("gray90", "gray20"),
                                                                button_color=("gray90", "gray20"),
                                                                button_hover_color=("gray75", "gray28"),
                                                                text_color=("gray10", "gray90"),
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # Text entry box
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter your main sequence")
        self.entry.grid(row=3, column=1, columnspan=3, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # Submission button
        self.submitButton = customtkinter.CTkButton(self,
                                                    fg_color="#FA8072",
                                                    hover_color="#CD5C5C",
                                                    text_color=("gray10", "gray90"),
                                                    text="Submit",
                                                    command=self.submission)
        self.submitButton.grid(row=0, column=0, padx=20, pady=10)

    def change_appearance_mode_event(self, new_scaling: str):
        """Changes the theme of the app (Light, Dark, System)"""
        customtkinter.set_appearance_mode(new_scaling)

    def submission(self):
        # Should check if the s
        print("joe")


if __name__ == "__main__":
    app = App()
    app.mainloop()
