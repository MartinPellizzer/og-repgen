from tkinter import *
from fpdf import FPDF

'''
bg_color = "#121212"
fg_color = "#f2f2f2"

count = 0
def click():
	global count
	username = entry.get()
	entry.delete(0, END)
	#entry.delete(len(entry.get())-1, END)
	count += 1
	print(str(count) + username)

def display():
	if(x.get()==1):
		print("on")
	else:
		print("off")

window = Tk()
window.geometry("420x800")
window.title("Certificato Sanificazione")
window.iconphoto(True, PhotoImage(file="logo.png"))
#window.config(bg=bg_color)

#label_image = PhotoImage(file="logo.png")
nome_fornitore = Label(	window, 
			text="Nome: ", 
			#bg=bg_color, 
			#fg=fg_color, 
			#font=("Arial",12, "normal"),
			#image=label_image, 
			#compound="bottom", 
)
nome_fornitore.pack()



entry = Entry(	window,
		#font=("Arial", 50),
		bd=0,
		#show="*",
) 
#entry.config(state=DISABLED)
entry.pack(anchor=W)

x = IntVar()
check_button_photo = PhotoImage(file="logo.png")
check_button = Checkbutton(	window,
				text="i agree",
				variable=x,
				onvalue=1,
				offvalue=0,
				command=lambda:display(),
				padx=50,
				pady=30,
				image=check_button_photo,		
				indicatoron=0,		
				#width=370,		
)
check_button.pack()


photo = PhotoImage(file="logo.png")
submit = Button(window,
		text="Genera Report",
		command=lambda:click(),
		#bg=bg_color, 
		#fg=fg_color, 
		#font=("Arial",12, "normal"),
		#activeforeground=fg_color, 
		#activebackground=bg_color, 
		#state=DISABLED, 
		image=photo, 
)
submit.pack()

# radiobutton

# scale

# area select


from tkinter import messagebox

def message_box_click():
	messagebox.showinfo(title="title", message="message")
	#messagebox.showwarning(title="title", message="message")
	#messagebox.showerror(title="title", message="message")
	#if messagebox.askokcancel(title="title", message="message"):
	#	print("")
	#if messagebox.askretrycancel(title="title", message="message"):
	#	print("")
	#if messagebox.askyesnocancel(title="title", message="message"):
	#	print("")

message_box_button = Button(window, command=message_box_click, text="message box")
message_box_button.pack()


# color picker

# textarea


# ----------------------------------------------------------------
# filedialog
# ----------------------------------------------------------------
from tkinter import filedialog

def savefile():
	file = filedialog.asksaveasfile(defaultextension=".txt",
					filetypes=[
						("text file", ".txt"),
						("html file", ".html"),
						("all file", ".*"),
					])
	if file is None:
		return
	filetext = str(fd_text.get(1.0, END))
	file.write(filetext)
	file.close()

def openfile():
	filepath = filedialog.askopenfilename(initialdir="",
						title="Open File",
						filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
	file = open(filepath, "r")
	print(file.read())
	file.close()

fd_button = Button(text="Open", command=openfile)
fd_button.pack()

fd_text = Text(window)
fd_text.pack()
fd_save = Button(text="Save", command=savefile)
fd_save.pack()


# ----------------------------------------------------------------
# menubar
# ----------------------------------------------------------------
def copy():
	print("you copy")

def paste():
	print("you paste")

def openFile():
	print("file has been opened")

def saveFile():
	print("file has been saved")

menubar = Menu(window)
window.config(menu=menubar)

openImage = PhotoImage(file="logo.png")
fileMenu = Menu(menubar, tearoff=0, font=("Arial", 16))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound="left")
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)


editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)



# ----------------------------------------------------------------
# frames
# ----------------------------------------------------------------
frame = Frame(window, bg="pink", bd=0)
frame.pack(side=LEFT)

Button(frame, text="w").pack(side=TOP)
Button(frame, text="a").pack(side=LEFT)
Button(frame, text="s").pack(side=LEFT)
Button(frame, text="d").pack(side=LEFT)

# ----------------------------------------------------------------
# window
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# tabs
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# grid
# ----------------------------------------------------------------

l1 = Label(window, text="name", width=20).grid(row=0, column=0)
e1 = Entry(window).grid(row=0, column=1)


window.mainloop()
'''

