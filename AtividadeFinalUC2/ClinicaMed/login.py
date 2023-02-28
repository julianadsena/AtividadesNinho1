from tkinter import * #ferramenta python que permite o desenvolvimento de interface gráfica
# a utilização de * significa a importação de todos os métodos e classes da biblioteca
from tkinter import messagebox
from PIL import ImageTk #ajuda a importar imagens jpg
import getpass
def login():
    if usernameEntry.get()=='' or senhaEntry.get()=='':
        messagebox.showerror('Erro','Não pode existir campos vazios')
    elif usernameEntry.get()=='Usuario' and senhaEntry.get()=='1234':
        messagebox.showinfo('Success',f'Bem-vindo {usernameEntry.get()}')
        window.destroy() #fecha a janela anterior
        import sistema
        
    else:
        messagebox.showinfo('Erro','Credencial inválida')
window = Tk () #classe

window.geometry('1288x700+0+0') #método para estabelecer o tamanho da janela e o +0 serve para deixar a tela no canto esquerdo
window.title('Login do Sistema Clinica Cuidar')
window.resizable(False,False) #não deixa redimensionar a tela

backgroundImage = ImageTk.PhotoImage(file = 'TelaInicial.jpg') #importar imagem
bgLabel = Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame = Frame(window,bg='cyan4')
loginFrame.place(x=450,y=250)
logoImage = PhotoImage(file='loginMed.png')
logoLabel = Label(loginFrame, image=logoImage,bg='cyan4')
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage = PhotoImage(file='log.png')
usernameLabel = Label(loginFrame,image=usernameImage,text = 'Usuário',compound=LEFT
                   ,font=('times new roman',15,'bold'),bg='cyan4')
senhaImagem = PhotoImage(file="senha.png")
senhaLabel = Label(loginFrame,image=senhaImagem,text = ' Senha',compound=LEFT
                   ,font=('times new roman',15,'bold'),bg='cyan4')
usernameLabel.grid(row=1,column=0,pady=10,padx=5)
senhaLabel.grid(row=2,column=0,pady=10,padx=5)
usernameEntry=Entry(loginFrame,font=('times new roman',15,'bold'),bd=5)
usernameEntry.grid(row=1,column=1,pady=10,padx=5)
senhaEntry = Entry(loginFrame,font=('times new roman',15,'bold'),bd=5,show='*')
senhaEntry.grid(row=2,column=1,pady=10,padx=5)
loginButton = Button(loginFrame,text='Login',font=('times new roman',15,'bold'),width=15,
fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)
window.mainloop() #permite a continuidade da exibição da janela
