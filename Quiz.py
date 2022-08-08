print("Seja muito bem vindo ao quiz do Edu!")

answer_user = input("Gostaria de começar? (S/N) ")

if answer_user != "S" and answer_user != "s":
    print("Volte mais vezes S2!")
    quit()

#pontuação
score = 0

print("Iniciando...")

#Question 1
print("\n------- |ESPANÕL| -------\n")
print("La expresión 'rebozar los bistecs' significa: \n (A) Refogar a pernil \n (B) Fritar almôndegas \n (C) Grelhar carne branca \n (D) Cozinhar carne suína \n" )

answer_1 = input("Resposta: ")

if answer_1 == "C" or answer_1 == "c":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

#Question 2
print("\n------- |ENGLISH| -------\n")
print("Como se diz PREDIZER na língua inglesa?: \n (A) Say \n (B) Tell \n (C) Guess \n (D) Foretell \n" )

answer_2 = input("Resposta: ")

if answer_2 == "D" or answer_2 == "d":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

#Question 3
print("\n------- |ENGLISH| -------\n")
print("Na frase, 'This time Im gonna study harder', o que HARDER significa? \n (A) Difícil \n (B) Duro \n (C) Mais \n (D) Forte \n")

answer_3 = input("Resposta: ")

if answer_3 == "C" or answer_3 == "c":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

#Question 4
print("\n------- |ENGLISH| -------\n")
print("Complete: Did you ___ your homework? \n (A) Do \n (B) Done \n (C) Make \n (D) Did \n" )

answer_4 = input("Resposta: ")

if answer_4 == "A" or answer_4 == "a":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

#Question 5
print("\n------- |ESPAÑOL| -------\n")
print("Quando uma pessoa vai a um estabelecimento é pede: 'Quiero un rebanada de ...', significa que deseja um(a): \n (A) Dúzia de ovos \n (B) Uma fatia de pastel \n (C) Porção de Petisco \n (D) Farelo de Cereais \n" )

answer_5 = input("Resposta: ")

if answer_5 == "B" or answer_5 == "b":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

#Question 6
print("\n------- |ESPAÑOL| -------\n")
print("'Ha rebosado lo leche que acalenté ahora mismo'. Qual tradução tem o vocábulo 'rebosado'? \n (A) Ingerir \n (B) esfriar \n (C) Derramar \n (D) Recusar \n " )

answer_6 = input("Resposta: ")

if answer_6 == "C" or answer_6 == "c":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
   print("Resposta Incorreta! \n ")

#Question 7
print("\n------- |ESPAÑOL| -------\n")
print("Se afirmamos que certo alguém é “Un hombre ramplón”, em espanhol refere-se à pessoa?: \n (A) Vulgar  \n (B) Destemível \n (C) Predestinada  \n (D) Pessimista \n" )

answer_7 = input("Resposta: ")

if answer_7 == "A" or answer_7 == "a":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

#Question 8
print("\n------- |ESPAÑOL| -------\n")
print("Quando utiliza-se nas frases o termo “temprano”. Que acepção essa palavra assume? \n (A) De modo \n (B) De lugar \n (C) Meio \n (D) Tempo \n" )

answer_8 = input("Resposta: ")

if answer_8 == "D" or answer_8 == "d":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

#Question 9
print("\n------- |ESPAÑOL| -------\n")
print("Voy a comprar un teléfono inalámbrico a la mañana. O adjetivo inalámbrico caracteriza um modelo de aparelho telefônico: \n (A) Provido de alarme \n (B) Composto de fibra óptica \n (C) Sem fio \n (D) Dotado de rastreador de ligação \n" )

answer_9 = input("Resposta: ")

if answer_9 == "C" or answer_9 == "c":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

#Question 10
print("\n------- |ESPAÑOL| -------\n")
print("O adjetivo 'destellado' tem relação de qualificar algo que é: \n (A) Brilhoso \n (B) Precário \n (C) Singular \n (D) Lindo \n" )

answer_10 = input("Resposta: ")

if answer_10 == "A" or answer_10 == "a":
    print("Resposta Correta! \n ")
    score = score + 1
else : 
    print("Resposta Incorreta! \n ")

print(f"\n | Pontuação Final: {score}/10 |\n")    