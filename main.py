"""A program to register using unique-ID, username and password and store in a text file.
Then to login using the registered unique-ID. It can also be used to generate 7-9 digit password and has the ability
 to store the generated password in a text file."""

from tkinter import *
import time
import os
import string
import random


class PasswordManager:
    """This class is used for registeration and login purpose. It stores the username and password in a text file
    under the name of the unique id."""

    # __init__() to store unique id, name, password and also a variable to check whether the text file exists or not.
    def __init__(self, unique_id=None, name=None, password=None, accept_id=None):
        self.username = name
        self.password = password
        self.unique_id = unique_id
        self.check_id = accept_id

    def App_starting_page(self):
        """To open the new window and display "Password manager" App."""
        password_manager_app = Tk()
        Object_for_background = AppBackground(
            password_manager_app, 400, 240, "Password Manager", "turquoise1"
        )
        Object_for_background.app_title()
        Object_for_background.app_color()
        Object_for_background.app_geometry()
        Object_for_background.app_icon()
        self.main_window(password_manager_app)
        password_manager_app.mainloop()

    def main_window(self, App):
        """To display the main functions in the app."""
        Label(
            App,
            text="Select Your Choice",
            bg="Pink",
            width="400",
            height="2",
            font=("Times", 20, "italic"),
        ).pack()
        Label(App, text="", bg="turquoise1").pack()

        Button(
            App,
            text="Login",
            height="1",
            width="25",
            bg="Pink",
            command=lambda: self.app_call(App, 1),
        ).pack()
        Label(App, text="", bg="turquoise1").pack()

        Button(
            App,
            text="Register",
            height="1",
            width="25",
            bg="Pink",
            command=lambda: self.app_call(App, 2),
        ).pack()
        Label(App, text="", bg="turquoise1").pack()

        Button(
            App,
            text="QUIT",
            height="1",
            width="10",
            bg="Red",
            fg="White",
            font=("Times", 10, "bold"),
            command=lambda: self.app_call(App, 4),
        ).pack()
        Label(App, text="", bg="turquoise1").pack()

    def app_call(self, App_window, key):
        """To destroy the current page and open the next page."""
        if key == 1:
            # Closes the current window and opens the "Login page" window.
            App_window.destroy()
            self.login_page()

        elif key == 2:
            # Closes the current window and opens the "Register page" window.
            App_window.destroy()
            self.register_window()

        elif key == 3:
            # Closes the info window and opens the starting page of the "Password Manager" app.
            App_window.destroy()
            self.App_starting_page()

        elif key == 4:
            # Closes the current window and opens the starting page of the app.
            App_window.destroy()
            App_start_function()

        else:
            # Prints "KeyError in the console if the key passed isn't correct."
            print(KeyError)

    def register_window(self):
        """To open the "Register window" app and also used for inputting unique-ID, username and password."""
        register_window = Tk()
        Object_for_background = AppBackground(
            register_window, 400, 400, "Register", "White"
        )
        Object_for_background.app_title()
        Object_for_background.app_color()
        Object_for_background.app_geometry()
        Object_for_background.app_icon()

        Label(
            register_window,
            text="Please Register",
            width="400",
            height="2",
            bg="Blue",
            fg="White",
            font=("Times", 17, "bold"),
        ).pack()
        Label(register_window, text="", bg="White").pack()

        self.unique_id = StringVar(register_window)

        unique_id_label = Label(
            register_window, text="Unique ID", bg="White", fg="Black", font=("", 13)
        ).pack()
        unique_id_entry = Entry(register_window, textvariable=self.unique_id)
        unique_id_entry.pack()

        Label(register_window, text="", bg="White").pack()

        self.username = StringVar(register_window)

        username_label = Label(
            register_window, text="Username", bg="White", fg="Black", font=("", 13)
        ).pack()
        username_entry = Entry(register_window, textvariable=self.username, width="30")
        username_entry.pack()

        Label(register_window, text="", bg="White").pack()

        self.password = StringVar(register_window)

        password_label = Label(
            register_window, text="Password", bg="White", fg="Black", font=("", 13)
        ).pack()
        password_entry = Entry(
            register_window, textvariable=self.password, width="30", show="*"
        )
        password_entry.pack()

        Label(register_window, text="", bg="White").pack()

        Button(
            register_window,
            text="Register",
            bg="Blue",
            fg="White",
            height="1",
            font=("Times", 10, "bold"),
            command=lambda: self.store_info(register_window),
        ).pack()

        Label(register_window, text="", bg="White").pack()

        Button(
            register_window,
            text="QUIT",
            height="1",
            width="7",
            bg="Red",
            fg="White",
            font=("Times", 10, "bold"),
            command=lambda: self.app_call(register_window, 4),
        ).pack()

    def login_page(self):
        """To open the "Login page" window.It is also used for inputting the unique-ID and to display the
        corresponding username and password."""
        login_window = Tk()
        Object_for_background = AppBackground(login_window, 300, 310, "Login", "White")
        Object_for_background.app_title()
        Object_for_background.app_color()
        Object_for_background.app_geometry()
        Object_for_background.app_icon()

        Label(
            login_window,
            text="Check Unique ID",
            width="400",
            height="2",
            bg="Blue",
            fg="White",
            font=("Times", 17, "bold"),
        ).pack()
        Label(login_window, text="", bg="White").pack()

        self.check_id = StringVar(login_window)

        unique_id_label = Label(
            login_window, text="Unique ID", bg="White", fg="Black", font=("", 13)
        ).pack()
        unique_id_entry = Entry(login_window, textvariable=self.check_id)
        unique_id_entry.pack()

        Label(login_window, text="", bg="White").pack()
        Button(
            login_window,
            text="Show",
            bg="Blue",
            fg="White",
            height="1",
            font=("Times", 10, "bold"),
            command=lambda: self.show_info(login_window),
        ).pack()

        Label(login_window, text="", bg="White").pack()

        Button(
            login_window,
            text="QUIT",
            bg="Red",
            fg="White",
            height="1",
            font=("Times", 10, "bold"),
            command=lambda: self.app_call(login_window, 3),
        ).pack()
        Label(login_window, text="", bg="white").pack()

    def store_info(self, registered_window):
        """To store the username and password from the user in a text file named with it's unique-ID."""
        Label(registered_window, text="", bg="White").pack()
        Label(
            registered_window,
            text="Registration Success!",
            bg="Blue",
            fg="White",
            font=("", 15, "underline"),
        ).pack()

        unique_id_info = self.unique_id.get()
        username_info = self.username.get()
        password_info = self.password.get()

        file = open(unique_id_info + ".txt", "w")
        file.write(username_info + "\n")
        file.write(password_info)
        time.sleep(3)
        file.close()
        registered_window.mainloop()

    def show_info(self, login_window):
        """To display the username and password using unique-ID from the text file."""
        id_check = self.check_id.get()

        if os.path.isfile("{}.txt".format(id_check)):
            # Checks if the required file exists in the directory which was saved earlier.
            show_info_window = Tk()
            Object_for_background = AppBackground(
                show_info_window, 330, 240, "User Info", "Blue"
            )
            Object_for_background.app_title()
            Object_for_background.app_color()
            Object_for_background.app_geometry()
            Object_for_background.app_icon()
            Label(
                show_info_window,
                text="User Info",
                width="330",
                height="2",
                bg="Blue",
                fg="White",
                font=("Times", 18, "italic"),
            ).pack()
            Label(login_window, text="", bg="White").pack()

            file = open("{}.txt".format(id_check), "r")
            read_file = file.read()
            display_data = read_file.split("\n")
            Label(show_info_window, text="", bg="Blue").pack()
            Label(
                show_info_window,
                text="Your Details: ",
                bg="White",
                fg="Blue",
                width="330",
                font=("Times", 10, "underline"),
            ).pack()
            Label(show_info_window, text="", bg="White", fg="Blue", width="330").pack()
            Label(
                show_info_window,
                text="Username : " + display_data[0],
                bg="White",
                fg="Blue",
                width="330",
            ).pack()
            Label(
                show_info_window,
                text="Password : " + display_data[1],
                bg="White",
                fg="Blue",
                width="330",
            ).pack()
            Label(show_info_window, text="", bg="White", height="1", width="330").pack()
            Label(
                show_info_window, text="", bg="Blue", fg="Blue", height="1", width="330"
            ).pack()
            Button(
                show_info_window,
                text="QUIT",
                bg="Red",
                fg="White",
                height="1",
                font=("Times", 10, "bold"),
                command=show_info_window.destroy,
            ).pack()
            show_info_window.mainloop()

        elif len(id_check) == 0:
            # Checks if the unique_ID is an empty entry/string. If so it prints a warning.
            Label(login_window, text="", bg="White").pack()
            Label(
                login_window,
                text="No entry given!",
                fg="Red",
                width="30",
                font=("", 10, "bold underline"),
            ).pack()

        else:
            # If not any, then it warns: "Unique_id doesn't exist".
            Label(login_window, text="", bg="White").pack()
            Label(
                login_window,
                text="Unique-ID does not exist!",
                fg="Red",
                width="30",
                font=("", 10, "bold underline"),
            ).pack()

        login_window.mainloop()


