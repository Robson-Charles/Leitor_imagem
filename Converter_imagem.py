
import os

import ler_texto_da_imagem


class manipular_arquivo:
    def _transforma_em_svg(self):
        import os
        nome_arquivo, extensao_arquivo = os.path.splitext(self)

        novo_nome_arquivo = nome_arquivo + '.svg'
        os.rename(self, novo_nome_arquivo)
        return Converter_imagem._converter_jpg(novo_nome_arquivo)

class Converter_imagem:
    def _converter_jpg(self):

        from wand.image import Image

        with Image(filename=self) as img:
            img.format = 'jpg'
            img.save(filename='Captcha.jpg')

        os.remove('Captcha.svg')
        ler_texto_da_imagem.iniciar()











class escrever_arquivo:




    def __melhorar_font(self = ' '):

        with open(self, 'r', encoding='UTF-8') as arq:
            arquivo = arq.read()
            lista = arquivo.split('|')

            for item in lista:
                    if '<svg' not in item:
                        #print('a')
                        find_d = item.find('d="')
                        find_fim = item.find('"></path>')
                        conteudo_d = item[(find_d + 2):find_fim]
                        vezes_d = conteudo_d.count('Z')
                        if vezes_d > 3 and vezes_d < 6:
                            #print('segunda')
                            primeira_ocorrencia = conteudo_d.find('Z')
                            if primeira_ocorrencia != -1 or primeira_ocorrencia != 0:
                                segunda_ocorrencia = conteudo_d.find('Z',
                                                                     primeira_ocorrencia + 1)
                            with open('Captcha.txt', 'a', encoding='UTF-8') as arq:
                                segunda_ocorrencia += 1
                                arq.write(item.replace(conteudo_d, conteudo_d[:segunda_ocorrencia]))

                        elif vezes_d > 0 and vezes_d < 4:
                            #print('primeira')
                            primeira_ocorrencia = conteudo_d.find('Z')
                            if primeira_ocorrencia != -1 or primeira_ocorrencia != 0:
                                primeira_ocorrencia = conteudo_d.find('Z')
                                with open('Captcha.txt', 'a', encoding='UTF-8') as arq:
                                    primeira_ocorrencia += 1
                                    arq.write(item.replace(conteudo_d, conteudo_d[:primeira_ocorrencia]))
                        elif vezes_d == 0:
                            pass
                        else:
                            #print('terceita')
                            primeira_ocorrencia = conteudo_d.find('Z')
                            if primeira_ocorrencia != -1 or primeira_ocorrencia != 0:
                                segunda_ocorrencia = conteudo_d.find('Z',
                                                                     primeira_ocorrencia + 1)  # Encontra a segunda ocorrência após a primeira
                                terceira_ocorrencia = conteudo_d.find('Z', segunda_ocorrencia + 1)
                                with open('Captcha.txt', 'a', encoding='UTF-8') as arq:
                                    terceira_ocorrencia += 1
                                    arq.write(item.replace(conteudo_d, conteudo_d[:terceira_ocorrencia]))

                        #print(conteudo_d)
                        #print(vezes_d)
                        #print('-' * 30)
                    else:
                        with open('Captcha.txt', 'w', encoding='UTF-8') as arq:
                            arq.write(item)
        with open('Captcha.txt', 'r', encoding='UTF-8') as arq:
            svg_conferir_final = arq.read()
            if '</svg>' not in svg_conferir_final:
                with open('Captcha.txt', 'a', encoding='UTF-8') as arq:
                    arq.write('</svg>')
        return manipular_arquivo._transforma_em_svg('Captcha.txt')
    def criar_txt(self):
        #print(self)
        #with open("Captcha.txt", 'w', encoding='UTF-8') as arq:

            #arq.write(self.replace('%', ' ').replace('*', '=').replace('width="300"', 'width="1600"').replace('height="100"', 'height="900"').replace('#', '').replace('><path', '>|<path'))
        return escrever_arquivo.__melhorar_font(self)





#escrever_arquivo.criar_txt(paths_separados)

















