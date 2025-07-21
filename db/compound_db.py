import sqlite3

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
        self.conn = sqlite3.connect("compounds.db")
        self.cursor = self.conn.cursor()

    def add_to_db(self, compound):
        try:
            self.cursor.execute("""
                INSERT INTO compounds (name, formula, molar_mass, mp, bp)
                                VALUES (?, ?, ?, ?, ?)
            """, (compound.name, compound.formula, compound.molMass, compound.mp, compound.bp))
            self.conn.commit()
            print(f"✅ Added: {compound.name}")
        except sqlite3.IntegrityError:
            print(f"⚠️ Duplicate not added: '{compound.name}' already exists.")

    def list_from_db(self):
        self.cursor.execute("SELECT name, formula, molar_mass, mp, bp FROM compounds")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"Name: {row[0]}, Formula: {row[1]}, Molar Mass: {row[2]} g/mol, Melting Point: {row[3]} °C, Boiling Point: {row[4]} °C")

    def close(self):
        self.conn.close()

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