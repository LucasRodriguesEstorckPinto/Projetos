from tkinter import *
def abre(url = 'https://www.cursoemvideo.com/course/javascript/aulas/repeticoes-em-javascript/modulos/repeticoes-parte-1/https://www.cursoemvideo.com/course/javascript/aulas/repeticoes-em-javascript/modulos/repeticoes-parte-1/'):
    import webbrowser
    try:
        webbrowser.open(url)
    except:
        print('SITE INDISPONÍVEL OU INTERNET DESCONECTADA')
    else:
        a = 'Abrindo...'
        textoa['text'] = a



janela = Tk()
janela.title('Verifica site')
texto_ini = Label(janela, text='abrir o curso em video')
texto_ini.grid(column=0,row=0,padx=10,pady=10)
botao = Button(janela, text = 'Verificar',command=abre)
botao.grid(column=0,row=1)
textoa = Label(janela, text = '')
textoa.grid(column=0, row=2)


janela.mainloop()


