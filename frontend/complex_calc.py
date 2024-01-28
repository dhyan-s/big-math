# import required libraries
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import pyperclip

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# read text from result.txt
with open('result.txt', 'r') as file:
    # Read the content of the file and store it in a variable
    number = str(file.read())

numberLength = len(number)
chunkSize = 1000
chunkNumber = numberLength // chunkSize
chunkNumber-=1

current_chunk = 0
chunkArray = [
]

# gui app
class ComplexCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.appWidth = 1037
        self.appHeight = 730

        self.title("BigMath - Complex Calculator")
        self.geometry(f"{self.appWidth}x{self.appHeight}")
        self.resizable(0, 0)

        # creating divisons
        self.inputFrame = ctk.CTkScrollableFrame(self, width=430, height=650, bg_color="transparent", corner_radius=12, border_color="#ffffff", scrollbar_button_color="#2587be", scrollbar_button_hover_color="#2596be")
        self.inputFrame.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        self.transferOutputBtn = ctk.CTkButton(self, text="<<", width=60, height=40, text_color="#ffffff", corner_radius=12, font=("Helvetica", 22), command=self.transferOutput)
        self.transferOutputBtn.grid(row=0, column=1, padx=(20, 10), pady=(40, 0), sticky=N)

        self.outputFrame = ctk.CTkScrollableFrame(self, width=430, height=600, bg_color="transparent", corner_radius=12, border_color="#ffffff", scrollbar_button_color="#2587be", scrollbar_button_hover_color="#2596be")
        self.outputFrame.grid(row=0, column=2, padx=(10, 10), pady=(10, 0))

        self.changeCalc = ctk.CTkButton(self, text="Click here for simpler calculator", corner_radius=5, font=("Arial", 20), command=self.changeSimpleCalc)
        self.changeCalc.grid(row=1, column=1, columnspan=3)


        # define lists and default values for combobox
        self.operationList = ["+", "-", "*", "/ (unfinished)", "^", "√"]
        self.operationListDefaultVal = "+"

        self.additionalOperationList = ["Select an Option", "HCF", "LCM", "Factorials", "Trigonometry", "Logarithms"]
        self.additionalOperationListDefaultVal = "Select an Option"

        # create input text boxes and choose an operation using combobox
        self.inputText1 = ctk.CTkTextbox(self.inputFrame, width=425, height=175, font=("Helvetica", 20))
        self.inputText1.grid(row=0, column=0, pady=(0, 20), columnspan=3)

        self.operationComboBox = ctk.CTkComboBox(self.inputFrame, width=425, height=30, border_color="#2587be", values=self.operationList, font=("Arial", 15))
        self.operationComboBox.grid(row=1, column=0, pady=10, columnspan=3)
        self.operationComboBox.set(self.operationListDefaultVal)

        self.inputText2 = ctk.CTkTextbox(self.inputFrame, width=425, height=175, font=("Helvetica", 20))
        self.inputText2.grid(row=2, column=0, pady=(20, 0), columnspan=3)
        
        # create button to add more input fields
        self.addTextBoxBtn = ctk.CTkButton(self.inputFrame, text="+", width=420, fg_color="transparent", border_color="#2587be", border_width=1, corner_radius=2, font=("Arial", 20), command=self.createInputBox)
        self.addTextBoxBtn.grid(row=3, column=0, pady=(20, 0))

        # evaluate result based on given input
        self.evaluateBtn = ctk.CTkButton(self.inputFrame, text="Evaluate Result", corner_radius=6, font=("Arial", 20), command=self.loadFirstChunk)
        self.evaluateBtn.grid(row=4, column=0, pady=(15, 10), ipadx=4, ipady=3, columnspan=3)

        # creating output division under output frame
        self.outputText = ctk.CTkTextbox(self.outputFrame, width=425, height=550, activate_scrollbars=False, font=("Helvetica", 20))
        self.outputText.grid(row=0, column=0, columnspan=2)

        self.copyTextBtn = ctk.CTkButton(self.outputText, text="Copy", width=10, command=self.copyText)
        self.copyTextBtn.grid(row=0, column=0, sticky=NE, pady=5, padx=0)

        self.initialRow = 3

    # create more input fields
    def createInputBox(self):
        self.newOperatorDropdown = ctk.CTkComboBox(self.inputFrame, width=425, height=30, border_color="#2587be", values=self.operationList, font=("Arial", 15))
        self.newOperatorDropdown.grid(row=self.initialRow+1, column=0, pady=(20, 0), columnspan=3)
        self.newOperatorDropdown.set(self.operationListDefaultVal)

        self.newInputText = ctk.CTkTextbox(self.inputFrame, width=425, height=175, font=("Helvetica", 20))
        self.newInputText.grid(row=self.initialRow+2, column=0, pady=20, columnspan=3)

        self.addTextBoxBtn.grid(row=self.initialRow+3, column=0, pady=(15, 0))
        self.evaluateBtn.grid(row=self.initialRow+4)

        self.initialRow+=5


    # load the first chunk of the data(with 1000 characters) on clicking evaluate button
    def loadFirstChunk(self):
        messagebox.showwarning("Dummy numbers", "We did not have enough time to complete the integration. However, to demonstrate the functionality of the chunk loading, some dummy numbers will be used.")
        global current_chunk
        with open("result.txt", 'r') as f:
            f.seek(current_chunk * chunkSize)
            content = f.read(chunkSize)
            chunkArray.append([current_chunk, content])
            self.outputText.insert("1.0", content)

            self.loadMoreBtn = ctk.CTkButton(self.outputFrame, text="Load More Chunks", width=167, height=30, font=("Helvetica", 18), command = self.loadNewChunk)
            self.loadMoreBtn.grid(row=1, column=0, pady=10)

    # load more chunks of data
    def loadNewChunk(self):
        global current_chunk
        if current_chunk<chunkNumber:
            with open("result.txt", 'r') as f:
                current_chunk+=1
                f.seek(current_chunk * chunkSize)
                content = f.read(chunkSize)
                chunkArray.append([current_chunk, content])
            self.outputText.insert("1.0", content)

            self.loadPreviousBtn = ctk.CTkButton(self.outputFrame, text="Load Previous Chunk", width=167, height=30, font=("Helvetica", 18), command=self.loadPreviousChunk)
            self.loadPreviousBtn.grid(row=1, column=1, pady=10)
        
        else:
            messagebox.showinfo("Last Chunk", "This is the last chunk - There are no chunks after this one")

    # load the previous chunk
    def loadPreviousChunk(self):
        global current_chunk
        if current_chunk>0:
            self.outputText.delete(1.0, END)
            with open("result.txt", 'r') as f:
                current_chunk -= 1
                f.seek(current_chunk * chunkSize)
                content = f.read(chunkSize)
                chunkArray.append([current_chunk, content])

                self.outputText.insert("1.0", content)
        else:
            messagebox.showinfo("First Chunk", "This is the first chunk - There are no chunks before this one")

    # transfer data in output screen to input screen if required
    def transferOutput(self):
        self.inputText1.insert(1.0, number)


    # open simple calculator 
    def changeSimpleCalc(self):
        self.destroy()
        from simple_calc import SimpleCalculator

    # copy chunk in text box to clipboard
    def copyText(self):
        self.textCopied = str(self.outputText.get("1.0", END))
        pyperclip.copy(self.textCopied)

# launch application
app = ComplexCalculator()
app.mainloop()