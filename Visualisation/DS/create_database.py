import sqlite3

conn = sqlite3.connect('people_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    prenom TEXT,
    age INTEGER,
    salary REAL,
    education TEXT,
    department TEXT,
    city TEXT
)
''')

people_data = [
    ('Ben Ali', 'Ahmed', 28, 55000, 'Bachelor', 'IT', 'Tunis'),
    ('Bouaziz', 'Fatima', 32, 65000, 'Master', 'Marketing', 'Sfax'),
    ('Mansouri', 'Omar', 45, 80000, 'PhD', 'Engineering', 'Sousse'),
    ('Hammami', 'Amira', 29, 48000, 'Bachelor', 'Sales', 'Kairouan'),
    ('Chouchane', 'Samir', 41, 75000, 'Master', 'Finance', 'Gabes'),
    ('Amri', 'Lina', 36, 71000, 'Bachelor', 'HR', 'Bizerte'),
    ('Jebali', 'Khaled', 38, 63000, 'PhD', 'IT', 'Monastir'),
    ('Trabelsi', 'Rania', 26, 52000, 'Bachelor', 'Marketing', 'Medenine'),
    ('Ouertani', 'Sami', 33, 67000, 'Master', 'Engineering', 'Tataouine'),
    ('Zidi', 'Nada', 24, 48000, 'Bachelor', 'Sales', 'Gafsa'),
    ('Ayari', 'Yassine', 47, 83000, 'PhD', 'Finance', 'Nabeul'),
    ('Khalifa', 'Salma', 30, 58000, 'Bachelor', 'IT', 'Ben Arous'),
    ('Jaziri', 'Mohamed', 34, 66000, 'Master', 'Marketing', 'Ariana'),
    ('Mahjoub', 'Hanaa', 39, 78000, 'PhD', 'Engineering', 'Sfax'),
    ('Gharbi', 'Anis', 25, 49000, 'Bachelor', 'Sales', 'Kebili'),
    ('Maaloul', 'Basma', 42, 72000, 'Master', 'Finance', 'Siliana'),
    ('Salah', 'Firas', 37, 74000, 'Bachelor', 'HR', 'Kairouan'),
    ('Chebbi', 'Latifa', 40, 75000, 'Master', 'Engineering', 'Zarzis'),
    ('Jendoubi', 'Nizar', 27, 56000, 'Bachelor', 'IT', 'El Kef'),
    ('Kacem', 'Rihab', 29, 50000, 'Bachelor', 'Marketing', 'Jendouba'),
    ('Boukhris', 'Ismail', 44, 79000, 'PhD', 'Finance', 'Tunis'),
    ('Slim', 'Rim', 31, 59000, 'Bachelor', 'Sales', 'Sidi Bouzid'),
    ('Cherif', 'Oussama', 46, 82000, 'PhD', 'Engineering', 'Manouba'),
    ('Farhat', 'Mourad', 30, 61000, 'Master', 'Finance', 'Tozeur'),
    ('Karboul', 'Nour', 28, 53000, 'Bachelor', 'IT', 'Mahdia'),
    ('Sahli', 'Aymen', 35, 68000, 'Master', 'Marketing', 'Djerba'),
    ('Raies', 'Sara', 40, 76000, 'PhD', 'Engineering', 'Beja'),
    ('Azizi', 'Rached', 43, 77000, 'PhD', 'Finance', 'Gafsa'),
    ('Grira', 'Lina', 26, 51000, 'Bachelor', 'HR', 'Nabeul'),
    ('Douiri', 'Mohamed', 31, 60000, 'Bachelor', 'Sales', 'Monastir'),
    ('Kooli', 'Amine', 33, 65000, 'Master', 'Finance', 'Medenine'),
    ('Hadhri', 'Asma', 29, 57000, 'Bachelor', 'IT', 'Ariana'),
    ('Bouhlel', 'Hamdi', 36, 69000, 'Master', 'Marketing', 'Zaghouan'),
    ('Sassi', 'Khaled', 38, 71000, 'Master', 'Engineering', 'Siliana'),
    ('Ben Salah', 'Leila', 27, 54000, 'Bachelor', 'HR', 'Sfax'),
    ('Belaid', 'Wassim', 41, 74000, 'PhD', 'Finance', 'Sousse'),
    ('Dabbabi', 'Safia', 32, 62000, 'Bachelor', 'Sales', 'Ben Arous'),
    ('Saidi', 'Yosra', 44, 78000, 'PhD', 'Marketing', 'Jendouba'),
    ('Aouini', 'Hamza', 35, 68000, 'Master', 'Engineering', 'Mahdia'),
    ('Lahmar', 'Faten', 29, 55000, 'Bachelor', 'IT', 'Tunis'),
    ('Akrout', 'Saber', 33, 66000, 'Master', 'Finance', 'Marsa'),
    ('Nasri', 'Ibtissem', 46, 81000, 'PhD', 'Engineering', 'Kasserine'),
    ('Brahmi', 'Nour', 28, 56000, 'Bachelor', 'Sales', 'Bizerte'),
    ('Mejri', 'Rami', 39, 72000, 'Master', 'Marketing', 'Sidi Bouzid'),
    ('Dhrif', 'Omar', 42, 79000, 'PhD', 'IT', 'Gabes'),
    ('Louati', 'Amani', 31, 59000, 'Bachelor', 'Sales', 'Monastir'),
    ('Zoghlami', 'Mahmoud', 45, 80000, 'PhD', 'Engineering', 'Kebili'),
    ('Hamza', 'Rania', 37, 65000, 'Master', 'Finance', 'Manouba'),
    ('Maamri', 'Nizar', 26, 53000, 'Bachelor', 'Marketing', 'Tunis'),
    ('Khaldi', 'Yasmina', 34, 61000, 'Master', 'HR', 'Tozeur')
]


cursor.executemany('''
INSERT INTO people (nom, prenom, age, salary, education, department, city)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', people_data)

print("Table created and data inserted successfully!")
conn.commit()
conn.close()
