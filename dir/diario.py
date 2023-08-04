import re
import os
import PyPDF2
import xlsxwriter

# Extrair todo texto de todas as páginas usando o PyPDF2


def extrair_texto_pdf(caminho_pdf):
    texto = ""  
    with open(caminho_pdf, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf)
        num_paginas = leitor_pdf.numPages

        for pagina in range(num_paginas):
            objeto_pagina = leitor_pdf.getPage(pagina)
            texto_pagina = objeto_pagina.extractText()
            texto += texto_pagina

    texto = texto.upper()
    return texto

# Restante do código permanece o mesmo...


# Extrair as matrículas de aposentadoria
def aposentadoria11(texto):
    padrao = r"RESOLVE CONCEDER APOSENTADORIA.* SEC, PROFESSOR, .*MATRÍCULA \b11\d{6}\b"
    aposentadorias_encontradas = re.findall(padrao, texto)
    return aposentadorias_encontradas

# Extrair as matriculas de licenca médica
def licenca_medica(texto):
    padrao = r'(\d{8})([A-Z\s]+)(PROFESSOR)(\d{2}\.\d{2}\.\d{4})(\d{2}\.\d{2}\.\d{4})'
    licencas_medicas_encontradas = re.findall(padrao, texto)
    return licencas_medicas_encontradas


def licenca_medica9(texto):
    padrao = r"RESOLVE CONCEDER LICENÇA PARA TRATAMENTO DE SAÚDE AO\(S\) SERVIDOR\(ES\) ABAIXO RELACIONADO\(S\): MATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS\b11\d{6}\b[A-Z ]{1,30}PROFESSOR\d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    licencas_medicas9_encontradas = re.findall(padrao, texto)
    return licencas_medicas9_encontradas

# Extrair as matriculas de designação

def designacao_vice(texto):
    padrao = r"\b11\d{6}, PARA O CARGO EM COMISSÃO VICE-DIRETOR"
    vice_diretores_encontrados = re.findall(padrao, texto)
    return vice_diretores_encontrados

def designacao_diretor(texto):
    padrao = r"\b11\d{6}, PARA O CARGO EM COMISSÃO DIRETOR"
    diretores_encontrados = re.findall(padrao, texto)
    return diretores_encontrados 


def readaptacao(texto):
    padrao = r"RESOLVE READAPTAR POR PRAZO DETERMINADO, NOS TERMOS DO\(A\) ART\. 43 DA LEI Nº 6\.677, DE 26 DE SETEMBRO DE 1994, O\(S\) SERVIDOR\(ES\) ABAIXO RELACIONADO\(S\):\nMATRÍCULANOME SERVIDORCARGODATA INÍCIODATA FIM  \d{8}[A-Z \s]+ PROFESSOR \d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    readaptacao_encontrada = re.findall(padrao, texto)
    return readaptacao_encontrada

# Extrair as remoções
def remocao(texto): # Quebra de linha - incluir
    padrao = r"RESOLVE REMOVER, A PEDIDO, O\(S\) SERVIDOR\(ES\)ABAIXO:\nMATRÍCULANOMECARGOUNIDADE ORIGEMUNIDADE DESTINODATA INÍCIONÚMERO DO PROC\. SEI.*\b11\d{6} .* PROFESSOR"
    remocoes_encontradas = re.findall(padrao, texto) 
    return remocoes_encontradas


def remocao8(texto):
    padrao = r"RESOLVE REMOVER, A PEDIDO, O\(S\) SERVIDOR\(ES\)ABAIXO:\nMATRÍCULANOMECARGOUNIDADE ORIGEMUNIDADE DESTINODATA INÍCIONÚMERO DO PROC\. SEI.*\b8\d{7}\b .* PROFESSOR"
    remocoes_encontradas8 = re.findall(padrao, texto)
    return remocoes_encontradas8


def alteracao_ch(texto):
    padrao = r"RESOLVE ALTERAR,  A CARGA HORÁRIA:\nMATRÍCULASERVIDORCARGOUNIDADE ORIGEMMUNICÍPIOCARGA HORÁRIA ATUALNOVA CARGA HORÁRIADATA INÍCIO \b11\d{6}\b .*\d{2}\.\d{2}"
    alteracoes = re.findall(padrao, texto)
    return alteracoes

