people = [
    {"Name": "Zinedine Zidane", "Nationality": "French"},
    {"Name": "Robert Lewandowski", "Nationality": "Polish"},
    {"Name": "Pierre Emrick Aubameyang", "Nationality": "Gabonese"},
    {"Name": "Gareth Bale", "Nationality": "Welsh"}
]

people.sort(key=lambda person: person["Name"])

print(people)