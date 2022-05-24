from tkinter import *
from Functions import *
import random

# Functions
def btn_quartzoFunction():
    img_user_pergaminho.grid_forget()
    img_user_podadeira.grid_forget()
    user_choice.set('Quartzo')
    adversary_choice.set(random.choice(q_p_p))
    img_user_quartzo.grid(row=0, column=2)
    
    if adversary_choice.get() == 'Podadeira':
        user_result.set('WIN')
        adversary_result.set('LOSS')
        
    elif adversary_choice.get() == 'Quartzo':
        user_result.set('TIE IN THIS GAME')
        adversary_result.set('TIE IN THIS GAME')
        
    else:
        user_result.set('LOSS')
        adversary_result.set('WIN')
        
    
def btn_pergaminhoFunction():
    user_choice.set('Pergaminho')
    adversary_choice.set(random.choice(q_p_p))
    img_user_pergaminho.grid(row=0, column=2)
    img_user_quartzo.grid_forget()
    img_user_podadeira.grid_forget()
    if adversary_choice.get() == 'Quartzo':
        user_result.set('WIN')
        adversary_result.set('LOSS')
        
    elif adversary_choice.get() == 'Pergaminho':
        user_result.set('TIE IN THIS GAME')
        adversary_result.set('TIE IN THIS GAME')
        
    else:
        user_result.set('LOSS')
        adversary_result.set('WIN')
    
def btn_podadeiraFunction():
    user_choice.set('Podadeira')
    adversary_choice.set(random.choice(q_p_p))
    img_user_podadeira.grid(row=0, column=2)
    img_user_pergaminho.grid_forget()
    img_user_quartzo.grid_forget()
    if adversary_choice.get() == 'Pergaminho':
        user_result.set('WIN')
        adversary_result.set('LOSS')
        
    elif adversary_choice.get() == 'Podadeira':
        user_result.set('TIE IN THIS GAME')
        adversary_result.set('TIE IN THIS GAME')
        
    else:
        user_result.set('LOSS')
        adversary_result.set('WIN')
# ///////////////////////////////////////////////FIM

# Windown config
root = Tk()
root.geometry(center(root,500,560))
root.configure(bg='#3E6292')
root.title('Pedra, Papel e Tesoura')
# ///////////////////////////////////////////////FIM

# Variables
q_p_p = ['Quartzo', 'Pergaminho', 'Podadeira']
user_choice = StringVar()
adversary_choice = StringVar()
user_result = StringVar()
adversary_result = StringVar() 
img_user_select = StringVar()
pergaminho_btn_img = PhotoImage(file= r'C:\Python Projects\Pedra_Papel_Tesoura\img\Pergaminho_mordecai (2).png')
podadeira_btn_img = PhotoImage(file= r'C:\Python Projects\Pedra_Papel_Tesoura\img\Podadeira_mordecai (1).png')
quartzo_btn_img = PhotoImage(file= r'C:\Python Projects\Pedra_Papel_Tesoura\img\Quartzo_mordecai (1).png')
quartzo_img_user = PhotoImage(file=r'C:\Python Projects\Pedra_Papel_Tesoura\img\Quartzo_mordecai (2).png')
podadeira_img_user = PhotoImage(file=r'C:\Python Projects\Pedra_Papel_Tesoura\img\Podadeira_mordecai (1).png')
pergaminho_img_user = PhotoImage(file=r'C:\Python Projects\Pedra_Papel_Tesoura\img\Pergaminho_mordecai (2).png')
# ///////////////////////////////////////////////FIM
# Containers
container_01 = Frame(
    root,
    bg='#3E6292',
    width=500
)
container_02 = Frame(
    root,
    bg='#3E6292',
    width=500,
    height=310
)
row_division = Frame (
    root,
    width=490,
    height=3,
    bg='#4F3D2F'
)
container_03 = Frame(
    root,
    bg='#3E6292',
    width=500,
    height=160
)
container_01.pack()
container_02.pack()
row_division.pack()
container_03.pack()
# ///////////////////////////////////////////////FIM
# Item Container_01
top_text = Label(
    container_01,
    text='Quartzo, Pergaminho e Podadeira',
    font='IceCreamPartySolid 30',
    bg='#3E6292',
    fg='white'
)
result_advesary = Label (
    container_01,
    text='',
    textvariable= adversary_result,
    bg='#3E6292',
    fg= 'white',
    font='IceCreamPartySolid 15'
)
result_user = Label (
    container_01,
    text='',
    textvariable= user_result,
    bg='#3E6292',
    fg= 'white',
    font='IceCreamPartySolid 15'
)

top_text.grid(row=0, columnspan=2)
result_advesary.grid(row=1,column=0)
result_user.grid(row=1,column=1)
# ///////////////////////////////////////////////FIM
# Item Container_02
img_adversary = Label(
    container_02,
    text="",
    textvariable= adversary_choice,
    width=33,
    height=15,
    bg='yellow'
)
row_division_01 = Frame(
    container_02,
    width=3,
    height=311,
    bg='#4F3D2F'
)
img_user_quartzo = Label(
    container_02,
    width=200,
    height=300,
    image=quartzo_img_user,
    bg='#3E6292'
)
img_user_podadeira = Label(
    container_02,
    width=200,
    height=300,
    image=podadeira_img_user,
    bg='#3E6292'
)
img_user_pergaminho = Label(
    container_02,
    width=200,
    height=300,
    image=pergaminho_img_user,
    bg='#3E6292'
)
img_adversary.grid(row=0, column=0)
row_division_01.grid(row=0, column=1,padx=4)

# ///////////////////////////////////////////////FIM
# Item Container_03
btn_quartzo = Button(
    container_03,
    text='Quartzo',
    image=quartzo_btn_img,
    border=0,
    command= btn_quartzoFunction
)
btn_pergaminho = Button(
    container_03,
    text='Pergaminho',
    image=pergaminho_btn_img,
    border=0,
    command= btn_pergaminhoFunction
)
btn_podadeira = Button(
    container_03,
    text='Podadeira',
    image=podadeira_btn_img,
    border=0,
    command=btn_podadeiraFunction
)
btn_quartzo.grid(row=0, column=0, sticky=NW,pady=3,padx=2)
btn_pergaminho.grid(row=0, column=1, sticky=NW,pady=3,padx=2)
btn_podadeira.grid(row=0, column=2, sticky=NW,pady=3,padx=2)
# ///////////////////////////////////////////////FIM

root.mainloop()