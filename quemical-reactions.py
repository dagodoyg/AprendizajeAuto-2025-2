molecules = ["H2", "O2", "H2O", "CO2", "CH4", "O2", "CO2"]  # list (duplicates allowed)
reaction_types = {"combustion", "oxidation", "hydrolysis"}  # set
reactions = {
    "combustion": ["CH4", "O2", "CO2", "H2O"],
    "oxidation": ["Fe", "O2", "Fe2O3"],
    "hydrolysis": ["NaCl", "H2O", "NaOH", "HCl"]
}

# Task: Find molecules that appear in ≥2 reaction types

mol = set(molecules)

for m in mol:
    count = 0
    for r in reaction_types:
        if m in reactions[r]:
         count += 1
    if count >= 2:
        print(m)
