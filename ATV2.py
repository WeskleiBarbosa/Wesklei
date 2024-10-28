frutas = {'mação', 'banana', 'abacaxí', 'laranja'}
frutas_encontradas = input("digite o nome de uma fruta").lower()
if frutas_encontradas in frutas:
  print('A fruta está no conjunto.')
else:
  print("A fruta não está no conjunto")