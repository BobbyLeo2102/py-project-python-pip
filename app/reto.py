def get_world_percentages(data):
  percentages_dict=
  {item['Country/Territory']}: item['World Population Percentage'] for item in data

names = percentages_dict.keys()
per = percentages_dect.values()

return names, per

#prueba para resolver el reto de graficar porcentaje de poblacion por paises