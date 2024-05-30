from tkinter import *
from pytube import YouTube
#from PIL import ImageTk, Image

root=Tk()
root.geometry('500x300')#Dimensiona el root "ventana"
root.resizable(0, 0)
root.title('Downloader Snow White')#Titulo
root.configure(bg='#313131')
#root.iconbitmap('C:\\Users\MIKI\Desktop\Python\GRAFICO\DownloaderSnowwhite\Logo.ico')Icono del programa

Label(root, text='Descarga videos de YouTube', font='arial 20 bold',fg='#ffffff', bg='#313131').place(x=55, y=30)#Texto normal

link=StringVar()
Label(root, text='Pega el link aqui:', font='arial 12',fg='#ffffff', bg='#313131').place(x=180, y=90)#Texto
link_enter=Entry(root, width=70, textvariable=link).place(x=32, y=120)#Fuente del texto

def Downloader():#Funcion del boton descargar
    url=YouTube(str(link.get()))
    video=url.streams.get_highest_resolution()
    video.download()
    Label(root, text='DESCARGADO', font='arial 13 bold', bg='#AACDE', fg='#B57199').place(x=180, y=240)#Fuente del texto

Button(root, text='DESCARGAR', font='arial 13 bold italic', bg='#ff3c3c', padx=2, command=Downloader).place(x=180, y=180)#Boton descargar, Morado B57199
Label(root, text='SNOW WHITE', font='arial 8', fg='#ffffff', bg='#313131').place(x=420, y=280)#Texto

root.mainloop()