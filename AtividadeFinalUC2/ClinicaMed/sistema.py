from tkinter import *
import time
import ttkthemes
import psycopg2
import pandas as pd
from PIL import ImageTk #ajuda a importar imagens jpg
from tkinter import ttk,messagebox,filedialog
#parte funcional
def iexit():
    result=messagebox.askyesno('Confirme','Deseja sair?')
    if result:
        sistema.destroy()
        import login
    else:
        pass
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=agenda.get_children()
    newlist=[]
    for index in indexing:
        content=agenda.item(index)
        datalist=content['values']
        newlist.append(datalist)
    table=pd.DataFrame(newlist,columns=['Cod','Nome','Dt. Nasc','Dt. Agendamento','Horário','Médico','Confirmado?','Tipo'])    
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')


def update_paciente():
    def update_data():        
        sql=f'''UPDATE "Paciente" SET "Nome"='{NomeEntry.get()}',"medico"='{MedicoEntry.get()}' , "confirmado"='{ConfirmadoEntry.get().lower()}' , "tipo"='{TipoEntry.get().lower()}' , "dtAgend"= '{DtAgendEntry.get()}' , "dataNasc"='{dtNascEntry.get()}' , "horario"='{HoraEntry.get()}' 
          WHERE "ID"='{IdEntry.get()}'
        '''
        mycursor.execute(sql)
        con.commit()
        messagebox.showinfo('Concluido','dado atualizado')
        update_window.destroy()
        show_paciente()

    update_window=Toplevel()
    update_window.grab_set()
    update_window.resizable(False,False)
    IdLabel=Label(update_window,text='Id',font=('times new roman',20,'bold'))
    IdLabel.grid(row=1,column=0,padx=30,pady=15)
    IdEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    IdEntry.grid(row=1,column=1,pady=15,padx=10)
    NomeLabel=Label(update_window,text='Nome',font=('times new roman',20,'bold'))
    NomeLabel.grid(row=2,column=0,padx=30,pady=15)
    NomeEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    NomeEntry.grid(row=2,column=1,pady=15,padx=10)
    dtNascLabel=Label(update_window,text='Data de nascimento',font=('times new roman',20,'bold'))
    dtNascLabel.grid(row=3,column=0,padx=30,pady=15)
    dtNascEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    dtNascEntry.grid(row=3,column=1,pady=15,padx=10)
    HoraLabel=Label(update_window,text='Horario',font=('times new roman',20,'bold'))
    HoraLabel.grid(row=4,column=0,padx=30,pady=15)
    HoraEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    HoraEntry.grid(row=4,column=1,pady=15,padx=10)
    TipoLabel=Label(update_window,text='Tipo(part ou conv)',font=('times new roman',20,'bold'))
    TipoLabel.grid(row=5,column=0,padx=30,pady=15)
    TipoEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    TipoEntry.grid(row=5,column=1,pady=15,padx=10)
    MedicoLabel=Label(update_window,text='Medico',font=('times new roman',20,'bold'))
    MedicoLabel.grid(row=6,column=0,padx=30,pady=15)
    MedicoEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    MedicoEntry.grid(row=6,column=1,pady=15,padx=10)
    ConfirmadoLabel=Label(update_window,text='Confirmado',font=('times new roman',20,'bold'))
    ConfirmadoLabel.grid(row=7,column=0,padx=30,pady=15)
    ConfirmadoEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    ConfirmadoEntry.grid(row=7,column=1,pady=15,padx=10)
    DtAgendLabel=Label(update_window,text='Dt Agendamento',font=('times new roman',20,'bold'))
    DtAgendLabel.grid(row=8,column=0,padx=30,pady=15)
    DtAgendEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    DtAgendEntry.grid(row=8,column=1,pady=15,padx=10)
    
    indexing=agenda.focus()
    content=agenda.item(indexing)
    listdata=content['values']
    IdEntry.insert(0,listdata[0])    
    NomeEntry.insert(0,listdata[1])
    dtNascEntry.insert(0,listdata[2])
    HoraEntry.insert(0,listdata[4])
    TipoEntry.insert(0,listdata[7])
    MedicoEntry.insert(0,listdata[5])
    ConfirmadoEntry.insert(0,listdata[6])
    DtAgendEntry.insert(0,listdata[3])

    update_Paciente_button=ttk.Button(update_window,text='Atualizar',command=update_data)
    update_Paciente_button.grid(row=9,columnspan=2,pady=15) 
    
