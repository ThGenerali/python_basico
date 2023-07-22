#Leitura de dados - temos três maneiras simples de lermos os dados de um arquivo.

#read() - Lê todas as linhas do arquivo de uma única vez 
arquivo = open('arquivo.txt', 'r')
leitura = arquivo.read()
arquivo.close()
print(leitura)

#readlines() - Retorna uma lista de strings, onde cada elemento corresponde a uma linha do arquivo
arquivo = open('arquivo.txt', 'r')
leitura = arquivo.readlines()
arquivo.close()
print(leitura)

#write() - Recebe como parâmetro uma string contendo o texto a ser inserido. Usando o método rstrip, tira os \n do arquivo, tanto na hora da escrita, como na hora da leitura do arquivo.
arquivo = open('arquivo.txt', 'a')
arquivo.write('Olá pessoal!\n')
arquivo.close()
arquivo = open('arquivo.txt', 'r')
leitura = arquivo.read()
arquivo.close()
print(leitura)

#writelines() - Recebe como parâmetro uma estrutura de dados que seja iterável. Usando o método rstrip, tira os \n do arquivo, tanto na hora da escrita, como na hora da leitura do arquivo.
linhas = ['Hello World!\n',
          'texto em lista\n',
          'aplicação do writelines\n']
arquivo = open('arquivo.txt', 'a')
arquivo.writelines(linhas)
arquivo.close()
arquivo = open('arquivo.txt', 'r')
leitura = arquivo.read()
arquivo.close()
print(leitura)