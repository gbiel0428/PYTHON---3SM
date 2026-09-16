import customtkinter as ctk 
ctk.set_appearance_mode('dark')
# FUNÇÕES 
def calcular():
     d = int(distancia.get() )
     c = float(comsumo.get())
     p = float(preco.get())
     
     formula = (d/c)*p
     resultado.configure(text=f"O Valor para a Viagem é de R$: {formula:.2f}")



janela= ctk.CTk()
janela.geometry("500x500")
janela.title("Calculadora de Viagem")
janela.iconbitmap("travel_airplane_1740.ico")


titulo = ctk.CTkLabel(janela,
                      width=200,
                      height=100,
                      text="APP VIAGEM",
                      text_color="white",
                      font=('Verdanna', 35 ,  ('bold')))
titulo.pack()

distancia = ctk.CTkEntry(janela,
                     width=300,
                     height=40,
                     border_color='white',
                     placeholder_text='Digite a distância da viagem em KM: ')

distancia.pack(pady=20)

comsumo = ctk.CTkEntry(janela,
                       width=300,
                       height=40,
                       border_color='white',
                       placeholder_text='Digite o comsumo do seu Veiculo: ')
comsumo.pack(pady=20)

preco = ctk.CTkEntry(janela,
                     width=300,
                     height=40,
                     border_color='white',
                     placeholder_text='Digite o preço autal do combustivel: ')
preco.pack(pady=20)

butao = ctk.CTkButton(
    janela,
    width=150,
    height=30,
    text="Calcular Gasto",
    fg_color="#F5F5F5",       # Fundo claro
    hover_color="#EAEAEA",    # Cor ao passar o mouse
    text_color="#000000",     # Texto preto
    border_width=1,
    border_color="#FF4D4D",   # Borda vermelha/rosa
    corner_radius=5,
    cursor="hand2",
    command=calcular
)


butao.pack(pady=20)


resultado = ctk.CTkLabel(janela,
                         text='',
                         text_color='white',
                         font=('arial',20))
resultado.pack(pady=30)


janela.mainloop()