#Calculadora de raiz quadrada
import math

print("SUPER RAIZ QUADRADA")

#Socilita o nome e senha do usuario
name = str(input("Login: "))
password = str(input("Password: "))

#Exibe o nome e senha
print("Bem vindo %s" + " " + name)
print("Senha: %s" + " " + password)

#Usuario entra com o numero para tirar a raiz
n1 = int(input("Digite o numero para tirar a raiz: "))

if(n1 == 0):
    print("Error")

#Calcula e mostra a raiz quadrada do numero digitado    
def raiz():
    n2 = math.sqrt(n1)

    if(n2 % 2 == 0):
        print type(n2)
        print(int(n2))
    else:
        print type(n2)
        print(float(n2))
        
raiz()