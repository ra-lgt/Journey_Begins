

#dataset=pd.read_excel('bus_list.xlsx')
class Data_set:
    data={'Tiruchirapalli': {'Chennai': ['NorthLay', 200, 'Tiger ', 450, 'Circum', 300, 'Cube', 450, 'Hippie', 450]}, 'Velankanni': {'Chennai': ['Amity', 300, 'Fastmove', 500, 'Mega', 350, 'UniRide', 200, 'Master', 550, 'Lion', 400]}, 'Chennai ': {'Selam': ['Calm', 500, 'Lava', 700, 'Yellow', 350, 'Fun', 600, 'Bus4U', 750]}, 'Chennai': {'Kumbakonam': ['Solid', 600, 'Instant', 550, 'Angel', 800, 'Big', 450, 'Pop', 400], 'Hosur': ['Fast', 500, 'Rainbow', 800, 'Bold', 689, 'Blue', 650, 'Break Away', 520]}, 'Madurai': {'Chennai': ['Go', 650]}, 'Mattuthavani': {'Koyambedu': ['Magic ', 400, 'Ace', 200, 'Shaker', 700, 'Mini', 650, 'A2Z', 351]}, 'Coimbatore': {'Tenkasi': ['Rapid', 300, 'Sundhara', 420], 'Chennai': ['Safe', 600, 'Abacus', 350, 'Amazing', 325, 'Dance Fever', 140]}}
"""
for froms in dataset["Froms"]:
    data[froms]={}

for froms,to in zip(dataset["Froms"],dataset["To"]):
    if(froms in data):
        data[froms][to]=list()

for froms,to,name,fare in zip(dataset["Froms"],dataset["To"],dataset["Name"],dataset["Fare"]):
    data[froms][to].append(name)
    data[froms][to].append(fare)
 {% for i in range(length)%}
 {{depature}}
 {{dataset[i]}}
print(data)
"""
