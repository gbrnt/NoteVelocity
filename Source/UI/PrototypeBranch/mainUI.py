"""The main UI file of my note-taking program"""

## Imports
from Tkinter import *
from tkFileDialog import askopenfilename
import makeThe

## Initialise NoteApp class
class NoteApp:

	## Constructor
	def __init__ (self, master):

		# Initialise variables
		self.openLocation = None
		self.inputFile = None
		self.outputFile = None

		# Initialise show variables
		self.showFormFrame = True
		self.showMenuBar = True

		# Create upper level 2 frame (Text + Formatting)
		self.textFormFrame = Frame(bg = "#FF0000")
		self.textFormFrame.pack(fill = BOTH, side = TOP, expand = 1)

		# Create left level 3 frame (Text)
		self.textFrame = Frame(self.textFormFrame, bg = "#FF8800")
		self.textFrame.pack(fill = BOTH, expand = 1, side = LEFT)

		if self.showFormFrame == True:
			# Create right level 3 frame (Formatting)
			self.formFrame = Frame(self.textFormFrame)
			self.formFrame.pack(fill = Y, side = RIGHT)

		# Create lower level 2 frame (File ops)
		if self.showMenuBar == True:
			self.fileOpsFrame = Frame()
			self.fileOpsFrame.pack(fill = X, side = BOTTOM)

		# Create text box in textFrame
		self.textBox = Text(self.textFrame, bg = "#FFFFFF", fg = "#404040", padx = 5, pady = 5)
		self.textBox.pack(fill = BOTH, expand = 1, side = LEFT)

		# Create scrollbar in textFrame
		self.textScrollBar = Scrollbar(self.textFrame, width = 16)
		self.textScrollBar.pack(fill = Y, side = RIGHT)

		# Link scrollbar and text box
		self.textBox.config(yscrollcommand = self.textScrollBar.set)
		self.textScrollBar.config(command = self.textBox.yview)

		if self.showFormFrame == True:
			# Create formatting buttons in formFrame
			self.boldButton = Button(self.formFrame, text = "<B>", width = 1, font = ("DejaVu Sans", "8", "normal"))
			self.boldButton.pack(side = TOP)
			self.boldButton.bind('<Enter>', lambda event: self.boldButton.configure(text = "B", font = ("DejaVu Sans", "8", "bold")))
			self.boldButton.bind('<Leave>', lambda event: self.boldButton.configure(text = "<B>", font = ("DejaVu Sans", "8", "normal")))

			self.italicButton = Button(self.formFrame, text = "*I*", width = 1, font = ("DejaVu Sans", "8", "normal"))
			self.italicButton.pack(side = TOP)
			self.italicButton.bind('<Enter>', lambda event: self.italicButton.configure(text = "I", font = ("DejaVu Sans", "8", "italic")))
			self.italicButton.bind('<Leave>', lambda event: self.italicButton.configure(text = "*I*", font = ("DejaVu Sans", "8", "normal")))

			self.underlineButton = Button(self.formFrame, text = "_U_", width = 1, font = ("DejaVu Sans", "8", "normal"))
			self.underlineButton.pack(side = TOP)
			self.underlineButton.bind('<Enter>', lambda event: self.underlineButton.configure(text = "U", font = ("DejaVu Sans", "8", "underline")))
			self.underlineButton.bind('<Leave>', lambda event: self.underlineButton.configure(text = "_U_", font = ("DejaVu Sans", "8", "normal")))

		if self.showMenuBar == True:
			# Create file operation buttons in fileOpsFrame
			self.openButton = Button(self.fileOpsFrame, text = "Open", font = ("DejaVu Sans", "8", "normal"), command = self.askLocation)
			self.openButton.pack(side = LEFT)

			self.saveButton = Button(self.fileOpsFrame, text = "Save", font = ("DejaVu Sans", "8", "normal"), command = self.saveFile)
			self.saveButton.pack(side = LEFT)

			self.quitButton = Button(self.fileOpsFrame, text = "Quit", font = ("DejaVu Sans", "8", "normal"), command = master.quit)
			self.quitButton.pack(side = RIGHT)

	# Ask for location and open file
	def askLocation(self):
		# Run open dialog box to get filename
		self.openLocation = askopenfilename(filetypes = [("Note files","*.note"),("Text files","*.txt")])

		# If the filename is a blank string
		if self.openLocation == "":
			# Return exception here - new window saying "No file selected"
			print ("Open Location Empty")
		else:
			# Open inputFile
			self.inputFile = open (self.openLocation, "r")

	def saveFile(self):
		pass

## STARTING

# Root widget
root = Tk()

# Root widget properties
root.title("Note") # Title in window title bar
root.minsize(640,480) # Minimum size of window
root.geometry("800x600") # Initial size of window
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(2, weight = 0)

# New instance of NoteApp
app = NoteApp(root)

# Call root widget's main loop
root.mainloop()