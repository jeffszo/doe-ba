import re
import pdfplumber
import xlsxwriter


def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with pdfplumber.open(caminho_pdf) as arquivo_pdf:
        num_paginas = len(arquivo_pdf.pages)

        for pagina in range(num_paginas):
            objeto_pagina = arquivo_pdf.pages[pagina]
            texto += objeto_pagina.extract_text()
    return texto

def extrair_matriculas_com_iniciais_onze(texto):
    padrao = r"\b11\d{6}\b"
    matriculas_encontradas = re.findall(padrao, texto)
    return matriculas_encontradas

def extrair_matriculas_com_iniciais_oito(texto):
    padrao_2 = r"\b8\d{7}\b"
    matriculas_encontradas2 = re.findall(padrao_2, texto)
    return matriculas_encontradas2


print('Seja bem-vindo(a)!')

caminho_do_pdf = input('Digite o caminho do arquivo PDF: ')
texto_extraido = extrair_texto_pdf(caminho_do_pdf)

matriculas_encontradas = extrair_matriculas_com_iniciais_onze(texto_extraido)
matriculas_encontradas2 = extrair_matriculas_com_iniciais_oito(texto_extraido)

for numero in matriculas_encontradas:
    print(numero)

for numero2 in matriculas_encontradas2:
    print(numero2)


def exportar_para_excel(dados, nome_arquivo):

    workbook = xlsxwriter.Workbook(nome_arquivo)
    sheet = workbook.add_worksheet()
    sheet.write(0, 0, "Matrículas")

    for linha, dado in enumerate(dados, start=1):
        sheet.write(linha, 0, dado)


    workbook.close()

dados = matriculas_encontradas + matriculas_encontradas2
nome_arquivo_excel = "dados_matriculas.xlsx"
exportar_para_excel(dados, nome_arquivo_excel)
print('Arquivo exportado em Excel com sucesso!')


