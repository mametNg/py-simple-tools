from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import time
import datetime as dt
from datetime import datetime, timedelta
import os
import json
from PIL import ImageTk, Image

class App():

	pathData = "label-print/trigger"
	fileName = False

	layout = None
	userID = False
	CustomerName = False
	printType = False
	printName = False
	config = False

	def saveCSV(self ,txt):
		try:
			ext = ".csv"
			path = os.path.join(App().basePath(), App.pathData).replace("\\", "/")
			file = os.path.join(path, App.fileName+ext).replace("\\", "/")

			if not os.path.isfile(file):
				wn = open(file, "w")
				wn.close()

			r1 = open(file, "w")
			r1.write(txt)
			r1.close()

			return True
		except Exception as e:
			return False

	def clear(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def basePath(self):
		return os.path.dirname(__file__).replace("\\", "/")

	def times(self, isFormat=False):
		now = datetime.now()
		if isFormat == False: isFormat = "%Y-%m-%d %H:%M:%S"
		return now.strftime(isFormat)

	def config(self):
		path = os.path.join(App().basePath(), "config/printer.json").replace("\\", "/")
		file_exists = os.path.exists(path)

		result = {}
		result['status'] = False

		if file_exists:
			f = open(path)
			data = json.load(f)
			f.close()

			result['status'] = True
			result['data'] = data

		return result

	def msgBox(self ,msg="", tpe=False):
		if tpe == "error":
			showerror(
				title='Error',
				message=msg
				)
		elif tpe == "warning":
			showwarning(
				title='Warning',
				message=msg
				)
		elif tpe == "info":
			showinfo(
				title='Information',
				message=msg
				)
		else:
			msg = 'Invalid'
			showerror(
				title='Error',
				message=msg
				)

	def setWindow(self):
		window_width = 300
		window_height = 365

		screen_width = App.layout.winfo_screenwidth()
		screen_height = App.layout.winfo_screenheight()

		center_x = int(screen_width/2 - window_width / 2)
		center_y = int(screen_height/2 - window_height / 2)
		App.layout.geometry(str(window_width)+'x'+str(window_height)+'+'+str(center_x)+'+'+str(center_y))
		App.layout.resizable(0, 0)

		App.layout.title("Label Test")
		ico = os.path.join(App().basePath(), "assets/img/icon.ico").replace("\\", "/")
		App.layout.iconbitmap(ico)

		# Card Base
		App.card = Frame(App.layout, width=300, height=400, bg="#fff")
		App.card.place(x=0, y=0)

		logo = os.path.join(App().basePath(), "assets/img/icon.png").replace("\\", "/")
		card_bg = Image.open(logo)
		card_bg = ImageTk.PhotoImage(card_bg)
		App.card.bg = Label(App.card, image=card_bg, bg='#fff')
		App.card.bg.image = card_bg
		App.card.bg.place(x=(window_width / 2)/2, y=-5)

	def setWindowError(self):
		window_width = 0
		window_height = 0

		screen_width = App.layout.winfo_screenwidth()
		screen_height = App.layout.winfo_screenheight()

		center_x = int(screen_width/2 - window_width / 2)
		center_y = int(screen_height/2 - window_height / 2)

		# set center screen
		App.layout.geometry(str(window_width)+'x'+str(window_height)+'+'+str(center_x)+'+'+str(center_y))
		App.layout.resizable(0, 0)
		# App.layout.state('zoomed')
		# App.layout.attributes('-alpha', 1)
		# App.layout.attributes('-topmost', 1)
		# App.layout.lift()
		# App.layout.lower()

		App.layout.title("Label Test")
		# hide header app
		App.layout.overrideredirect(True)

	def setForm(self):
		# App.card.pack(padx=10, pady=10, fill='x', expand=True)

		App.userID = StringVar()
		App.CustomerName = StringVar()
		App.printType = StringVar()
		App.printName = StringVar()

		App.label_userID = Label(App.card, text="User ID :", bg="#fff", fg="#373435", font=("yu gothic ui", 10, "bold"))
		App.label_userID.place(x=10, y=110)
		# App.label_userID.pack(fill='x', expand=True)

		App.input_userID = App.ttk.Entry(App.card, textvariable=App.userID)
		App.input_userID.place(x=10, y=130, width=280)
		# App.input_userID.pack(fill='x', expand=True)
		App.input_userID.focus()

		App.label_cusName = Label(App.card, text="Customer Name :", bg="#fff", fg="#373435", font=("yu gothic ui", 10, "bold"))
		App.label_cusName.place(x=10, y=160)
		# App.label_cusName.pack(fill='x', expand=True)

		App.input_cusName = App.ttk.Entry(App.card, textvariable=App.CustomerName)
		App.input_cusName.place(x=10, y=180, width=280)
		# App.input_cusName.pack(fill='x', expand=True)
		# App.input_cusName.focus()

		App.label_printType = Label(App.card, text="Print type :", bg="#fff", fg="#373435", font=("yu gothic ui", 10, "bold"))
		App.label_printType.place(x=10, y=210)
		# App.label_printType.pack(fill='x', expand=True)

		App.input_printType = App.ttk.Combobox(App.card, font=("yu gothic ui ", 10), textvariable=App.printType)
		App.input_printType.place(x=10, y=230, width=280)
		# App.input_printType.pack(fill='x', expand=True)
		# App.input_printType.focus()
		App.input_printType['values'] = ["inner", "outer"]

		App.label_printName = Label(App.card, text="Printer Name :", bg="#fff", fg="#373435", font=("yu gothic ui", 10, "bold"))
		App.label_printName.place(x=10, y=260)
		# App.label_printName.pack(fill='x', expand=True)

		App.input_printName = App.ttk.Combobox(App.card, font=("yu gothic ui ", 10), textvariable=App.printName)
		App.input_printName.place(x=10, y=280, width=280)
		# App.input_printName.pack(fill='x', expand=True)
		# App.input_printName.focus()
		App.input_printName['values'] = [App.config[x]['name'] for x in range(len(App.config))]

		# login button
		App.input_btnPrint = App.ttk.Button(App.card, text="Print", command=App().btn_print)
		App.input_btnPrint.place(x=10, y=320, width=280)
		# App.input_btnPrint.pack(fill='x', expand=True, pady=10)

	def btn_print(self):
		try:
			userID = App.userID.get().strip()
			CustomerName = App.CustomerName.get().strip()
			printType = App.printType.get().strip()
			printName = App.printName.get().strip()

			bartender_command = False
			isDate = False
			isTime = False

			if len(userID) == 0:
				App().msgBox("User ID can't be empty!", "error")
				App.input_userID.focus()
				return False

			if len(CustomerName) == 0:
				App().msgBox("Customer Name can't be empty!", "error")
				App.input_cusName.focus()
				return False

			if len(printType) == 0:
				App().msgBox("Print type can't be empty!", "error")
				App.input_printType.focus()
				return False

			if len(printName) == 0:
				App().msgBox("Printer Name can't be empty!", "error")
				App.input_printName.focus()
				return False

			if printType.lower() == "inner":

				App.fileName = "label_test_inner_"+str(App().times("%y%m%d%H%M%S"))
				# ddmmyy
				isDate = App().times("%d%m%y")
				isTime = App().times("%H:%M")

				bartender_command = "%BTW% /AF="+ os.path.join(App().basePath(), "label-print/template/label_test_inner.btw").replace("\\", "/") +" /D=<Trigger File Name> /PRN=\""+printName+"\" /R=3 /P\n%END%\n"
			elif printType.lower() == "outer":

				App.fileName = "label_test_outer_"+str(App().times("%y%m%d%H%M%S"))
				# dd-mmm-YYYY
				isDate = App().times("%d%b%y")
				isTime = App().times("%H:%M")

				bartender_command = "%BTW% /AF="+ os.path.join(App().basePath(), "label-print/template/label_test_outer.btw").replace("\\", "/") +" /D=<Trigger File Name> /PRN=\""+printName+"\" /R=3 /P\n%END%\n"
			else:
				App().msgBox("invalid print type!", "error")
				App.input_printType.focus()
				return False

			bartender_command += "uid\tcus_name\tdate\ttime\tprinter\n"
			bartender_command += userID+"\t"+CustomerName+"\t"+isDate+"\t"+isTime+"\t"+printName

			save = App().saveCSV(bartender_command)

			if save:
				App().msgBox("Success", "info")
				App.userID.set("")
				App.CustomerName.set("")
				App.printType.set("")
				App.printName.set("")
			else:
				App().msgBox("Print failed!", "error")
				return False
		except Exception as e:
			App().msgBox("Print failed!", "error")
			return False

	def start(self):
		App().clear()
		getConfig = App().config()

		App.layout = Tk()
		App.ttk = ttk

		if not getConfig['status']:
			App().setWindowError()
			App().msgBox("The configuration file was not found!", "error")
			App.layout.destroy()

		if getConfig['status']: 
			App.config = getConfig['data']
			App().setWindow()
			App().setForm()

		App.layout.mainloop()

if __name__ == '__main__':
    App().start()