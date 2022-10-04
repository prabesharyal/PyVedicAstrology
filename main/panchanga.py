# Panchanga refers tithi, days, nachhyatra, yog and karan.

#Days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
'''I used English format cause it's easier for calculations.'''


lunar_months = ['Chitta', 'Visaka', 'Jyeshta', 'Poorvashada', 'Sravana', 'Poorvabhadra', 'Aswini', 'Kartika', 'Mrigashira', 'Pushyami', 'Makha', 'Uttaraphalguni']

solar_months = ['Chaitra', 'Vyshaka', 'Jyeshta', 'Ashada', 'Shravana', 'Bhadrapadha', 'Asweyuja', 'Kartika', 'Margashira', 'Pushya', 'Magha', 'Phalguna']

tithis = {
    'krishnapaksha': 
[['Prathama','Padyami'], ['Dwitiya','Vidiya'], ['Tritiya','Thadiya'] ,['Chaviti'],['Panchami'],['Shashthi'],['Saptami'],['Ashtami'],['Navami'],['Dasami'],['Ekadasi'],['Dvadasi'],['Trayodasi'],['Chaturdashi'],['Amavasya']
],

'shuklapaksha': [
['Prathama', 'Padyami'],['Dwitiya', 'Vidiya'],['Tritiya', 'Thadiya'],['Chaviti'],['Panchami'],['Shashthi'],['Saptami'],['Ashtami'],['Navami'],['Dashami'],['Ekadashi'],['Dwadashi'],['Thrayodashi'],['Chaturdashi'],['Purnima','Paurnami']
]
}

#print((tithis['krishnapaksha'])[14])
chandramaas = tithis

#Nandadi Tithi
nandraa = (list((tithis['krishnapaksha'])[i] for i in [0,5,10])) #or 'shuklapaksha'
bhadraa = (list((tithis['krishnapaksha'])[i] for i in [1,6,11]))
jayaa = (list((tithis['krishnapaksha'])[i] for i in [2,7,12]))
riktaa = (list((tithis['krishnapaksha'])[i] for i in [3,8,13]))
purnaaa_k = (list((tithis['krishnapaksha'])[i] for i in [4,9,14]))
purnaaa_s = list((tithis['shuklapaksha'])[14])
purnaaa = list()
purnaaa.append([purnaaa_k, purnaaa_s])

#print(purnaaa)

#Fal
kanisthaa = {'shuklapaksha':[list((a for a in nandraa)),list((a for a in riktaa))]}
madhyamaa = {
    'shuklapaksha':[list((a for a in bhadraa)),list((a for a in purnaaa_s))],
    'krishnapaksha':[list((a for a in bhadraa)),list((a for a in purnaaa_k))],
    }
subhaa = {'shuklapaksha':[list((a for a in jayaa))]}
uttamaa = {'krishnapaksha':[list((a for a in nandraa))]}
adhamaa = {'krishnapaksha':[list((a for a in jayaa))]}

# This will be called  and edited whenever necessary at the end.