def alteracao_ch9(texto):
    padrao = r"RESOLVE ALTERAR,  A CARGA HORÁRIA:\nMATRÍCULASERVIDORCARGOUNIDADE ORIGEMMUNICÍPIOCARGA HORÁRIA ATUALNOVA CARGA HORÁRIADATA INÍCIO \b9\d{7}\b .*\d{2}\.\d{2}"
    alteracoes9 = re.findall(padrao, texto)
    return alteracoes9

def alteracoes_ch8(texto):
    padrao = r"RESOLVE ALTERAR,  A CARGA HORÁRIA:\nMATRÍCULASERVIDORCARGOUNIDADE ORIGEMMUNICÍPIOCARGA HORÁRIA ATUALNOVA CARGA HORÁRIADATA INÍCIO \b8\d{7}\b .*\d{2}\.\d{2}"
    alteracoes8 = re.findall(padrao, texto)
    return alteracoes8

def licenca_curso(texto):
    padrao = r"RESOLVE CONCEDER LICENÇA P\/PÓS GRAD \(100%\) AO\(S\) SERVIDOR\(ES\) ABAIXO RELACIONADO\(S\) PERTENCENTE\(S\) AO QUADRO DE PESSOAL DO\(A\) SECRETARIA DA EDUCAÇÃO\.\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  \b11\d{6}\b"
    licenca_curso_encontradas = re.findall(padrao, texto)
    return licenca_curso_encontradas

def licenca_curso9(texto):
    padrao = r"RESOLVE CONCEDER LICENÇA P\/PÓS GRAD .* AO\(S\) SERVIDOR\(ES\) ABAIXO RELACIONADO\(S\) PERTENCENTE\(S\) AO QUADRO DE PESSOAL DO\(A\) SECRETARIA DA EDUCAÇÃO\.\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  \b9\d{7}\b"
    licenca_curso_encontradas9 = re.findall(padrao, texto)
    return licenca_curso_encontradas9

def licenca_curso8(texto):
    padrao = r"RESOLVE CONCEDER LICENÇA P\/PÓS GRAD .* AO\(S\) SERVIDOR\(ES\) ABAIXO RELACIONADO\(S\) PERTENCENTE\(S\) AO QUADRO DE PESSOAL DO\(A\) SECRETARIA DA EDUCAÇÃO\.\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  \b8\d{7}\b"
    licenca_curso_encontradas8 = re.findall(padrao, texto)
    return licenca_curso_encontradas8

def licenca_gestante(texto):
    padrao = r"RESOLVE CONCEDER/PRORROGAR LICENÇA À GESTANTE, CONFORME O DISPOSTO NO\(A\) ART\. 154 DA LEI Nº 6.677, DE 26 DE SETEMBRO DE 1994, COM REDAÇÃO DADA PELO ART\. 1º DA LEI Nº 12.214, DE 26 DE MAIO DE 2011, À\(S\) SERVIDORA\(S\) ABAIXO RELACIONADA\(S\):\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  \b11\d{6}\b [A-Z ]+ PROFESSOR \d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    licenca_gestante_encontradas = re.findall(padrao, texto)
    return licenca_gestante_encontradas

def licenca_gestante8(texto):
    padrao = r"RESOLVE CONCEDER/PRORROGAR LICENÇA À GESTANTE, CONFORME O DISPOSTO NO\(A\) ART\. 154 DA LEI Nº 6.677, DE 26 DE SETEMBRO DE 1994, COM REDAÇÃO DADA PELO ART\. 1º DA LEI Nº 12.214, DE 26 DE MAIO DE 2011, À\(S\) SERVIDORA\(S\) ABAIXO RELACIONADA\(S\):\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  \b8\d{7}\b [A-Z ]+ PROFESSOR \d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    licenca_gestante_encontradas8 = re.findall(padrao, texto)
    return licenca_gestante_encontradas8

