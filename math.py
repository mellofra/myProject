#Calculadora de raiz quadrada
import math

print("SUPER RAIZ QUADRADA")

#Socilita o nome e senha do usuario
name = str(input("Login: "))
password = str(input("Password: "))

#Exibe o nome e senha
print("Bem vindo %s" + " " + name)
print("Senha: %s" + " " + password)

#Solicita o numero para tirar a raiz
n = 0
while(n == 0):
    n = int(input("Digite o numero para tirar a raiz :"))

#Calcula e mostra a raiz quadrada do numero digitado    
def raiz():
    r = math.sqrt(n)

    if(r % 2 == 0):
        print(type(r))
        print(int(r))
    else:
        print type(r)
        print(float(r))      
        
raiz()

print("fim")