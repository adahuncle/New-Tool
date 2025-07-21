class Compound:
    def __init__(self, name, formula, molMass, mp, bp):
        self.name = name
        self.formula = formula
        self.molMass = molMass
        self.mp = mp
        self.bp = bp

    def __repr__(self):
        return f"Name: {self.name}, Formula: {self.formula}, Molar Mass: {self.molMass} g/mol, Melting Point: {self.mp} °C, Boiling Point: {self.bp} °C"
    
class CompoundLibrary:
    def __init__(self):
        self.compounds = []

    def add_compounds(self, compound):
        for c in self.compounds:
            if c.name == compound.name:
                print (f"Compound '{compound.name}' already exists.")
                return
        self.compounds.append(compound)

    def remove_compounds(self, name):
        for c in self.compounds:
            if c.name == name:
                self.compounds.remove(c)
                print(f"Compound '{name}' removed.")
                return
        print(f"Compound '{name}' does not exist.")

    def search_compounds(self, name):
        for c in self.compounds:
            if c.name == name:
                print(c)
                return
        print(f"Compound '{name}' not found.")
            
    def list_compounds(self):
        for c in self.compounds:
            print (c)

def parse_compound_file(filename):
    compounds = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    for i in range(0, len(lines), 5):
        name = lines[i].split(": ")[1]
        formula = lines[i+1].split(": ")[1]
        molMass = float(lines[i+2].split(": ")[1])
        mp = float(lines[i+3].split(": ")[1])
        bp = float(lines[i+4].split(": ")[1])
        compound = Compound(name, formula, molMass, mp, bp)
        compounds.append(compound)

    return compounds