def licenca_gestante9(texto):
    padrao = r"RESOLVE CONCEDER/PRORROGAR LICENÇA À GESTANTE, CONFORME O DISPOSTO NO\(A\) ART\. 154 DA LEI Nº 6.677, DE 26 DE SETEMBRO DE 1994, COM REDAÇÃO DADA PELO ART\. 1º DA LEI Nº 12.214, DE 26 DE MAIO DE 2011, À\(S\) SERVIDORA\(S\) ABAIXO RELACIONADA\(S\):\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  \b9\d{7}\b [A-Z ]+ PROFESSOR \d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    licenca_gestante_encontradas9 = re.findall(padrao, texto)
    return licenca_gestante_encontradas9

# Exoneracao
def exoneracao(texto):
    padrao = r"RESOLVE  EXONERAR,.*\nMATRÍCULANOMECARGOUNIDADEDATA INÍCIOPROCESSO  \b11\d{6}\b .* PROFESSOR"
    exoneracao_encontradas = re.findall(padrao, texto)
    return exoneracao_encontradas

def exoneracao8(texto):
    padrao = r"RESOLVE  EXONERAR,.*\nMATRÍCULANOMECARGOUNIDADEDATA INÍCIOPROCESSO  \b8\d{7}\b .* PROFESSOR"
    exoneracao_encontradas8 = re.findall(padrao, texto)
    return exoneracao_encontradas8

def exoneracao9(texto):
    padrao = r"RESOLVE  EXONERAR,.*\nMATRÍCULANOMECARGOUNIDADEDATA INÍCIOPROCESSO  \b9\d{7}\b .* PROFESSOR"
    exoneracao_encontradas9 = re.findall(padrao, texto)
    return exoneracao_encontradas9

def licenca_premio(texto):
    padrao = r"RESOLVE CONCEDER O DIREITO À LICENÇA-PRÊMIO AO\(S\) SERVIDOR\(ES\) INTEGRANTE\(S\) DO QUADRO DE MAGISTÉRIO PÚBLICO ESTADUAL DESTE ÓRGÃO, ABAIXO RELACIONADO\(S\):\nMATRÍCULANOMEQUINQUÊNIODATA INÍCIODATA FIMFINALIDADE  \b11\d{6}\b .*\d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    licenca_premio_encontradas = re.findall(padrao, texto)
    return licenca_premio_encontradas

def licenca_premio9(texto):
    padrao = r"RESOLVE CONCEDER O DIREITO À LICENÇA-PRÊMIO AO\(S\) SERVIDOR\(ES\) INTEGRANTE\(S\) DO QUADRO DE MAGISTÉRIO PÚBLICO ESTADUAL DESTE ÓRGÃO, ABAIXO RELACIONADO\(S\):\nMATRÍCULANOMEQUINQUÊNIODATA INÍCIODATA FIMFINALIDADE  \b9\d{7}\b .*\d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    licenca_premio_encontradas9 = re.findall(padrao, texto)
    return licenca_premio_encontradas9


def licenca_premio8(texto):
    padrao = r"RESOLVE CONCEDER O DIREITO À LICENÇA-PRÊMIO AO\(S\) SERVIDOR\(ES\) INTEGRANTE\(S\) DO QUADRO DE MAGISTÉRIO PÚBLICO ESTADUAL DESTE ÓRGÃO, ABAIXO RELACIONADO\(S\):\nMATRÍCULANOMEQUINQUÊNIODATA INÍCIODATA FIMFINALIDADE  \b8\d{7}\b .*\d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    licenca_premio_encontradas8 = re.findall(padrao, texto)
    return licenca_premio_encontradas8

def licenca_particular(texto):
    padrao = r"RESOLVE CONCEDER LICENÇA PARA TRATAR DE INTERESSE PARTICULAR AO\(S\) SERVIDOR\(ES\) ABAIXO RELACIONADO\(S\) PERTENCENTE\(S\) AO QUADRO DE PESSOAL DO\(A\) SEC\.\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  \d{8} .* \d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}"
    licenca_particular_encontradas = re.findall(padrao, texto)
    return licenca_particular_encontradas


# Caminho do arquivo
try:
    caminho_do_pdf = input('Digite o caminho do arquivo PDF: ')
    texto_extraido = extrair_texto_pdf(caminho_do_pdf)
except (FileNotFoundError, PermissionError):
    print(f'Caminho do arquivo está incorreto')
