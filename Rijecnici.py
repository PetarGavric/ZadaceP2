import random

ucenici = {}
broj_ocjena = {}
polozeno = 0

studenti = [
    'Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
    'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
    'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
    'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
    'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun'
]
    
for student in studenti:
    random_ocjena = random.randint(1, 5)
    ucenici[student] = random_ocjena
    if random_ocjena in broj_ocjena:
        broj_ocjena[random_ocjena] += 1
    else:
        broj_ocjena[random_ocjena] = 1
    if random_ocjena > 1:
        polozeno += 1

postotak = int(polozeno / len(studenti) * 100)

print(ucenici, "\n\nbroj ocjena: ", broj_ocjena, "\n\nPostotak prolaznosti: ", postotak, "%")
