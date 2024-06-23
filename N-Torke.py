from csv import reader
import csv

ocjene = {}
studenti = []

with open('rezultati.csv', 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    data=[tuple(line) for line in csv.reader(read_obj)]

print("ucenici koji su polozili: ")
for osoba in data:
    ime, prezime, bodovi, ocjena = osoba
    if int(bodovi) >= 50:
        print(osoba)
    if ocjena in ocjene:
        ocjene[ocjena] += 1
    else:
        ocjene[ocjena] = 1
    puno_ime = [ime, prezime]
    studenti.append(puno_ime)
    
print("ukupne ocjene: ")
print(ocjene)

print("ucenici po prezimenu od a do z: ")
poredani = sorted(studenti, key=lambda x: x[1])
counter = 0
for osoba in poredani:
    print(poredani[counter])
    counter += 1
