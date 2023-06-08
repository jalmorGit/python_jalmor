# programa que adivina un número entre el 1 y el 10
import random

numero = random.randint(1, 10)
adivina = int(input("Adivina un número entre el 1 y el 10: "))
if adivina == numero:
     print("Has acertado")
else:
     print("Has fallado, el número era", numero)







                                    