Capitals={}
Capitals = dict()
Capitals['Sooma'] = 'Helsingi'
Capitals['Rootsi'] = 'Stockholm'
Capitals['poola'] = 'Varssavi'
Capitals['saksama'] = 'Berliin'
Capitals['iirima'] = 'Dublin'
Capitals['prantsusma'] = 'Pariis'
Capitals['itaalia'] = 'Rooma'
Capitals['hispania'] = 'Madrid'
Capitals['portugal'] = 'Lissabon'
Capitals['tsehhi vabariik'] = 'Praha'
Capitals['austria'] = 'Viin'
Capitals['slovakia'] = 'Bratislava'
Capitals['ungari '] = 'Budapest'
Capitals['sloveenia '] = 'Ljubljana'
Capitals['horvatia'] = 'Zagreb'
Capitals['rumeenia  '] = 'Bukarest'
Capitals['bulgaria  '] = 'Sofia'
Capitals['Kreeka '] = 'Ateena'
Capitals['eesti   '] = 'Tallinn'
Capitals['lati  '] = 'Riia'
Capitals['leedu  '] = 'Vilnius'
Capitals['madalmaad   '] = 'Amsterdam'
Capitals['taani'] = 'Kopenhaagen'
Capitals['malta'] = 'Valletta'
Capitals['kupros'] = 'Nikosia'
Capitals['malta '] = 'Valletta'



























Countries = ['Russia', 'France', 'USA', 'Russia']
for country in Countries:
    if country in Capitals:
        print('Moscow ' + Russia + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)