else:
    aposentadorias_encontradas = aposentadoria11(texto_extraido)
    licencas_medicas_encontradas = licenca_medica(texto_extraido)
    licencas_medicas9_encontradas = licenca_medica9(texto_extraido)
    vice_diretores_encontrados = designacao_vice(texto_extraido)
    remocoes_encontradas = remocao(texto_extraido)
    readaptacao_encontrada = readaptacao(texto_extraido)
    remocoes_encontradas8 = remocao8(texto_extraido)
    alteracoes = alteracao_ch(texto_extraido)
    licenca_curso_encontradas = licenca_curso(texto_extraido)
    licenca_curso_encontradas8 = licenca_curso8(texto_extraido)
    licenca_curso_encontradas9 = licenca_curso9(texto_extraido)
    diretores_encontrados = designacao_diretor(texto_extraido)
    exoneracao_encontradas = exoneracao(texto_extraido)
    exoneracao_encontradas8 = exoneracao8(texto_extraido)
    exoneracao_encontradas9 = exoneracao9(texto_extraido)
    alteracoes9 = alteracao_ch9(texto_extraido)    
    alteracoes8 = alteracoes_ch8(texto_extraido)
    licenca_gestante_encontradas = licenca_gestante(texto_extraido)
    licenca_gestante_encontradas9 = licenca_gestante9(texto_extraido)
    licenca_gestante_encontradas8 = licenca_gestante8(texto_extraido)
    licenca_premio_encontradas = licenca_premio(texto_extraido)
    licenca_premio_encontradas8 = licenca_premio8(texto_extraido)
    licenca_premio_encontradas9 = licenca_premio9(texto_extraido)
    licenca_particular_encontradas = licenca_particular(texto_extraido)
#print(texto_extraido)

for readaptar in readaptacao_encontrada:
    readaptar = readaptar.replace(
        'RESOLVE READAPTAR POR PRAZO DETERMINADO, NOS TERMOS DO(A) ART. 43 DA LEI Nº 6.677, DE 26 DE SETEMBRO DE 1994, O(S) SERVIDOR(ES) ABAIXO RELACIONADO(S):\nMATRÍCULANOME SERVIDORCARGODATA INÍCIODATA FIM  ', 'READAPTAÇÃO - ')
    print(readaptar)

# Substituir 'proventos' por APOSENTADORIA
for aposentado in aposentadorias_encontradas:
    aposentado = re.sub(r'RESOLVE CONCEDER APOSENTADORIA.* SEC, PROFESSOR, .*MATRÍCULA', 'APOSENTADORIA -', aposentado)
    print(aposentado)
# Licença médica
for licenca in licencas_medicas_encontradas:
    print(f'LICENÇA MÉDICA - {licenca}')

# # for licenca9 in licencas_medicas9_encontradas:
# #     licenca_m9 = licenca9.upper()
# #     print(licenca_m9)



# Remoção
for removido in remocoes_encontradas:
    removido = removido.replace('RESOLVE REMOVER, A PEDIDO, O(S) SERVIDOR(ES)ABAIXO:\nMATRÍCULANOMECARGOUNIDADE ORIGEMUNIDADE DESTINODATA INÍCIONÚMERO DO PROC. SEI ', '')
    print(f'REMOÇÃO - {removido}')

for removido8 in remocoes_encontradas8:
    removido8 = removido8.replace('RESOLVE REMOVER, A PEDIDO, O(S) SERVIDOR(ES)ABAIXO:\nMATRÍCULANOMECARGOUNIDADE ORIGEMUNIDADE DESTINODATA INÍCIONÚMERO DO PROC. SEI ', '')
    print(f'REMOÇÃO - {removido8}')

# Alteração de CH
for alteracao in alteracoes:
    alteracao = alteracao.replace('RESOLVE ALTERAR,  A CARGA HORÁRIA:\nMATRÍCULASERVIDORCARGOUNIDADE ORIGEMMUNICÍPIOCARGA HORÁRIA ATUALNOVA CARGA HORÁRIADATA INÍCIO', 'ALTERAÇÃO DE CH - ')
    print(alteracao)

