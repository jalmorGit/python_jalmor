# programa que adivina un número entre el 1 y el 10
import random

numero = random.randint(1, 10)
adivina = int(input("Adivina un número entre el 1 y el 10: "))
if adivina == numero:
     print("Has acertado")
else:
     print("Has fallado, el número era", numero)


ram_list = [4, 12, 8, 8]
storage_list = [128, 128, 64, 128]
price_list = [900, 899, 600, 1000]

discounted_price_list = [x - (x*(5/100)) for x in price_list]
print(discounted_price_list)

# asking for customer's budget
budget = int(input('Enter your budget(in dollars): '))
# creating a list of Yes/No based on budget and discounted prices
within_budget = ['Yes' if x <= budget else 'No' for x in discounted_price_list]
print(within_budget)

                                    