import customtkinter as ctk
ctk.set_appearance_mode('dark')

def calcular():
    p =float(media1.get())
    s =float(media2.get())
    t =float(media3.get())

    formula = (p + s + t ) / 3
    
    if formula > 5:
            resultado.configure(text=f"Voçe esta aprovado.Sua Media foi: {formula:.1f}")
            
    else:
            resultado.configure(text= f"Voçe esta em Recuperação. Sua Media foi: {formula:.1f}")
        
    

janela = ctk.CTk()
janela.geometry('600x600')
janela.resizable(False,False)
janela.title('Sistema Escolar 2026')
janela.iconbitmap

titulo = ctk.CTkLabel(janela,
                    width=400,
                    height=100,
                    text="Sistema Escola",
                    text_color="yellow",
                    font=('Arial', 50 ,  ('bold')))
titulo.pack()


media1 = ctk.CTkEntry(janela,
                      width=400,
                      height=40,
                      border_color='yellow',
                      placeholder_text='Digite a sua nota na 1ª Unidade: ')
media1.pack(pady=20)


media2 = ctk.CTkEntry(janela,
                      width=400,
                      height=40,
                      border_color='yellow',
                      placeholder_text='Digite a sua nota da 2ª Unidade: ')
media2.pack(pady=20)

media3 = ctk.CTkEntry(janela,
                      width=400,
                      height=40,
                      border_color='yellow',
                      placeholder_text='Digite a sua nota da 3ª Unidade: ')
media3.pack(pady=20)


butao = ctk.CTkButton(janela,
                      width=150,
                      height=40,
                      text='Resultado',
                      fg_color="#fff705",
                      text_color="#000000",
                      border_width=1,
                      border_color="#000000",
                      cursor= 'hand2',
                      command=calcular)
butao.pack(pady=20)

resultado = ctk.CTkLabel(janela,
                         text='',
                         text_color='white',
                         font=('arial', 20))
resultado.pack(pady=30)


janela.mainloop()