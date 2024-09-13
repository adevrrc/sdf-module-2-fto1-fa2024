# Define a variable as a Dictionary
hockey_teams = {
    "Winnipeg": "Jets",
    "Edmonton": "Oilers",
    "Calgary": "Flames"
}

print(type(hockey_teams))
print(hockey_teams)

# Access Dictionary elements
print(hockey_teams["Winnipeg"])

# Redefine element value
hockey_teams["Calgary"] = "Lames"
print(hockey_teams["Calgary"])

# Dictionary Functions
print(hockey_teams.keys())
print(hockey_teams.values())
print(hockey_teams.items())
print(hockey_teams.get("Winnipeg"))

best_team = hockey_teams("Winnipeg")
print(best_team)
print(hockey_teams)

hockey_teams.clear()
print(hockey_teams)

# Other methods
# copy()
# popitem() # removes last inserted key-value pair
# setdefault(keyname, value) # if the key does not exist, the key-value pair is inserted
