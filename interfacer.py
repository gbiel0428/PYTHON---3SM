import customtkinter as ctk 
import qrcode 
from PIL import Image,ImageTk

ctk.set_appearance_mode('dark')

# Janela

janela = ctk.CTk()
janela.geometry("400x500")
janela.title('Sistema Gerador de QRCODE')
janela.resizable(False,False)

# Janela Concluida

imagem_qr = None

def gerar_qrcode():
    global imagem_qr
    texto = emtrada.get()
    
    if (texto !=''):
        qr = qrcode.make(texto)
        qr = qr.resize((300,300))
        imagem_qr = ImageTk.PhotoImage(qr)
        resultado.configure(image=imagem_qr,text='')
    else:
        resultado.configure(text='Informe o texto ou o pix')
    
# Elementos da Janela

titulo = ctk.CTkLabel(janela,
                    text='Sistema Gerador de Qrcode',
                    text_color='yellow',
                    font=('Arial',30))
titulo.pack(pady=10)

emtrada = ctk.CTkEntry(janela,
                    width=300,
                    height=40,
                    placeholder_text='Informe a URL ou o PIX',
                    placeholder_text_color='yellow')
emtrada.pack(pady=10)


botao = ctk.CTkButton(janela,
                    width=100,
                    height=20,
                    fg_color='white',
                    text='Gerar QrCode',
                    text_color='black',
                    hover_color='silver',
                    cursor='hand2',
                    command=gerar_qrcode)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                        text='')
resultado.pack(pady=20)


# Iniciar Janela

janela.mainloop()