class PasswordGenerator:
    """This class is used for generating 7-9 digit password and to store the generated password in a text file.."""

    def App_opening_page(self):
        """To open the new tab and to call the "AppBackground" class for designing the front-end view."""
        password_generator_app = Tk()
        Object_for_background = AppBackground(
            password_generator_app, 300, 340, "Password Generator", "pale turquoise"
        )
        Object_for_background.app_title()
        Object_for_background.app_color()
        Object_for_background.app_geometry()
        Object_for_background.app_icon()
        self.Pass_Gen_window(password_generator_app)
        password_generator_app.mainloop()

    def Pass_Gen_window(self, password_generator_app):
        """To display the opening tab of 'Password Generator'."""
        Label(
            password_generator_app,
            text="Select Your Choice",
            bg="khaki",
            width="400",
            height="2",
            font=("Times", 20, "italic underline"),
        ).pack()
        Label(password_generator_app, text="", bg="pale turquoise").pack()

        Button(
            password_generator_app,
            text="7 Digit Password",
            height="2",
            width="15",
            bg="khaki",
            font=("Times", 10, "bold"),
            command=lambda: self.print_passcode(7),
        ).pack()
        Label(password_generator_app, text="", bg="pale turquoise").pack()

        Button(
            password_generator_app,
            text="8 Digit Password",
            height="2",
            width="15",
            bg="khaki",
            font=("Times", 10, "bold"),
            command=lambda: self.print_passcode(8),
        ).pack()
        Label(password_generator_app, text="", bg="pale turquoise").pack()

        Button(
            password_generator_app,
            text="9 Digit Password",
            height="2",
            width="15",
            bg="khaki",
            font=("Times", 10, "bold"),
            command=lambda: self.print_passcode(9),
        ).pack()
        Label(password_generator_app, text="", bg="pale turquoise").pack()

        Button(
            password_generator_app,
            text="QUIT",
            height="1",
            width="5",
            bg="red",
            fg="White",
            font=("Times", 10, "bold"),
            command=lambda: self.call_function(password_generator_app),
        ).pack()
        Label(password_generator_app, text="", bg="pale turquoise").pack()

    def print_passcode(self, key):
        """To display the generated password in the next window."""
        Show_password = Tk()
        Object_for_background = AppBackground(
            Show_password, 400, 270, "Generated Passcode", "Steelblue"
        )
        Object_for_background.app_title()
        Object_for_background.app_color()
        Object_for_background.app_geometry()
        Object_for_background.app_icon()

        # To store various characters and symbols in an variable, we use password as a private variable.
        __password = string.ascii_letters + string.digits + string.punctuation
        random_password = "".join(random.choices(__password, k=key))

        Label(
            Show_password,
            text="{} Digit Password".format(key),
            bg="Olivedrab1",
            width="400",
            height="2",
            font=("Times", 15, "italic underline"),
        ).pack()
        Label(Show_password, text="", bg="Steelblue").pack()

        print(random_password)

        Label(
            Show_password, text=random_password, font=("Calibri", 30, "bold"), bg="snow"
        ).pack()
        Label(Show_password, text="", bg="Steelblue").pack()
        Button(
            Show_password,
            text="Save Password as '.txt' file",
            height="1",
            width="20",
            fg="Black",
            bg="Olivedrab1",
            font=("Times", 10, "bold"),
            command=lambda: self.save_password(Show_password, random_password, key),
        ).pack()
        Label(Show_password, text="", bg="Steelblue").pack()
        Button(
            Show_password,
            text="QUIT",
            height="1",
            width="10",
            fg="White",
            bg="Red",
            font=("Times", 10, "bold"),
            command=Show_password.destroy,
        ).pack()
        Label(Show_password, text="", bg="Steelblue").pack()

        Show_password.mainloop()

    def save_password(self, password_window, password, key):
        """To store the generated password as a text file. """
        file = open("{} Digit password.txt".format(key), "w")
        file.write("Password: {}".format(password))
        time.sleep(3)
        file.close()
        Label(
            password_window,
            text="Note: Password stored as '{} Digit password.txt'".format(key),
            bg="snow",
            fg="Green",
            font="italic",
        ).pack()
        password_window.mainloop()

    def call_function(self, password_generator_app):
        """To destroy current window and to start the opening page."""
        password_generator_app.destroy()
        App_start_function()


