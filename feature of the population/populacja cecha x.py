"""
z populacji generalnej n = 50 pobrano elementarną próbkę i przebadano ze względu na cechę X. Otrzymano wyniki:
3.6, 5.0, 4.0, 4.7, 5.2, 5.9, 4.5, 5.3, 5.5, 3.9, 5.6, 3.5, 5.4, 5.2, 4.1, 5.0, 3.1, 5.8, 4.8, 4.4, 4.6, 5.1, 4.7, 3.0, 5.5, 6.1, 3.8, 4.9, 5.6, 6.1, 5.9, 4.2, 6.4, 5.3, 4.5, 4.9, 4.0, 5.2, 3.3, 5.4, 4.7, 6.4, 5.1, 3.4, 5.2, 6.2, 4.4, 4.3, 5.8, 3.7

zbadaj:
- ilosc klas
- szerokosc pojedynczej klasy
- ilosc elementow w klasie

stworz histogram
"""

from math import floor
from math import sqrt
import csv

# spis wszystkich zbadanych wartosci
results = [3.6, 5.0, 4.0, 4.7, 5.2, 5.9, 4.5, 5.3, 5.5, 3.9, 5.6, 3.5, 5.4, 5.2, 4.1, 5.0, 3.1, 5.8, 4.8, 4.4, 4.6, 5.1, 4.7, 3.0, 5.5, 6.1, 3.8, 4.9, 5.6, 6.1, 5.9, 4.2, 6.4, 5.3, 4.5, 4.9, 4.0, 5.2, 3.3, 5.4, 4.7, 6.4, 5.1, 3.4, 5.2, 6.2, 4.4, 4.3, 5.8, 3.7]
results_rising = sorted(results)

# ilosc zbadanych elementow
size = len(results)

# liczba klas
classes = sqrt(size)
classes = floor(classes)

# szerokosc pojedynczej klasy
max = max(results)
min = min(results)

# roznica miedzy najwieksza i najmniejsza wystepujaca wartoscia
delta = max - min

# szerokosc klasy zaokraglona do 2 miejsca po przecinku (0,49 tak jak na cwiczeniach)
width_of_class = round(delta/classes, 2)

if(width_of_class * classes >= delta):
    print("szerokosc klasy jest odpowiednia")
else:
    print("zla szerokosc klasy")

print("posortowane zbadane wartosci: ", results_rising)
print("liczba zbadanych wartosci: ", size)
print("wartosc min: ", min)
print("wartosc max: ", max)
print("ilosc klas: ", classes)
print("szerokosc pojedynczej klasy: ", width_of_class)

class1 = []
class2 = []
class3 = []
class4 = []
class5 = []
class6 = []
class7 = []

for i in range(0, size):
    if (results_rising[i] >= 3.0 and results_rising[i] < 3.49):
        class1.append(results_rising[i])
    elif (results_rising[i] >= 3.49 and results_rising[i] < 3.98):
        class2.append(results_rising[i]) 
    elif (results_rising[i] >= 3.98 and results_rising[i] < 4.47):
        class3.append(results_rising[i])   
    elif (results_rising[i] >= 4.47 and results_rising[i] < 4.96):
        class4.append(results_rising[i]) 
    elif (results_rising[i] >= 4.96 and results_rising[i] < 5.45):
        class5.append(results_rising[i]) 
    elif (results_rising[i] >= 5.45 and results_rising[i] < 5.94):
        class6.append(results_rising[i]) 
    elif (results_rising[i] >= 5.94 and results_rising[i] < 6.43):
        class7.append(results_rising[i]) 

elements_checker = len(class1 + class2 + class3 + class4 + class5 + class6 + class7)

if elements_checker != size:
    print("niepoprawna liczba elementow w jednej z klas. \n")
else:
    print("liczba elementow jest poprawna! \n")

print("class1 wartosci:", class1, "\nclass1 liczba elementow: ", len(class1))
print("class2 wartosci:", class2, "\nclass2 liczba elementow: ", len(class2))
print("class3 wartosci:", class3, "\nclass3 liczba elementow: ", len(class3))
print("class4 wartosci:", class4, "\nclass4 liczba elementow: ", len(class4))
print("class5 wartosci:", class5, "\nclass5 liczba elementow: ", len(class5))
print("class6 wartosci:", class6, "\nclass6 liczba elementow: ", len(class6))
print("class7 wartosci:", class7, "\nclass7 liczba elementow: ", len(class7))

# dopisywanie wartosc do pliku CSV
#kolumna 1: indeks klasy, kolumna 2: liczba elementow w klasie
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=";")

    writer.writerow(('class1', len(class1)))
    writer.writerow(('class2', len(class2)))
    writer.writerow(('class3', len(class3)))
    writer.writerow(('class4', len(class4)))
    writer.writerow(('class5', len(class5)))
    writer.writerow(('class6', len(class6)))
    writer.writerow(('class7', len(class7)))

# dopiswanie wartosci do pliku TXT
#kolumna 1: indeks klasy, kolumna 2: liczba elementow w klasie
plik = open("data.txt", "w")

plik.write((str(1) + " " + str(len(class1))))
plik.write("\n")
plik.write((str(2) + " " + str(len(class2))))
plik.write("\n")
plik.write((str(3) + " " + str(len(class3))))
plik.write("\n")
plik.write((str(4) + " " + str(len(class4))))
plik.write("\n")
plik.write((str(5) + " " + str(len(class5))))
plik.write("\n")
plik.write((str(6) + " " + str(len(class6))))
plik.write("\n")
plik.write((str(7) + " " + str(len(class7))))

plik.close()

"""
gnuplot:
	set tics font "Helvetica,15" 
	set ytics 1		odstep na osi y co 1 miejsce
	set xtics 1		odstep na osi x co 1 miejsce

    set xlabel "numer klasy"                legenda
	set ylabel "liczba elementow"           legenda

    plot "data.txt" u 1:2 t "liczba elementow w danej klasie" w lp 

"""