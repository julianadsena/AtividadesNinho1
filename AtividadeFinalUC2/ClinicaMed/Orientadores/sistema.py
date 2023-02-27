from tkinter import *
import time
import ttkthemes
import psycopg2
from PIL import ImageTk #ajuda a importar imagens jpg
from tkinter import ttk,messagebox
from Modelo.classPaciente import Paciente
from Conexao.classConexao import Conexao
#parte funcional
def clock():
    date=time.strftime('%d/%m/%Y')
    hora=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Data:{date}\nHora:{hora}')
    datetimeLabel.after(1000,clock) #para os segundos mudarem
count = 0
text = ''
def slider():
    global text,count #para atualizar o valor da variavel dentro da funcao a seguir
    text = text + s[count] #S
    sliderLabel.config(text=text)
    count +=1
    sliderLabel.after(100,slider)
def connect_database():
    def connect():
        try:
            con = psycopg2.connect(database = "Clinica", host = f"{hostEntry.get()}", port = "5433", user = f"{usernameEntry.get()}", password = f"{passwordEntry.get()}")
            mycursor=con.cursor()
            connectWindow.destroy()
            messagebox.showinfo('Success','Conectado a base de dados')
        except:
            messagebox.showerror('Error','Informações Inválidas') 
    addPacButton.config(state=NORMAL)
    searchPacButton.config(state=NORMAL)
    deletePacButton.config(state=NORMAL)
    updatePacButton.config(state=NORMAL)
    showPacButton.config(state=NORMAL)
    exportPacButton.config(state=NORMAL)
    connectWindow=Toplevel()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Conexão com a base de dados')
    connectWindow.resizable(0,0)
    hostnameLabel=Label(connectWindow,text='Host Name',font=('times new roman',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=Label(connectWindow,text='Usuário',font=('times new roman',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)
    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectWindow,text='Senha',font=('times new roman',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2,show='*')
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)
    
    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,column=1,padx=2.5)
    
    
#parte GUI
sistema=ttkthemes.ThemedTk()
sistema.get_themes()
sistema.set_theme('breeze')

sistema.geometry('1174x680+50+20')
sistema.resizable(0,0)
sistema.title('Sistema Clínica Cuidar - Recepção')
backgroundImage = ImageTk.PhotoImage(file = 'TelaInicial.jpg') #importar imagem
bgLabel = Label(sistema,image=backgroundImage)
bgLabel.place(x=0,y=0)

datetimeLabel=Label(sistema,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Sistema Clínica Cuidar \n Área da Recepção'
sliderLabel=Label(sistema,text=s,font=('times new roman',18,'italic bold'))
sliderLabel.place(x=500,y=0)
slider()

connectButton = ttk.Button(sistema,text='Conectar com a base de dados',command=connect_database)
connectButton.place(x=900,y=10)

leftFrame=Frame(sistema)
leftFrame.place(x=50,y=80,width=300,height=550)

logoImg=PhotoImage(file='logo.png')
logoImLabel = Label(leftFrame, image=logoImg)
logoImLabel.grid(row=0,column=0,padx=20)

addPacButton=ttk.Button(leftFrame, text ='Adicionar Paciente',width=25)
addPacButton.grid(row=1,column=0,pady=30)

searchPacButton=ttk.Button(leftFrame, text ='Procurar Paciente',width=25)
searchPacButton.grid(row=2,column=0,pady=30)

deletePacButton=ttk.Button(leftFrame, text ='Deletar Paciente',width=25)
deletePacButton.grid(row=3,column=0,pady=30)

updatePacButton=ttk.Button(leftFrame, text ='Atualizar Paciente',width=25)
updatePacButton.grid(row=4,column=0,pady=30)

showPacButton=ttk.Button(leftFrame, text ='Mostrar Paciente',width=25)
showPacButton.grid(row=5,column=0,pady=30)

exportPacButton=ttk.Button(leftFrame, text ='Exportar Paciente',width=25)
exportPacButton.grid(row=6,column=0,pady=30)

exitButton=ttk.Button(leftFrame, text ='Sair',width=25)
exitButton.grid(row=7,column=0,pady=30)
rightFrame=Frame(sistema)
rightFrame.place(x=350,y=80,width=800,height=550)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame,orient=VERTICAL)

agenda=ttk.Treeview(rightFrame,columns=('Cod','Nome','Contato','Dt. Agendamento','Horário','Tipo','Médico','Confirmado?'),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=agenda.xview)
ScrollbarY.config(command=agenda.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)

agenda.pack(fill=BOTH,expand=1)
agenda.heading('Cod',text='Cod')
agenda.heading('Nome',text='Nome')
agenda.heading('Contato',text='Contato')
agenda.heading('Dt. Agendamento',text='Dt.Agendamento')
agenda.heading('Horário',text='Horário')
agenda.heading('Tipo',text='Tipo')
agenda.heading('Médico',text='Médico')
agenda.heading('Confirmado?',text='Confirmado?')
agenda.config(show='headings')


sistema.mainloop()