for alteracao_9 in alteracoes9:
    alteracao_9 = alteracao_9.replace('RESOLVE ALTERAR,  A CARGA HORÁRIA:\nMATRÍCULASERVIDORCARGOUNIDADE ORIGEMMUNICÍPIOCARGA HORÁRIA ATUALNOVA CARGA HORÁRIADATA INÍCIO', 'ALTERAÇÃO DE CH - ')
    print(alteracao_9)

for alteracao_8 in alteracoes8:
    alteracao_8 = alteracao_8.replace('RESOLVE ALTERAR,  A CARGA HORÁRIA:\nMATRÍCULASERVIDORCARGOUNIDADE ORIGEMMUNICÍPIOCARGA HORÁRIA ATUALNOVA CARGA HORÁRIADATA INÍCIO', 'ALTERAÇÃO DE CH - ')
    print(alteracao_8)



for curso9 in licenca_curso_encontradas9:
    curso9 = curso9.replace('RESOLVE CONCEDER LICENÇA P/PÓS GRAD (50%) AO(S) SERVIDOR(ES) ABAIXO RELACIONADO(S) PERTENCENTE(S) AO QUADRO DE PESSOAL DO(A) SECRETARIA DA EDUCAÇÃO.\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  ', 'LICENCA PARA CURSO - ')
    print(curso9)

for curso8 in licenca_curso_encontradas8:
    curso8 = curso8.replace('RESOLVE CONCEDER LICENÇA P/PÓS GRAD (100%) AO(S) SERVIDOR(ES) ABAIXO RELACIONADO(S) PERTENCENTE(S) AO QUADRO DE PESSOAL DO(A) SECRETARIA DA EDUCAÇÃO.\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  ', 'LICENCA PARA CURSO - ')
    print(curso8)

# Licença para curso
for curso in licenca_curso_encontradas:
    curso = curso.replace('RESOLVE CONCEDER LICENÇA P/PÓS GRAD (100%) AO(S) SERVIDOR(ES) ABAIXO RELACIONADO(S) PERTENCENTE(S) AO QUADRO DE PESSOAL DO(A) SECRETARIA DA EDUCAÇÃO.\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS  ', 'LICENCA PARA CURSO - ')
    print(curso)



# Designação
for designado in diretores_encontrados:
    designado = designado.replace(', PARA O CARGO EM COMISSÃO DIRETOR', '')
    print(f'DESIGNAÇÃO DIRETOR - {designado}')

for vice in vice_diretores_encontrados:
    vice = vice.replace(', PARA O CARGO EM COMISSÃO VICE-DIRETOR', '')
    print(f'DESIGNAÇÃO VICE-DIRETOR - {vice}')

# Exoneracao
for exo in exoneracao_encontradas:
    print(exo)

for exo9 in exoneracao_encontradas9:
    print(exo9)

for exo8 in exoneracao_encontradas8:
    print(exo8)


# Licenca gestante
for licenca_gest in licenca_gestante_encontradas:
    licenca_gest = licenca_gest.replace('RESOLVE CONCEDER/PRORROGAR LICENÇA À GESTANTE, CONFORME O DISPOSTO NO(A) ART. 154 DA LEI Nº 6.677, DE 26 DE SETEMBRO DE 1994, COM REDAÇÃO DADA PELO ART. 1º DA LEI Nº 12.214, DE 26 DE MAIO DE 2011, À(S) SERVIDORA(S) ABAIXO RELACIONADA(S):\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS', 'LICENCA GESTANTE -')
    print(licenca_gest)

for licenca_gest9 in licenca_gestante_encontradas9:
    licenca_gest9 = licenca_gest9.replace('RESOLVE CONCEDER/PRORROGAR LICENÇA À GESTANTE, CONFORME O DISPOSTO NO(A) ART. 154 DA LEI Nº 6.677, DE 26 DE SETEMBRO DE 1994, COM REDAÇÃO DADA PELO ART. 1º DA LEI Nº 12.214, DE 26 DE MAIO DE 2011, À(S) SERVIDORA(S) ABAIXO RELACIONADA(S):\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS', 'LICENCA GESTANTE -')
    print(licenca_gest9)

