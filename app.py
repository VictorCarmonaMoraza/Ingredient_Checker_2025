
##Ingredientes: Lo definiremos como un conjunto
#harina,azucar, mantequilla
ingredients ={"flour","sugar","butter"}

print(ingredients)

#agregar huevos
ingredients.add("eggs")
print(ingredients)

#Eliminar un ingrediente
ingredients.remove("flour")
print(ingredients)

#Los conjuntos no tendran nunca duplicados
##Operaciones
conjunto_a = {"flour","sugar","butter"}
conjunto_b = {"sugar","eggs"}

#Unir dos conjuntos
print(conjunto_a | conjunto_b)  # {'eggs', 'flour', 'sugar', 'butter'}

#interseccion de dos conjuntos
print(conjunto_a & conjunto_b)  #{'sugar'}

#diferencia entre dos conjuntos
print(conjunto_a-conjunto_b)  #{'butter', 'flour'}



