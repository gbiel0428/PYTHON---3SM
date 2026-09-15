import customtkinter as ctk

ctk.set_appearance_mode("dark")

# ---- JANELA -------------------------------------------------------

janela = ctk.CTk()
janela.geometry("500x500")
janela.title('Sistema de Login - 2026')
janela.iconbitmap('1490886323-27-math_82468.ico')

# ---------------------------------------------------------------

titulo = ctk.CTkLabel(janela,
                        text='Sistema de Login',
                        text_color='Red',
                        font=('arial', 20))
titulo.pack()

login = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        border_color='red',
                        placeholder_text='Informe o Login: ')
login.pack(pady=30)

senha = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        border_color='red',
                        placeholder_text='Informe a Senha: ',
                        show='*')
senha.pack(pady=30)

butao = ctk.CTkButton(janela,
                        width=200,
                        height=40,
                        text='Acessar',
                        fg_color='red',
                        cursor='hand2')
butao.pack(pady=30)

janela.mainloop()