window = Tk()
window.geometry("1920x1080")

'''
frame1 = Frame(window, bg="#888888", width=300).pack(side=LEFT, fill=BOTH)
frame2 = Frame(window, bg="#f2f2f2")
frame2.pack(side=LEFT, fill=BOTH, expand=1)

Button(frame1, text="w").pack()
Button(frame1, text="a").pack()
Button(frame1, text="s").pack()
Button(frame1, text="d").pack()
Button(frame2, text="d").pack()
'''

frame1 = Frame(	window, 
		#bg="green", 
		width=300, 
		relief="raised", 
		borderwidth=1, 
		)
frame1.pack(fill=Y, side=LEFT)
frame1.pack_propagate(0)

frame2 = Frame(	window, 
		#bg="red",
		relief="raised", 
		borderwidth=1, 
		)
frame2.pack(side=LEFT, expand=1, fill=BOTH)
frame2.pack_propagate(0)

padx = 10
pady = 2

name_label = Label(frame1, text="Nome: ")
name_label.pack(anchor=W, padx=padx, pady=pady)
name_entry = Entry(frame1, width=40)
name_entry.pack(anchor=W, padx=padx, pady=pady)
'''
separator_label = Label(frame1, text="")
separator_label.pack(anchor=W, pady=10)
'''

address_label = Label(frame1, text="Indirizzo: ")
address_label.pack(anchor=W, padx=padx, pady=pady)
address_entry = Entry(frame1, width=40)
address_entry.pack(anchor=W, padx=padx, pady=pady)

city_label = Label(frame1, text="Città: ")
city_label.pack(anchor=W, padx=padx, pady=pady)
city_entry = Entry(frame1, width=40)
city_entry.pack(anchor=W, padx=padx, pady=pady)

state_label = Label(frame1, text="Provincia: ")
state_label.pack(anchor=W, padx=padx, pady=pady)
state_entry = Entry(frame1, width=40)
state_entry.pack(anchor=W, padx=padx, pady=pady)

zip_label = Label(frame1, text="Cap: ")
zip_label.pack(anchor=W, padx=padx, pady=pady)
zip_entry = Entry(frame1, width=40)
zip_entry.pack(anchor=W, padx=padx, pady=pady)

country_label = Label(frame1, text="Stato: ")
country_label.pack(anchor=W, padx=padx, pady=pady)
country_entry = Entry(frame1, width=40)
country_entry.pack(anchor=W, padx=padx, pady=pady)

email_label = Label(frame1, text="Email: ")
email_label.pack(anchor=W, padx=padx, pady=pady)
email_entry = Entry(frame1, width=40)
email_entry.pack(anchor=W, padx=padx, pady=pady)

phone_label = Label(frame1, text="Tel: ")
phone_label.pack(anchor=W, padx=padx, pady=pady)
phone_entry = Entry(frame1, width=40)
phone_entry.pack(anchor=W, padx=padx, pady=pady)

vat_label = Label(frame1, text="IVA: ")
vat_label.pack(anchor=W, padx=padx, pady=pady)
vat_entry = Entry(frame1, width=40)
vat_entry.pack(anchor=W, padx=padx, pady=pady)

def generate_report():
    pdf = FPDF()
    pdf.add_page()
    #pdf.cell(95, 7, "Fornitore Servizio")
    pdf.output("report.pdf")
    

submit = Button(frame1,
		text="Genera Report",
		command=lambda:generate_report(),
)
submit.pack()

Label(frame2, text="label1").pack()

window.mainloop()
