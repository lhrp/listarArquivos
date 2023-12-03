import os
from tkinter import messagebox

caminhoBasePasta = os.getcwd()

arquivos = os.listdir(caminhoBasePasta)

listaArquivos = fr"{caminhoBasePasta}\arquivosPasta.txt"

def listarArquivo():
    with open(listaArquivos, 'w') as listandoArquivos:
        for arquivo in arquivos:
            caminhoArquivo = caminhoBasePasta + "\\" + arquivo
            listandoArquivos.write(caminhoArquivo + "\n")

listarArquivo()
    
        
messagebox.showinfo("Att", "Arquivo arquivosImg.txt atualizado!")