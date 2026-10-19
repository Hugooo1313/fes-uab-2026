###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom_tecnic = str(input("Nom del tècnic:"))
nom_xarxa = str(input("Nom de la xarxa"))
print(f"Nom del tècnic:{nom_tecnic}, Nom de la xarxa: {nom_xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud_fibra = float(input("Longitud de l'enllaç de fibra en Km:"))
velocitat_transmició = float(input("Velocitat de transmició en Gbps"))
temps = 8 / velocitat_transmició

print(f"L'enllaç de {longitud_fibra}km necessita {temps} segons pero transmetre 1GB")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores_feina = float(input("Hores de feina:"))
preu_hora = float(input("Preu per hora en €:"))
preu_material = float(input("Preu del material:"))

cost_total = (hores_feina*preu_hora) + preu_material
print(f"El cost total serà de: {cost_total} euros.")