from module1 import*
Strana_dict={"Austria": "Viin", ## Loome tühi sõnastik Capitals
"Belgia": "Brüssel",
"Eesti":  "Tallinn",
"Saksamaa":" Berliin",
"Iirimaa": "Dublin",
 "Liechtenstein": "Vaduz",   ## Täida oma väheste väärtustega
"Holland": "Amsterdam",
 "Prantsusmaa":"Pariis",
"Bulgaaria": "Sofia",
 "Poola ": "Varssavi ",
"Tšehhi ": "Praha ",
"Albaania ": "Tirana ",
"Bosnia ja Hertsegoviina": "Sarajevo ",
"Põhja-Makedoonia ": "Skopje ",
 "Serbia ": "Belgrad "}
print(Strana_dict )
while True:
    print("privet! Пройдёмся по странам и их столицам!")
    print("1 - leidke riik  pealinna järgi ja pealinna riigi järgi .,\n2 - lisa uus riik ja pealinn,\n4 Проверяем знания -")
    menu=input()
    if menu=="1":
        v=input("iskat po strane stolitsu(1) ILI pealinn po STRANE(2)? ")
        Strana(Strana_dict,v)
    elif menu=="2":
        new_key_value(Strana_dict)
        