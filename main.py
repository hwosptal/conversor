from PIL import Image  
import argparse
import os

os.system("cls") 

def pngparajpg(diretorio, caminho_novo): 
    img = Image.open(diretorio).convert("RGBA") #preserva o canal alfa  
 
    img_com_fundo_branco = Image.new("RGB", img.size, (255, 255, 255))
    img_com_fundo_branco.paste(img, mask=img.split()[3]) #usa o canal alfa como mascara

    img_com_fundo_branco.save(f"{caminho_novo}.jpg", quality=95) #salva img

def jpgparapng(diretorio, caminho_novo):
    img = Image.open(diretorio)
    img.save(f"{caminho_novo}.png")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Conversor")
    parser.add_argument("-png",help="Converte PNG para JPG [-png C:/caminho/do/arquivo.png -f C:/novo/caminho]")
    parser.add_argument("-jpg",help="Converte JPG para PNG [-jpg C:/caminho/do/arquivo.jpg -f C:/novo/caminho]") 
    parser.add_argument("-f",help="Nome e Caminho do novo arquivo")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    if args.png:
        pngparajpg(args.png, args.f)
    elif args.jpg:
        jpgparapng(args.jpg, args.f)
    else:
        print("Selecione: -png ou -jpg para fazer a conversao")