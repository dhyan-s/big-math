# import required libraries
import customtkinter as ctk
from tkinter import *
import pyperclip

# set theme and appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# set up app and widgets
class SimpleCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # screen coordinates
        self.appWidth = 360
        self.appHeight = 490

        self.widgetWidth = self.appWidth/3
        self.widgetHeight= self.appHeight/5

        # set up window
        self.title("BigMath - Simple Calculator")
        self.geometry(f"{self.appWidth}x{self.appHeight+145}")

        # calculator interface
        self.operationScreen = ctk.CTkEntry(self, placeholder_text="Enter any operation", width=self.appWidth, height=75, border_color="black", corner_radius=12, font=("Helvetica", 22))
        self.operationScreen.grid(row=0, column=0, columnspan=3)

        # create copy button that copies the result to clipboard
        self.copyButton = ctk.CTkButton(self.operationScreen, text="Copy", width=10, command=self.copyResult)
        self.copyButton.grid(row=0, column=0, sticky=NE, pady=5, padx=5)

        # create calculator buttons
        self.one = ctk.CTkButton(self, text="1", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black",  border_spacing=2, corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(1))
        self.two = ctk.CTkButton(self, text="2", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2, corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(2))
        self.three = ctk.CTkButton(self, text="3", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(3))
        self.four = ctk.CTkButton(self, text="4", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(4))
        self.five = ctk.CTkButton(self, text="5", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(5))
        self.six = ctk.CTkButton(self, text="6", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(6))
        self.seven = ctk.CTkButton(self, text="7", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(7))
        self.eight = ctk.CTkButton(self, text="8", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(8))
        self.nine = ctk.CTkButton(self, text="9", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(9))
        self.zero = ctk.CTkButton(self, text="0", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry(0))

        self.add = ctk.CTkButton(self, text="+", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry("+"))
        self.subtract = ctk.CTkButton(self, text="-", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry("-"))
        self.multiply = ctk.CTkButton(self, text="*", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry("*"))
        self.divide = ctk.CTkButton(self, text="/", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20), command=lambda: self.setValuesEntry("/"))
        self.equal = ctk.CTkButton(self, text="=", width=self.widgetWidth, height=self.widgetHeight, border_width=5, border_color="black", border_spacing=2,corner_radius=12, text_color="black", font=("Rockwell", 20))

        self.clear = ctk.CTkButton(self, text="C", width=self.appWidth-120, height=70, border_width=5, border_color="black",  corner_radius=12, text_color="black", font=("Rockwell", 20), command=self.clearValuesEntry)
        self.shiftComplexCalc = ctk.CTkButton(self, text="Complex\nCalculator", width=self.widgetWidth, height=70, border_width=5, border_color="black",  corner_radius=12, text_color="black", font=("Rockwell", 15), command=self.loadComplexCalc)

        self.one.grid(row=1, column=0)
        self.two.grid(row=1, column=1)
        self.three.grid(row=1, column=2)
        self.four.grid(row=2, column=0)
        self.five.grid(row=2, column=1)
        self.six.grid(row=2, column=2)
        self.seven.grid(row=3, column=0)
        self.eight.grid(row=3, column=1)
        self.nine.grid(row=3, column=2)
        self.zero .grid(row=5, column=0)  

        self.add.grid(row=4, column=0)
        self.subtract.grid(row=4, column=1)
        self.multiply.grid(row=4, column=2)
        self.divide.grid(row=5, column=2)
        self.equal.grid(row=5, column=1)

        self.clear.grid(row=6, column=0, columnspan=2)
        self.shiftComplexCalc.grid(row=6, column=2)

    def setValuesEntry(self, char):
        self.presentText = str(self.operationScreen.get())
        self.operationScreen.delete(0, END)
        self.operationScreen.insert(END, self.presentText + str(char))

    
    def clearValuesEntry(self):
        self.operationScreen.delete(0, END)

    def loadComplexCalc(self):
        self.destroy()
        from complex_calc import ComplexCalculator

    def copyResult(self):
        self.textCopy = str(self.operationScreen.get())
        pyperclip.copy(self.textCopy)

app = SimpleCalculator()
app.mainloop()