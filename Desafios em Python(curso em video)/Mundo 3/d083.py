#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = (str(input("Informe uma expressão: ")))        #aqui a expressão é inserida para a verificação
pilha = []                                           #declaramos a pilha

for simb in exp:                        #verifica os símbolos contido na expressão
    if simb == '(':
        pilha.append('(')               #adicionar a abertura do parêntese na lista, caso tenha  na expressão
    elif  simb == ')':                  #se não, se o ")" estiver contido na expressão:
        if len(pilha) > 0:              #se o parêntese aberto foi inserido e o tamanho da pilha é maior  que  0
            pilha.pop()                 #exclui o último elemento da pilha
        else:
            pilha.append(')')           #se não, adicionamos fechamento do parêntese e interrompemos o laço
            break
if len(pilha) ==  0:                    #concluímos que, se o tamanho de pilha for igual a 0
    print("A expressão está correta")   #a expressão está correta
else:
    print("A expressão está incorreta") #se não a expressão está incorreta

