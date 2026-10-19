###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom_encaminador = "Router Habitació"
ubicació = "Habitació"
nombre_ports = 8
encaminador_encès = True

print(
    f"Encaminador: {nom_encaminador}; ubicació:{ubicació}; ports:{nombre_ports}; Encès?: {encaminador_encès}"
)

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

GB_inclosos = 20
GB_consumits = 13
GB_restants = GB_inclosos - GB_consumits
print(f"GB contractats: {GB_inclosos}, GB consumits: {GB_consumits}, GB restants: {GB_restants} ")