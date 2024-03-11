#Proyecto 2 Calculadora
def sumar(a, b):    
    return a + b

def restar(a, b):
    return a - b

def dividir(a,b):
    return a / b

print('Bienvenido a la calculadora basica ')

#Definimos 
a = int(input('Escribe el primer numero a calcular: '))
b = int(input('Escribe el segundo numero a calcular: '))

operacion = input('Selecciona la operacion a hacer (+, -, /): ')

if operacion == '+': 
    print('Tu resultado es: ', sumar(a, b))
elif operacion == '-':
    print('Tu resultado es: ', restar(a, b))
elif operacion == '/':
    print('Tu resultado es: ', dividir(a, b))
else:
    print('Operación no válida. Por favor, selecciona +, - o /.')
