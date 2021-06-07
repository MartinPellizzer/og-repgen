from tkinter import *
from fpdf import FPDF
from pdf2image import convert_from_path
from PIL import ImageTk, Image

max_col_width = 95


preview_width = 210*2
preview_height = 297*2

class PDF(FPDF):
    def header(self):
        self.image('logo.jpg', 10, 8, h=25)
        self.set_font('times', '', 12)
        self.cell(max_col_width)
        self.multi_cell(max_col_width, 6, ' \n   Numero Certificato: 3220167A2020105041616447\n   Data Certificato: 03/06/2021\n ', border=1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('times', 'B', 10)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')
        
        
def generate_report():
    name = name_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip = zip_entry.get()
    country = country_entry.get()
    email = "Email: " + email_entry.get()
    phone = "Tel: " + phone_entry.get()
    vat = "VAT: " + vat_entry.get()

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.alias_nb_pages()

    pdf.add_page()

    pdf.set_text_color(16)
    pdf.set_draw_color(128)

    pdf.set_font('arial', '', 12)

    cell_width = max_col_width 

    pdf.set_font('arial', 'B', 14)
    pdf.cell(cell_width, 7, 'Fornitore Servizio')
    pdf.cell(cell_width, 7, 'Cliente', ln=True)
    pdf.ln(3)
    
    pdf.set_font('arial', '', 12)
    pdf.cell(cell_width, 7, name)
    pdf.cell(cell_width, 7, name)
    pdf.ln()
    
    pdf.set_font('arial', '', 12)
    pdf.cell(cell_width, 7, address)
    pdf.cell(cell_width, 7, address)
    pdf.ln()
    
    pdf.set_font('arial', '', 12)
    pdf.cell(cell_width, 7, city + " (" + state + "), " + zip)
    pdf.cell(cell_width, 7, city + " (" + state + "), " + zip)
    pdf.ln()
    
    pdf.set_font('arial', '', 12)
    pdf.cell(cell_width, 7, country)
    pdf.cell(cell_width, 7, country)
    pdf.ln()
    
    pdf.set_font('arial', '', 12)
    pdf.cell(cell_width, 7, email)
    pdf.cell(cell_width, 7, email)
    pdf.ln()
    
    pdf.set_font('arial', '', 12)
    pdf.cell(cell_width, 7, phone)
    pdf.cell(cell_width, 7, phone)
    pdf.ln()
    
    pdf.set_font('arial', '', 12)
    pdf.cell(cell_width, 7, vat)
    pdf.cell(cell_width, 7, vat)
    pdf.ln()
    
    pdf.output('report.pdf')
    
def preview_report():
    global preview_label
    global image
    global my_image
    generate_report()
    pages = convert_from_path('report.pdf')
    for page in pages:
        page.save("report.png")
        
    image = Image.open("report.png")
    image = image.resize((preview_width, preview_height), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(image)

    preview_label.config(image=my_image)
    #preview_label.image = my_image


# --------------------------------------------------------------------------
# tkinter
# --------------------------------------------------------------------------
window = Tk()
window.geometry("1920x1080")
window.iconbitmap("logo.ico")
window.title("Certificato Sanificazione")
window.state('zoomed')

menubar = Menu(window)
window.config(menu=menubar)

openImage = PhotoImage(file="logo.png")
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Exit", command=quit)


frame_top = Frame(	window, 
		#bg="green", 
		relief="raised", 
		borderwidth=1, 
		)
frame_top.pack(fill=BOTH, expand=1, side=TOP)
frame_top.pack_propagate(0)

status_label = Label(window, text="Stato")
status_label.pack()

frame1 = Frame(	frame_top, 
		#bg="green", 
		width=300, 
		relief="raised", 
		borderwidth=1, 
		)
frame1.pack(fill=Y, side=LEFT)
frame1.pack_propagate(0)

frame2 = Frame(	frame_top, 
		#bg="red",
		relief="raised", 
		borderwidth=1, 
		)
frame2.pack(expand=1, fill=BOTH)
frame2.pack_propagate(0)


padx = 10
pady = 2

name_label = Label(frame1, text="Nome: ")
name_label.pack(anchor=W, padx=padx, pady=pady)
name_entry = Entry(frame1, width=40)
name_entry.pack(anchor=W, padx=padx, pady=pady)

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

submit = Button(frame1,
		text="Genera Certificato",
		command=lambda:generate_report(),
)
submit.pack(side=LEFT)

preview = Button(frame1,
		text="Anteprima Certificato",
		command=lambda:preview_report(),
)
preview.pack(side=LEFT)

image = Image.open("report.png")
image = image.resize((preview_width, preview_height), Image.ANTIALIAS)
my_image = ImageTk.PhotoImage(image)

preview_label = Label(  frame2,
                        text="label1",
                        image=my_image,
                        )
preview_label.pack()


'''
frame1 = Frame(window, bg="green")
frame1.grid(row=0, column=0)

label1 = Label(frame1, text="label1", width=30)
label1.grid(row=0, column=0)

frame2 = Frame(	window, bg="red")
frame2.grid(row=0, column=1, sticky=W+E)

label2 = Label(frame2, text="label2")
label2.grid(row=0, column=0)
'''

window.mainloop()
