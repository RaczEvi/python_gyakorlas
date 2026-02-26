print("hello")

#ez egy komment

x = 10
print(x)
x = 30
print(x)
y = 1.5456
print(y)

nev = "Valaki"
print(nev)

print([1,2,3,4,5])
print("hello" + " world")
print("hello" + str(12))
print(f"hello {12} {nev}")

tuple_szamok = (2,4)
print(f"szamok: {(1,2,5,7) } tuple_szamok: {tuple_szamok}")
print("tuple_szamok:" + str(tuple_szamok))

lista = [1,1,1,1,1,3,3,4]
print(lista)
halmaz = {1,1,1,1,1,3,3,4}
print(halmaz)

szotar = {"nev": "Anna", "kor": 20 }
print(szotar)
logikai = False
print(logikai)

ertek = None
print(ertek)

szam1 = 11
nev = "Jani"
Nev = "Jozsi"
print(nev + " es " + Nev + " baratok")

PI = 3.14
print(PI)
print(1.5 + 2 * 3 - 4 / 2 + 0.5)

x = 5
y = 3
print("x mod y: " + str(x % y))
print("Harom az erteke az y-nak? " + str(y) == 3)
print("Harom az erteke az y-nak? " + str(y == 3))

x = 5
y = 10
if y > 5:
    print("y nagyobb mint 5")
if y % 2 == 0:
    print("y paros es nagyobb mint 5")
else:
    print("y kisebb vagy egyenlo mint 5")

for i in range(5):
    print(i)
for nev in ["Anna", "Jani", "Jozsi"]:
    print(nev)

print("vege")

while y < 10:
    print("y meg kisebb mint 10")
    y = (y + 1)
    print("y erteke: " + str(y))

def fuggveny():
    print("Ez egy fuggveny")
    return "Alma"
print("kovetkezo sor")
fuggveny()

print ( " A fuggveny hozzaadott egy "+ fuggveny() + "-t")
