#Criação, Abertura e Fechamento de Arquivos
#Criação - Usa a função open() na qual já abre o arquivo. 
#Dentro da função open(), utiliza o nome do arquivo e o modo de uso como argumento.
#Open(arquivo, modo)

#Modos - cada modo tem sua função, na qual permite ler e escrever

#Modo 'r' - Modo somente leitura
leitura = open('arquivo.txt', 'r')
print(f'Modo somente leitura {leitura}')

#Modo 'w' - Modo de escrita. Cria um arquivo, caso ainda não exista, ou substitui o arquivo atual.
open('Arquivo.txt', 'w')
print ('Cria ou substitui o arquivo.')

#Modo 'x' - Modo de escrita. Cria um arquivo, se o arquivo já retorna um erro.
open('ArquivO.txt', 'x')
print('Modo de escrita. Cria um arquivo, caso exista retorna erro.')

#Modo 'a' - Modo de escrita. Cria um arquivo, caso ainda não exista. Se o arquivo existi, novas escritas serão adicionadas ao final dele.
open('Arquivo.txt', 'a')
print('Modo de escrita. Cria um arquivo, caso ainda não exista. Se o arquivo existi, novas escritas serão adicionadas ao final dele')

#Modo - 't' - Abre o arquivo no modo texto (modo padrão)
open('Arquivo', 't')
print('Abrindo arquivo no modo texto')

#Modo - 'b' - Abre o arquivo no modo binário
open('ARquivo.txt', 'b')
print('Abrindo arquivo em modo binário')

#Fechamento de Arquivos - No final de todo processo utilizados a função close() para fechar o arquivo e evitar perda de dados ou um arquivo corrompido

#close()
leitura.close()
print('Fechando arquivo.')