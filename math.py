#Calculadora de raiz quadrada
import math

print("SUPER RAIZ QUADRADA")

#Socilita o nome e senha do usuario
name = str(input("Login: "))
password = str(input("Password: "))

#Exibe o nome e senha
print(str("Bem vindo "), str(name))

resposta = ""
while(resposta == ""):
    resposta = str(input("Mostrar senha?: S ou N"))
    if(resposta == "S"):
        print(str("Senha: "), str(password))
    elif(resposta == "N"):
        print(str("Senha: ", str("--------")))

#Solicita o numero para tirar a raiz
n = 0
if(name != "" and password != ""):
    while(n == 0):
        n = int(input("Digite o numero para tirar a raiz: "))

#Calcula e mostra a raiz quadrada do numero digitado    
def raiz():
    r = math.sqrt(n)
    if(r % 2 == 0):
        print(str("Numero: "), int(n))
        print(str("Raiz:"), float(r))
        print(type(r))
    else:
        print(str("Numero: "), int(n))
        print(str("Raiz"), float(r))
        print(type(r))
        
if(name != "" and password != ""):
    raiz()
elif(name == "" and password == ""):
    print("Internal error")

print("fim")