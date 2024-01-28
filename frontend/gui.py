# import required libraries
import customtkinter as ctk
from tkinter import *

# set up app
class MainWin(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # basic set up
        self.appWidth = 310
        self.appHeight = 100

        self.title("BigMath - Home")
        self.geometry(f"{self.appWidth}x{self.appHeight}")
        self.resizable(0, 0)

        # set up widgets
        ctk.CTkLabel(self, text="Choose a Calculator").grid(row=0, column=0, columnspan=2, pady=(10, 0))

        self.simpleCalc = ctk.CTkButton(self, text="Simple Calculator", command=self.openSimpleCalc)
        self.simpleCalc.grid(row=1, column=0, padx=(10,0))

        self.complexCalc = ctk.CTkButton(self, text="Complex Calculator", command=self.openComplexCalc)
        self.complexCalc.grid(row=1, column=1, padx=(10, 0))

    def openSimpleCalc(self):
        self.destroy()
        from .simple_calc import SimpleCalculator

    def openComplexCalc(self):
        self.destroy()
        from .complex_calc import ComplexCalculator

def run():
    app = MainWin()
    app.mainloop()