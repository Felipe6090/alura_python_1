import hang, guessing

print('*****************************')
print('bem vindo, escolha seu jogo: ')
print('*****************************')

print("(1) Forca (2) Adivinhação")

choosed_game = int(input("Qual jogo? "))

if(choosed_game == 1):
    hang.execute()
elif(choosed_game == 2):
    guessing.execute()