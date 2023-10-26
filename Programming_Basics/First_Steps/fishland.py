skumriya = float(input())
caca = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_cena = (skumriya * 160 / 100) * palamud_kg

safrid_cena = (caca * 180 / 100) * safrid_kg
midi_cena = midi_kg * 7.50

smetka = palamud_cena + safrid_cena + midi_cena

print("{:.2f}".format(smetka))
