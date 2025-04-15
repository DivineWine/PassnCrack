import os
import time
import random as rd

os.system('clear')

class PasswordGenerator:
    def __init__(self):
        self.character_numbers = [str(x) for x in range(10)]
        self.character_letters = list("abcdefghijklmnopqrstuvwxyz")
        self.character_specials = [
            "!", "'", "^", "#", "%", "½", "&", "¾", "$", "£", "/", "{", "[", "(", "]", ")",
            "=", "}", "<", ">", "|", "@", "~", ",", ";", "×", "-", "_"
        ]
        self.passwords = []
        self.selected_characters = []

    def display_menu(self):
        print("""
██████╗  █████╗ ███████╗███╗   ██╗ ███╗   ██╗ ██████╗██████╗  █████╗  ██████╗╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝████╗  ██║████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝█╝██║ ██╔╝
██████╔╝███████║███████╗██╔██╗ ██║██╔██╗ ██║██║     ██████╔╝███████║██║     █ █████╔╝ 
██╔═══╝ ██╔══██║╚════██║██║╚██╗██║██║╚██╗██║██║     ██╔═══╝ ██╔══██║██║     █ ██╔═██╗ 
██║     ██║  ██║███████║██║ ╚████║██║ ╚████║╚██████╗██║     ██║  ██║╚██████╗ ╗██║  ██╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╝╚═╝  ╚═╝
==============================
Educational Purposes ONLY !!!
==============================

==============================
  PASSWORD CHARACTER OPTIONS
==============================
1) Letters only
2) Numbers only
3) Special characters only
4) Letters + Numbers
5) Letters + Special characters
6) Numbers + Special characters
7) Letters + Numbers + Special characters (default)
""")
        choice = input("Select an option (1-7): ").strip()
        self.set_character_set(choice)

    def set_character_set(self, choice):
        match choice:
            case "1":
                self.selected_characters = self.character_letters
            case "2":
                self.selected_characters = self.character_numbers
            case "3":
                self.selected_characters = self.character_specials
            case "4":
                self.selected_characters = self.character_letters + self.character_numbers
            case "5":
                self.selected_characters = self.character_letters + self.character_specials
            case "6":
                self.selected_characters = self.character_numbers + self.character_specials
            case "7" | _:
                self.selected_characters = (
                    self.character_letters + self.character_numbers + self.character_specials
                )
                print("ℹ️ Defaulting to: Letters + Numbers + Special characters.")

    def ask_password_length(self):
        while True:
            user_input = input("How many characters should each password have? >>> ")
            if user_input.isdigit():
                return int(user_input)
            else:
                print("⚠️ Please enter a valid number.")

    def ask_password_count(self):
        user_input = input("How many passwords do you want to generate? (Press Enter for 1000) >>> ")
        if user_input.strip() == "":
            return 1000
        try:
            return int(user_input)
        except ValueError:
            print("⚠️ Invalid input! Defaulting to 1000 passwords.")
            return 1000

    def generate_passwords(self):
        if not self.selected_characters:
            self.selected_characters = (
                self.character_letters + self.character_numbers + self.character_specials
            )

        password_count = self.ask_password_count()
        password_length = self.ask_password_length()

        self.passwords = []

        for _ in range(password_count):
            password = [rd.choice(self.selected_characters) for _ in range(password_length)]
            self.passwords.append(''.join(password))

        print(f"\n✅ Successfully generated {len(self.passwords)} passwords.")

    def write_to_file(self):
        with open("passwords.txt", "a") as file:
            for password in self.passwords:
                file.write(password + "\n")
        print("📁 All passwords have been saved to 'passwords.txt'.")

    def move_file_to_folder(self):
        os.system(f"mv passwords.txt {self.folder_name}")
        print(f"📁 'passwords.txt' has been moved to the folder '{self.folder_name}'.")

    def create_and_zip_folder(self):
        self.folder_name = input("Enter a name for the folder >>> ")
        os.system(f"mkdir -p {self.folder_name}")
        print("📂 Folder created successfully.")
        time.sleep(0.5)

        compress = input("Do you want to compress the folder into a .zip file? [y/n] >>> ").strip().lower()
        if compress == "y":
            os.system(f"zip -r {self.folder_name}.zip {self.folder_name}")
            time.sleep(0.5)
            print(f"✅ Folder '{self.folder_name}' has been zipped successfully.")
        elif compress == "n":
            print("⏭️ Skipping zip process.")
        else:
            print("⚠️ Invalid input! Zip operation skipped.")

# Main usage
if __name__ == "__main__":
    app = PasswordGenerator()
    app.display_menu()
    app.generate_passwords()
    app.write_to_file()
    app.create_and_zip_folder()
    app.move_file_to_folder()

