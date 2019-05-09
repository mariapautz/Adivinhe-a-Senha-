import random #importa para a execução do sorteio da senha
valor_tentativa = 0 #vai ser útil para o while de tentativas maximas que o usuario pode executar
digitos_senha = 0 #digitos que devem ir até 5
senha = "" #a senha
while digitos_senha <5:
    sorteio = str(random.randrange(1,10))
    senha += sorteio #senha vai receber os digitos sorteados
    digitos_senha += 1 #a cada numero sorteado receberá 1 para somar


lista=[senha[0], senha[1], senha[2], senha[3], senha[4]] #lista com todos os digitos da senha
while valor_tentativa <= 10: #as tentativas nao podem ultrapassar 10
    tentativa1 = input('Insira sua tentativa: ')
    if tentativa1[0] in lista: #se a tentativa estiver na senha
        valor= ' 0' #0 pois indica que o digito está em qualquer lugar da senha
        if tentativa1[0] == senha[0]:
            valor = ' +1' #se o digito inserido estiver no mesmo valor da senha, ele recebe +1
    else:
        valor=' -1'
    if tentativa1[1] in lista:
        valor1=' 0'
        if tentativa1[1]==senha[1]:
            valor1 = ' +1'
    else:
        valor1 = ' -1'
    if tentativa1[2] in lista:
        valor2=' 0'
        if tentativa1[2]==senha[2]:
            valor2 = ' +1'
    else:
        valor2 = ' -1'
    if tentativa1[3] in lista:
        valor3=' 0'
        if tentativa1[3]==senha[3]:
            valor3 = ' +1'
    else:
        valor3 = ' -1'
    if tentativa1[4] in lista:
        valor4=' 0'
        if tentativa1[4]==senha[4]:
            valor4 = ' +1'
    else:
        valor4 = ' -1'
    
    print (valor+valor1+valor2+valor3+valor4) #aqui vai printar todos os valores que a senha para adivinhar recebeu
    if valor == " +1" and valor1 == " +1" and valor2 == " +1" and valor3 == " +1" and valor4 == " +1": #vai conferir se todos os numeros estão iguais
        print ('Parabéns! Você ganhou!') 
        break
    else:
        valor_tentativa += 1 #se nao forem iguais, as tentativas vao se acumulando até 10

    




            