for licenca_gest8 in licenca_gestante_encontradas8:
    licenca_gest8 = licenca_gest8.replace('RESOLVE CONCEDER/PRORROGAR LICENÇA À GESTANTE, CONFORME O DISPOSTO NO(A) ART. 154 DA LEI Nº 6.677, DE 26 DE SETEMBRO DE 1994, COM REDAÇÃO DADA PELO ART. 1º DA LEI Nº 12.214, DE 26 DE MAIO DE 2011, À(S) SERVIDORA(S) ABAIXO RELACIONADA(S):\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS', 'LICENCA GESTANTE -')
    print(licenca_gest8)

for licenca_pre in licenca_premio_encontradas:
    licenca_pre = licenca_pre.replace('RESOLVE CONCEDER O DIREITO À LICENÇA-PRÊMIO AO(S) SERVIDOR(ES) INTEGRANTE(S) DO QUADRO DE MAGISTÉRIO PÚBLICO ESTADUAL DESTE ÓRGÃO, ABAIXO RELACIONADO(S):\nMATRÍCULANOMEQUINQUÊNIODATA INÍCIODATA FIMFINALIDADE ', 'LICENCA PREMIO -')
    licenca_pre = licenca_pre.replace(r'\d{2}\.\d{2}\.\d{4}\/\d{2}\.\d{2}\.\d{4}', '')
    print(licenca_pre)

for licenca_pre9 in licenca_premio_encontradas9:
    licenca_pre9 = licenca_pre9.replace('RESOLVE CONCEDER O DIREITO À LICENÇA-PRÊMIO AO(S) SERVIDOR(ES) INTEGRANTE(S) DO QUADRO DE MAGISTÉRIO PÚBLICO ESTADUAL DESTE ÓRGÃO, ABAIXO RELACIONADO(S):\nMATRÍCULANOMEQUINQUÊNIODATA INÍCIODATA FIMFINALIDADE ', 'LICENCA PREMIO -')
    licenca_pre9 = licenca_pre9.replace(r'\d{2}\.\d{2}\.\d{4}\/\d{2}\.\d{2}\.\d{4}', '')
    print(licenca_pre9)

for licenca_pre8 in licenca_premio_encontradas9:
    licenca_pre8 = licenca_pre8.replace('RESOLVE CONCEDER O DIREITO À LICENÇA-PRÊMIO AO(S) SERVIDOR(ES) INTEGRANTE(S) DO QUADRO DE MAGISTÉRIO PÚBLICO ESTADUAL DESTE ÓRGÃO, ABAIXO RELACIONADO(S):\nMATRÍCULANOMEQUINQUÊNIODATA INÍCIODATA FIMFINALIDADE ', 'LICENCA PREMIO -')
    licenca_pre8 = licenca_pre8.replace(r'\d{2}\.\d{2}\.\d{4}\/\d{2}\.\d{2}\.\d{4}', '')
    print(licenca_pre8)

# Interesse particular
for lic_particular in licenca_particular_encontradas:
    lic_particular = lic_particular.replace('RESOLVE CONCEDER LICENÇA PARA TRATAR DE INTERESSE PARTICULAR AO(S) SERVIDOR(ES) ABAIXO RELACIONADO(S) PERTENCENTE(S) AO QUADRO DE PESSOAL DO(A) SEC.\nMATRÍCULANOMECARGODATA INÍCIODATA FIMTOTAL DE DIAS', 'LICENCA POR INTERESSE PARTICULAR -')
    print(lic_particular)














# # Extrair as matrículas de designação
# def designacao (texto):
#     padrao_2


# def extrair_matriculas_com_iniciais_oito(texto):
#     padrao_2 = r"\b8\d{7}\b"
#     matriculas_encontradas2 = re.findall(padrao_2, texto)
#     return matriculas_encontradas2


# def exportar_para_excel(matriculas, nome_arquivo):
#     workbook = xlsxwriter.Workbook(nome_arquivo)
#     sheet = workbook.add_worksheet()
#     sheet.write(0, 0, "MATRICULA")
#     for linha, matricula in enumerate(matriculas, start=1):
#         matricula, nome = matricula
#         sheet.write(linha, 0, matricula)
#         sheet.write(linha, 1, nome)

#     workbook.close()


# exportar_para_excel(matriculas_encontradas, "dados_matriculas.xlsx")
# print('Arquivo exportado em Excel com sucesso!')
