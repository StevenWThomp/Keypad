#!/usr/bin/env python3
# final_keypad
# Steven Thompson
# 12/12/2017

""" Keypad that allows for input of a 7 digit password """

from tkinter import *


class Application(Frame):
    """ GUI frame with a text box and keypad """

    def __init__(self, master):
        """ initialize the frame """
        super(Application, self).__init__(master)
        self.grid()
        self.FONT = ("times bold", "20")
        self.PASSWORD = ("1111111")
        self.current_digit = 0
        self.create_widgets()

    def create_widgets(self):
        """ Create the buttons for the keypad """

        # create and disable text box
        self.txt_prompt = Text(self, width=10, height=1, font=self.FONT)
        self.txt_prompt.grid(row=0, column=0, columnspan=3, sticky=W + E)
        self.txt_prompt.config(state=DISABLED)

        # Create row 1 buttons
        self.btn_seven = Button(self, text="7", font=self.FONT,
                                command=lambda: self.digit("7"))
        self.btn_seven.grid(row=1, column=0, sticky=W + E)

        self.btn_eight = Button(self, text="8", font=self.FONT,
                                command=lambda: self.digit("8"))
        self.btn_eight.grid(row=1, column=1, sticky=W + E)

        self.btn_nine = Button(self, text="9", font=self.FONT,
                               command=lambda: self.digit("9"))
        self.btn_nine.grid(row=1, column=2, sticky=W + E)

        # Create row 2 buttons
        self.btn_four = Button(self, text="4", font=self.FONT,
                               command=lambda: self.digit("4"))
        self.btn_four.grid(row=2, column=0, sticky=W + E)

        self.btn_five = Button(self, text="5", font=self.FONT,
                               command=lambda: self.digit("5"))
        self.btn_five.grid(row=2, column=1, sticky=W + E)

        self.btn_six = Button(self, text="6", font=self.FONT,
                              command=lambda: self.digit("6"))
        self.btn_six.grid(row=2, column=2, sticky=W + E)

        # Create row 3 buttons
        self.btn_one = Button(self, text="1", font=self.FONT,
                              command=lambda: self.digit("1"))
        self.btn_one.grid(row=3, column=0, sticky=W + E)

        self.btn_two = Button(self, text="2", font=self.FONT,
                              command=lambda: self.digit("2"))
        self.btn_two.grid(row=3, column=1, sticky=W + E)

        self.btn_three = Button(self, text="3", font=self.FONT,
                                command=lambda: self.digit("3"))
        self.btn_three.grid(row=3, column=2, sticky=W + E)

        # Create 0, clear, and unlock buttons
        self.btn_zero = Button(self, text="0", font=self.FONT,
                               command=lambda: self.digit("0"))
        self.btn_zero.grid(row=4, column=0, sticky=W + E)

        self.btn_clear = Button(self, text="Clear", font=self.FONT,
                                command=self.clear)
        self.btn_clear.grid(row=4, column=1, columnspan=2, sticky=W + E)

        self.btn_unlock = Button(self, text="Unlock", font=self.FONT,
                                 command=self.unlock)
        self.btn_unlock.grid(row=5, column=0, columnspan=3, sticky=W + E)

        # updates the buttons
        # Will also disable text box and buttons if more than 7 digits are entered

    def digit(self, new_digit):
        self.prompt = self.txt_prompt.get(0.0, END).strip()
        if len(self.prompt) >= 7:
            self.disable_buttons()
            self.txt_prompt.config(state=DISABLED)
        else:
            self.current_digit = new_digit
            self.update_box()

        # This allows the user to press any button on the keypad to start typing again
        # after hitting the unlock button
        if self.prompt == "ERROR" or self.prompt == "UNLOCKED":
            self.txt_prompt.config(state=NORMAL)
            self.current_digit = new_digit
            self.txt_prompt.delete(0.0, END)
            self.txt_prompt.insert(0.0, self.current_digit)
            self.enable_buttons()

    # updates the text box with input from the buttons
    def update_box(self):
        self.txt_prompt.config(state=NORMAL)
        self.txt_prompt.insert(END, self.current_digit)

    # sets parameters for whether the keypad gets unlocked
    def unlock(self):
        self.prompt = self.txt_prompt.get(0.0, END).strip()
        self.txt_prompt.config(state=NORMAL)
        if self.prompt == self.PASSWORD:
            self.txt_prompt.delete(0.0, END)
            self.txt_prompt.insert(0.0, "UNLOCKED")
            self.txt_prompt.config(state=DISABLED)
        else:
            self.txt_prompt.delete(0.0, END)
            self.txt_prompt.insert(0.0, "ERROR")
            self.txt_prompt.config(state=DISABLED)
        self.enable_buttons()

    # clears the text box when corresponding button is pressed
    def clear(self):
        self.txt_prompt.config(state=NORMAL)
        self.txt_prompt.delete(0.0, END)
        self.enable_buttons()

    # Enables all of the number buttons when called on
    def enable_buttons(self):
        self.btn_zero.config(state=NORMAL)
        self.btn_one.config(state=NORMAL)
        self.btn_two.config(state=NORMAL)
        self.btn_three.config(state=NORMAL)
        self.btn_four.config(state=NORMAL)
        self.btn_five.config(state=NORMAL)
        self.btn_six.config(state=NORMAL)
        self.btn_seven.config(state=NORMAL)
        self.btn_eight.config(state=NORMAL)
        self.btn_nine.config(state=NORMAL)

        # Disables all of the number buttons when called on

    def disable_buttons(self):
        self.btn_zero.config(state=DISABLED)
        self.btn_one.config(state=DISABLED)
        self.btn_two.config(state=DISABLED)
        self.btn_three.config(state=DISABLED)
        self.btn_four.config(state=DISABLED)
        self.btn_five.config(state=DISABLED)
        self.btn_six.config(state=DISABLED)
        self.btn_seven.config(state=DISABLED)
        self.btn_eight.config(state=DISABLED)
        self.btn_nine.config(state=DISABLED)


root = Tk()
# Set attributes
root.title("Keypad")

# Create framework
app = Application(root)
app.grid()

# Kick off the event handler loop
root.mainloop()