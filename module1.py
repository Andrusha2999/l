def Strana(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="1":
        mas=[]
        capital=(input("vvedite pealinn: ")).capitalize()
        capital.title()
        for i in values_list:
            if i==capital:
                for i in range(len(values_list)):
                    if values_list[i]==capital:
                        mas.append(int(i))
                        print("Strana -", keys_list[i],"<-->", "pealinn -", values_list[i])
    else:
        Strana=(input("Vvedite Stranu: ")).capitalize()
        a=d.get(Strana)
        print("Strana -", Strana ,"<-->", "Stoli2a -", a)
    return

def new_key_value(d:dict):
    new={}
    Strana=(input("vvedite  stranu: ")).capitalize()
    capital=(input("vvedite pealinn: ")).capitalize()
    new={Strana:capital}

    return d,new