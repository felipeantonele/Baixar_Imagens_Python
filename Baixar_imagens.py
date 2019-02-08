import csv
import time
import urllib.request
import requests


if __name__ == '__main__':
    lista_link = str(r'Lista_link.csv')
    try:
        with open(lista_link,'r', encoding='utf-8', errors='ignore') as lb:
            reader = csv.reader(lb)
            i = 0
            for r in reader:
                if i >= 0 : #alterado aqui
                    link1 = r[0]
                    nomeprod = r[1]
                    req = None
                    req2 = None
                    arquivo = None
                    tipo = None
                    tentativa = 1
                    while tentativa > 0:
                        try:
                            time.sleep(0.2)
                            req1 = requests.get(link1)
                            tentativa = 0
                            if req1.status_code == 200:
                                tipo = str('salva')
                                arquivo = str(r'imagens') + chr(92) + nomeprod
                                try:
                                    urllib.request.urlretrieve(link1, arquivo)
                                except:
                                    pass
                            else:
                                tipo = str('não localizada')
                                try:
                                    with open(r'erros.txt', 'a') as txtfile:
                                        texto_write = str(nomeprod + ";" + link1 + ";" + "\r\n")
                                        txtfile.write(texto_write)
                                        txtfile.close()
                                except IOError:
                                    print('I/O Error')
                        except Exception as e:
                            time.sleep(1.0)
                            tentativa += 1
                            print('Erro, tentativa: ' + tentativa)
                            pass
                    print('Imagem ' + tipo + ', código produto: ' + nomeprod + ' - imagem: ' + str(i + 1) + ' de 1169')
                i += 1
    except IOError:
        print('Erro de IO')