def show_paciente():
    query = 'select * from "Paciente"'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    agenda.delete(*agenda.get_children())
    for data in fetched_data:
        agenda.insert('', END, values=data)
def search_paciente():
    def search_data():         
        sql=f'''SELECT * FROM "Paciente" WHERE "Nome"='{NomeEntry.get()}' or "medico"='{MedicoEntry.get()}' or "confirmado"='{ConfirmadoEntry.get().lower()}' or "tipo"='{TipoEntry.get().lower()}' or "dtAgend"= '{DtAgendEntry.get()}' or "dataNasc"='{dtNascEntry.get()}' or "horario"='{HoraEntry.get()}' or "medico"='{MedicoEntry.get()}' or "confirmado"='{ConfirmadoEntry.get()}' or "tipo"='{TipoEntry.get()}'
            '''
        mycursor.execute(sql)
        agenda.delete(*agenda.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            agenda.insert('',END,values=data)

       
        

    search_window=Toplevel()
    search_window.grab_set()
    search_window.resizable(False,False)
    NomeLabel=Label(search_window,text='Nome',font=('times new roman',20,'bold'))
    NomeLabel.grid(row=1,column=0,padx=30,pady=15)
    NomeEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    NomeEntry.grid(row=1,column=1,pady=15,padx=10)
    dtNascLabel=Label(search_window,text='Data de nascimento',font=('times new roman',20,'bold'))
    dtNascLabel.grid(row=2,column=0,padx=30,pady=15)
    dtNascEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    dtNascEntry.grid(row=2,column=1,pady=15,padx=10)
    HoraLabel=Label(search_window,text='Horario',font=('times new roman',20,'bold'))
    HoraLabel.grid(row=3,column=0,padx=30,pady=15)
    HoraEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    HoraEntry.grid(row=3,column=1,pady=15,padx=10)
    TipoLabel=Label(search_window,text='Tipo(part ou conv)',font=('times new roman',20,'bold'))
    TipoLabel.grid(row=4,column=0,padx=30,pady=15)
    TipoEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    TipoEntry.grid(row=4,column=1,pady=15,padx=10)
    MedicoLabel=Label(search_window,text='Medico',font=('times new roman',20,'bold'))
    MedicoLabel.grid(row=5,column=0,padx=30,pady=15)
    MedicoEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    MedicoEntry.grid(row=5,column=1,pady=15,padx=10)
    ConfirmadoLabel=Label(search_window,text='Confirmado',font=('times new roman',20,'bold'))
    ConfirmadoLabel.grid(row=6,column=0,padx=30,pady=15)
    ConfirmadoEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    ConfirmadoEntry.grid(row=6,column=1,pady=15,padx=10)
    DtAgendLabel=Label(search_window,text='Dt Agendamento',font=('times new roman',20,'bold'))
    DtAgendLabel.grid(row=7,column=0,padx=30,pady=15)
    DtAgendEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    DtAgendEntry.grid(row=7,column=1,pady=15,padx=10)

    search_Paciente_button=ttk.Button(search_window,text='Procurar',command=search_data)
    search_Paciente_button.grid(row=8,columnspan=2,pady=15)  
def delete_Paciente():
    indexing=agenda.focus()
    print(indexing)
    content=agenda.item(indexing)
    content_id=content['values'][0]
    sql=f'''DELETE FROM "Paciente" WHERE "ID"='{content_id}' 
    '''
    mycursor.execute(sql)
    con.commit()
    content_name=content['values'][1]
    messagebox.showinfo('Deletado',f'O paciente {content_name} foi excluído')
    sql = '''SELECT * FROM "Paciente"'''
    mycursor.execute(sql)
    fetched_data=mycursor.fetchall()
    agenda.delete(*agenda.get_children())
    for data in fetched_data:
        agenda.insert('',END,values=data)
def add_Paciente():
    def add_data():
        if NomeEntry.get()=='' or dtNascEntry.get()=='' or HoraEntry.get()=='' or TipoEntry.get() =='' or MedicoEntry.get()=='' or ConfirmadoEntry.get()=='' or DtAgendEntry.get() == '':
            messagebox.showerror('Error','Necessário preencher pelo menos um campo',parent=add_window)
        else:
            try:
                sql=f'''INSERT INTO "Paciente"
                values (default,'{NomeEntry.get()}','{dtNascEntry.get()}','{DtAgendEntry.get()}','{HoraEntry.get()}','{MedicoEntry.get()}','{ConfirmadoEntry.get()}','{TipoEntry.get()}')
                '''
                mycursor.execute(sql)
                con.commit()
                result=messagebox.askyesno('Dado adicionado.','Deseja limpar o formulario',parent=add_window)
                if result:
                    NomeEntry.delete(0,END)
                    dtNascEntry.delete(0,END)
                    DtAgendEntry.delete(0,END)
                    HoraEntry.delete(0,END)
                    MedicoEntry.delete(0,END)
                    ConfirmadoEntry.delete(0,END)
                    TipoEntry.delete(0,END)
                else:
                    pass
            except: 
                messagebox.showerror('Error')
                return
            sql = '''SELECT * FROM "Paciente"
            '''
            mycursor.execute(sql)
            fetched_data=mycursor.fetchall()
            agenda.delete(*agenda.get_children())
            for data in fetched_data:
                dataList=list(data)
                agenda.insert('',END,values=dataList)              

    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)    
    NomeLabel=Label(add_window,text='Nome',font=('times new roman',20,'bold'))
    NomeLabel.grid(row=1,column=0,padx=30,pady=15)
    NomeEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    NomeEntry.grid(row=1,column=1,pady=15,padx=10)
    dtNascLabel=Label(add_window,text='Data de nascimento',font=('times new roman',20,'bold'))
    dtNascLabel.grid(row=2,column=0,padx=30,pady=15)
    dtNascEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    dtNascEntry.grid(row=2,column=1,pady=15,padx=10)
    HoraLabel=Label(add_window,text='Horario',font=('times new roman',20,'bold'))
    HoraLabel.grid(row=3,column=0,padx=30,pady=15)
    HoraEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    HoraEntry.grid(row=3,column=1,pady=15,padx=10)
    TipoLabel=Label(add_window,text='Tipo(part ou conv)',font=('times new roman',20,'bold'))
    TipoLabel.grid(row=4,column=0,padx=30,pady=15)
    TipoEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    TipoEntry.grid(row=4,column=1,pady=15,padx=10)
    MedicoLabel=Label(add_window,text='Medico',font=('times new roman',20,'bold'))
    MedicoLabel.grid(row=5,column=0,padx=30,pady=15)
    MedicoEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    MedicoEntry.grid(row=5,column=1,pady=15,padx=10)
    ConfirmadoLabel=Label(add_window,text='Confirmado',font=('times new roman',20,'bold'))
    ConfirmadoLabel.grid(row=6,column=0,padx=30,pady=15)
    ConfirmadoEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    ConfirmadoEntry.grid(row=6,column=1,pady=15,padx=10)
    DtAgendLabel=Label(add_window,text='Dt Agendamento',font=('times new roman',20,'bold'))
    DtAgendLabel.grid(row=7,column=0,padx=30,pady=15)
    DtAgendEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    DtAgendEntry.grid(row=7,column=1,pady=15,padx=10)

    add_Paciente_button=ttk.Button(add_window,text='Adicionar',command=add_data)
    add_Paciente_button.grid(row=8,columnspan=2,pady=15)
