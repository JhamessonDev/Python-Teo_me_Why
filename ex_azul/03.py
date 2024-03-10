# Faça um programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvet: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme e chocolate
# Cobertura: caramelo (R$!,50), morango (R$!,50) chocolate (R$!,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

tipo_sorvete = input('Entre com o tipo do sorvete: [casquinha/cascão/cestinha]: ')
sabor = input('Entre com o sabor do sorvete: [morango/creme/chocolate]: ')
cobertura = input('Entre com a cobertura que você quer: [caramelo/morango/chocolate]: ')

valor = 0

# Tipo de sorvete
if tipo_sorvete == 'casquinha':
    valor = valor + 1

elif tipo_sorvete == 'cascão':
    valor += 2.5

elif tipo_sorvete == 'cestinha':
     valor += 4

else:
    print('Escolha corretamente')

# Cobertura
coberturas = 'caramelo, morango, chocolate'
if cobertura in coberturas:
    valor += 1.5

elif cobertura == '':
    pass

else:
    print('Escolha uma cobertura válida')


print(f'Seu sorvete de {tipo_sorvete} de {sabor}, cobertura de {cobertura}, custará {valor}')