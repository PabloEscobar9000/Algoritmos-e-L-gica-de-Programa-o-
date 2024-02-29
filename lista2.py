#1
print('1º\n')
lado1 = int(input('Digite o lado 1: '))
lado2 = int(input('Digite o lado 2: '))
lado3 = int(input('Digite o lado 3: '))

if(lado1+lado2>lado3 or lado1+lado3>lado2 or lado3+lado2>lado1):
    
    print('eh triangulo')

    if(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        print('escaleno')
        

    elif (lado1 == lado2 == lado3):
        print('equilatero')

    elif (lado1==lado2 or lado1==3 or lado2==lado3):
        print('isosceles')

else:
    {
        print('nao eh triangulo')
    }

#2
print('---------------------')
print('2º\n')
ano = int(input('Digite o Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')

#3
print('---------------------')
print('3º\n')
peso = float(input('digite o peso: '))

if(peso>50):
    excesso = peso-50
    multa = excesso*4

    print(f'o excesso foi de {excesso}kg')
    print(f'a multa sera de {multa}R$')

else:
    {
        print('nao houve excesso de peso')
    }

#4
print('---------------------')
print('4º\n')
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))

if(valor1>valor2 and valor1>valor3):
    print('O primeiro valor eh o maior')

elif valor2>valor1 and valor2>valor3:
    print('O segundo valor eh o maior')
else:
    {
        print('O terceiro valor eh o maior')    
    }

#5
print('---------------------')
print('5º\n')

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))

if(valor1<valor2 and valor1<valor3):
    print('O primeiro valor eh o menor')

elif valor2<valor1 and valor2<valor3:
    print('O segundo valor eh o menor')
else:
    {
        print('O terceiro valor eh o menor')    
    }

#6

print('---------------------')
print('6º\n')

ganHora = float(input('Digite quanto vc ganha por hora: '))
hrsTrab = float(input('Digite as horas trabalhadas no mês: '))

salarioBruto = ganHora*hrsTrab
desconto = (11/100*salarioBruto)+(8/100*salarioBruto)+(5/100*salarioBruto)
salarioLiquido = salarioBruto - desconto

print(f'ao INSS pagou {8/100*salarioBruto}R$')
print(f'ao sindicato pagou {5/100*salarioBruto}R$')

print(f'O salario bruto eh: {salarioBruto}')
print(f'O salario liquido eh: {salarioLiquido}')

#7
print('---------------------')
print('7º\n')

tamPintar = float(input('Digite o tamanho a ser pintado em metros quadrados: '))

latas = (tamPintar/3)
preco = latas*80.

latasNece = round(latas, 0)

print(f'latas necessarias: {latasNece}')
print(f'preco total: {preco:.2f}R$')
































     
    
    