def clock():
    global date,hora
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
        global mycursor,con         
        try:
            
            con = psycopg2.connect(database = "Clinica", host = f"{hostEntry.get()}", port = "5433", user = f"{usernameEntry.get()}", password = f"{passwordEntry.get()}")
            mycursor=con.cursor()                        
            messagebox.showinfo('Success','Conectado a base de dados')     
            connectWindow.destroy()
            addPacButton.config(state=NORMAL)
            searchPacButton.config(state=NORMAL)
            updatePacButton.config(state=NORMAL)
            showPacButton.config(state=NORMAL)
            exportPacButton.config(state=NORMAL)
            deletePacButton.config(state=NORMAL)
            exitButton.config(state=NORMAL)
        except:            
            messagebox.showerror('ERROR','Detalhes invalidos',parent=connectWindow)
            return  
        
        
       
            
        
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
leftFrame.place(x=50,y=80,width=300,height=600)

logoImg=PhotoImage(file='logo.png')
logoImLabel = Label(leftFrame, image=logoImg)
logoImLabel.grid(row=0,column=0,padx=20)

addPacButton=ttk.Button(leftFrame, text ='Adicionar Paciente',width=25,state=DISABLED,command=add_Paciente)
addPacButton.grid(row=1,column=0,pady=20)

