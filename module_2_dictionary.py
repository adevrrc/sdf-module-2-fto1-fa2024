# Syntax for dictionaries
# {key: value, key: value, key: value}
hockey_teams = {
    "winnipeg": "jets",
    "edmonton": "oilers",
    "calgary": "flames"
}

print(type(hockey_teams))

print(hockey_teams)

print(f"My favorite hockey team is the {hockey_teams["winnipeg"].title()}.")

hockey_teams["calgary"] = "hitmen"

print(hockey_teams)

print(hockey_teams.keys())

print(hockey_teams.values())

print(hockey_teams.items())

print(hockey_teams.get("winnipeg"))

#print(hockey_teams["winnipe"])

hockey_teams.clear()

print(hockey_teams)
