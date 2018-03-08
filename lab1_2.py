#!python3
import random
done = False
while done == False:		# Petla, ktora bedzie dzialala dopoki nie podamy prawidlowych granic
	try:
		a = int(input("Podaj dolny zakres: "))
		b = int(input("Podaj gorny zakres: "))
		if a > b:	# Sprawdza, czy dolna granica nie jest wieksza od gornej
			raise ValueError("Zle granice, sprobuj jeszcze raz.")
		c = random.randint(a,b)
		done = True
		zgadnij = False
		while zgadnij == False:		# Petla, ktora bedzie dzialala, dopoki nie zgadniemy
			d = int(input("Zgadnij liczbe: "))
			if c == d:
				print("Gratulacje XD")
				zgadnij = True
			elif c > d:
				print("Za mala liczba! Sprobuj jeszcze raz.")
			else:
				print("Za duza liczba! Sprobuj jeszcze raz.")

	except ValueError as e:
		print(e)