searchPacButton=ttk.Button(leftFrame, text ='Procurar Paciente',width=25,state=DISABLED,command=search_paciente)
searchPacButton.grid(row=2,column=0,pady=20)

deletePacButton=ttk.Button(leftFrame, text ='Deletar Paciente',width=25,state=DISABLED,command=delete_Paciente)
deletePacButton.grid(row=3,column=0,pady=20)

updatePacButton=ttk.Button(leftFrame, text ='Atualizar Paciente',width=25,state=DISABLED,command=update_paciente)
updatePacButton.grid(row=4,column=0,pady=20)

showPacButton=ttk.Button(leftFrame, text ='Mostrar Paciente',width=25,state=DISABLED,command=show_paciente)
showPacButton.grid(row=5,column=0,pady=20)

exportPacButton=ttk.Button(leftFrame, text ='Exportar Paciente',width=25,state=DISABLED,command=export_data)
exportPacButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)
                
rightFrame=Frame(sistema)
rightFrame.place(x=350,y=80,width=820,height=600)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame,orient=VERTICAL)

agenda=ttk.Treeview(rightFrame,columns=('Cod','Nome','Dt. Nasc','Dt. Agendamento','Horário','Médico','Confirmado?','Tipo'),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=agenda.xview)
ScrollbarY.config(command=agenda.yview)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)

agenda.pack(fill=BOTH,expand=1)
agenda.heading('Cod',text='Cod')
agenda.heading('Nome',text='Nome')
agenda.heading('Dt. Nasc',text='Dt. Nascimento')
agenda.heading('Dt. Agendamento',text='Dt.Agendamento')
agenda.heading('Horário',text='Horário')
agenda.heading('Médico',text='Médico')
agenda.heading('Confirmado?',text='Confirmado?')
agenda.heading('Tipo',text='Tipo')


agenda.column('Cod',width=50,anchor=CENTER)
agenda.column('Nome',width=200,anchor=CENTER)
agenda.column('Dt. Nasc',width=300,anchor=CENTER)
agenda.column('Dt. Agendamento',width=300,anchor=CENTER)
agenda.column('Horário',width=200,anchor=CENTER)
agenda.column('Médico',width=200,anchor=CENTER)
agenda.column('Confirmado?',width=200,anchor=CENTER)
agenda.column('Tipo',width=100,anchor=CENTER)


style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')
agenda.config(show='headings')

sistema.mainloop()
