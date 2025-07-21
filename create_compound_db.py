import sqlite3

conn = sqlite3.connect("compounds.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS compounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    formula TEXT,
    molar_mass REAL,
    mp REAL,
    bp REAL
    )
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_name ON compounds(name)")

print("✅ Database and table created.")
conn.commit()
conn.close()