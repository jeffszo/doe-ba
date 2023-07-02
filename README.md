# Extração de matrículas no Diário Oficial - BA

## 🔗 Índice
-   <a href="#📋-sobre">Sobre</a>
-   <a href="#🎯-tecnologias-utilizadas">Tecnologias utilizadas</a>
-   <a href="#🪲-problema---consulta-manual">Problema - Consulta manual</a>
-   <a href="#♨️-como-usar">Como usar</a>
-   <a href="#🌐-referências">Referências</a>

## 📋 Sobre
<p>Projeto desenvolvido para facilitar a busca das matrículas dos professores e gestores escolares no Diário Oficial do Estado da Bahia.</p>

## 🎯 Tecnologias utilizadas:
-   Python
-   re
-   pdfplumber
-   xlsxwriter
  
## 🪲 Problema - Consulta manual
<p>O problema em questão é o demasiado tempo dedicado a consultar os servidores escolares no Diário Oficial. Fazer esse trabalho <strong>TODOS OS DIAS</strong> preenche um espaço do tempo nos servidores da SEC/CPG que poderia ser dedicado em outras tarefas que são mais urgentes.</p>

<br>

- ### Quantidade de matrículas para buscar: 
![Pesquisa das matriculas dos professores](img/search-teacher-doe.png)
![Pesquisa das matriiculas das designações](img/search-designate-doe.png)

<br>

- ### Depois de inserir a palavra-chave...
- ### Pega a matricula, caso seja um professor ou gestor
<img src ='img/preview-doe.png' ></img>
<img src ='img/preview-doe2.png' ></img>


<p>Pensando em maximizar o tempo gasto nisso, resolvi criar essa extração de texto automatizada com o Python.</p>



## ♨️ Como usar
-   Mensagem de boas-vindas
-   Solicitação para inserir o caminho do arquivo PDF
-   Será exibido as matrículas encontradas
-   E depois o aviso de exportação para Excel com sucesso

<br>

### Vídeo demonstrativo:
<video src="video/doe-ba%20%E2%80%93%20diario.py%202023-07-02%2015-32-49%20(online-video-cutter.com).mp4" controls title="Title"></video>
  <br>

### Etapa 1
![Terminal](img/terminal-01.png)
### Etapa 2
![Terminal](img/terminal-02.png)
![Terminal](img/terminal-03.png)

<p><strong>Até então só está disponível a versão via terminal ❗</strong></p>

<br>

## 🌐 Referências
<p>Aprendi alguns conceitos importantes com:</p>
  
  - https://www.youtube.com/@nerddosdados
  - https://www.youtube.com/@WalissonSilva