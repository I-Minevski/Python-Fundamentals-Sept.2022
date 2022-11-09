countries=input().split(", ")
capitals=input().split(", ")
final={countries[index]:capitals[index] for index in range(len(countries))}

#final=dict(zip(countries, capitals)) ebasi qkoto stava s toq zip a?

for (country, capital) in final.items():
    print(f"{country} -> {capital}")