# frase = 'Curso em Video Python'
# print(frase[1::2])

#print(len(frase))

#print(frase.replace('Python', 'Android'))       # troca as palavras por outras

#print(frase.upper()) #ou lower            # tudo maiusculo

#print(frase.find('Video'))     # mostra em qual caractere comeca a palavra           rfind - find reverso

#print(frase.count('o'))       # conta quantos caracteres especificos

#print(frase[9:])            # Lugar que comeca e termina de printar

#print(frase.capitalize())     # 1 letra maiuscula e o resto minuscula

#print(frase.title())           # letras que comecam palavras em maiuscula

#frase.strip()           #remove espacos inuteis no comeco e no final
   #frase.rstrip()       # remove da direita(ultimos)
   #frase.lstreip        # remove os da esquerda(primeiras)

#frase.split()            # tira os espacos e recomeca a contar os caracteres em cada palavra

#'-'.join(frase)

###########################################################################

#EX-22

# nome = input('Digite seu nome: ').strip()
# print(nome.upper())
# print(nome.lower())
# nodi = nome.split()
# print(len(nodi[0]))
# print(len(nome) - nome.count(' '))

###########################################################################

#EX-23

# numero = str(input('Digite um numero de 0 a 9999: '))
#
# print(numero[0])
# print(numero[1])
# print(numero[2])
# print(numero[3])

###########################################################################

 #cd = str(input('Digite sua cidade: '))
 #cida = cd.lower()
 #if cida.find('santo') == 0:
  #   print('Sua cidade comeca com Santo')
 #else: print('Sua cidade nao comeca com Santo')

###########################################################################

#EX-25

# nome = str(input('Digite seu nome: '))
# nomel = nome.lower()
# if nomel.find('silva') >= 0:
#     print('Voce tem Silva no nome')
# else:
#     print('Voce nao tem Silva no nome')

###########################################################################

#EX-26

frase = str(input('Digite uma frase: '))
fraselo = frase.lower()
print(f'A frase tem {fraselo.count('a')} a no meio')
print(f'A primeira vez que A aparece e {fraselo.find('a')}')
print(f'A ultima vez que A aparece e {fraselo.rfind('a')}')

###########################################################################

#EX-27

#nome = str(input('Digite seu nome: '))
#nomese = nome.split()
#print(nomese[0])