class AppBackground(PasswordManager, PasswordGenerator):
    """This is the main class. It is used for the app layout and other nessesary front-end work. This class inherits
    from classes 'PasswordManager' and 'PasswordGenerator' respectively. This type of inheritance is known as
    'Hierarcical Inheritance'."""

    # __init__() is a constructor used for initializing global variable in order to use them in any part of this class.
    def __init__(
        self,
        app_object,
        app_width=330,
        app_height=260,
        app_title="Password Generator And Manager",
        app_color="blue",
        app_icon="Icon.ico",
    ):
        # The glocal variables in other classes are inherited using the super() function.
        super().__init__(self)
        self.title = app_title
        self.app = app_object
        self.width = app_width
        self.height = app_height
        self.icon = app_icon
        self.color = app_color

    def app_geometry(self):
        """To modify the size of our app window and also to display them in the center of the display screen."""
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (self.width / 2)
        y_coordinate = (screen_height / 2) - (self.height / 2)
        self.app.geometry(
            "%dx%d+%d+%d" % (self.width, self.height, x_coordinate, y_coordinate)
        )
        self.app.resizable(False, False)

    def app_title(self):
        """To name our app and displaying it in the app-window."""
        self.app.title("{}".format(self.title))

    def app_icon(self):
        """To display the icon of our app. """
        self.app.iconbitmap("{}".format(self.icon))

    def app_color(self):
        """To beautify the front-end using plethora of color option"""
        self.app.config(bg="{}".format(self.color))

    def starting_page(self):
        """To display the starting page of the app."""
        Label(
            self.app,
            text="Select Your Choice",
            bg="Yellow",
            width="400",
            height="2",
            font=("Times", 25, "bold italic underline"),
        ).pack()
        Label(self.app, text="", bg="blue").pack()

        Button(
            self.app,
            text="Generate Password",
            height="2",
            width="30",
            bg="White",
            command=lambda: self.app_call_function(1),
        ).pack()
        Label(self.app, text="", bg="blue").pack()

        Button(
            self.app,
            text="Password Manager",
            height="2",
            width="30",
            bg="White",
            command=lambda: self.app_call_function(2),
        ).pack()
        Label(self.app, text="", bg="blue").pack()

        Button(
            self.app,
            text="QUIT",
            height="1",
            width="5",
            bg="Red",
            fg="white",
            font=("Times", 10, "bold"),
            command=self.app.destroy,
        ).pack()
        Label(self.app, text="", bg="blue").pack()

    def app_call_function(self, key):
        """To close the first page of the app and move onto the next page."""
        if key == 1:
            # To destroy the starting page and open "password generator" window.
            self.app.destroy()
            self.App_opening_page()
        elif key == 2:
            # To destroy the starting page and open "password manager" window.
            self.app.destroy()
            self.App_starting_page()
        else:
            # Prints "KeyError" in console if key is not found.
            print(KeyError)


def App_start_function():
    """Function which is used to call 'AppBackground' class and assigning a variable to run the app in a loop until the
    user wishes."""
    App = Tk()
    AppBG_class_object = AppBackground(App)
    AppBG_class_object.app_geometry()
    AppBG_class_object.app_title()
    AppBG_class_object.app_icon()
    AppBG_class_object.app_color()
    AppBG_class_object.starting_page()
    App.mainloop()


# Calling the function 'App_start_function'
if __name__ == "__main__":
    App_start_function()