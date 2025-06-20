
import sqlite3
from datetime import datetime

conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()

def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Branch (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS InsuranceType (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Contract (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        insurance_amount REAL NOT NULL,
        insurance_type_id INTEGER,
        tariff_rate REAL NOT NULL,
        branch_id INTEGER NOT NULL,
        FOREIGN KEY (branch_id) REFERENCES Branch(id),
        FOREIGN KEY (insurance_type_id) REFERENCES InsuranceType(id)
    )
    ''')

    conn.commit()

def insert_sample_data():

    branches = [
        ("Филиал Ростов-на-Дону", "пер. Семашко, 10"),
        ("Филиал Санкт-Петербург", "Невский пр., 25")
    ]
    cursor.executemany("INSERT INTO Branch (name, address) VALUES (?, ?)", branches)

    insurance_types = ["КАСКО", "ОСАГО", "ДМС", "Ипотечное страхование"]
    cursor.executemany("INSERT INTO InsuranceType (name) VALUES (?)", [(it,) for it in insurance_types])

    contracts = [
        ("2024-01-15", 500000.0, 1, 5.5, 1),
        ("2024-02-20", 20000.0, 2, 3.2, 2),
        ("2024-03-10", 1000000.0, 3, 7.0, 1)
    ]
    cursor.executemany(
        "INSERT INTO Contract (date, insurance_amount, insurance_type_id, tariff_rate, branch_id) VALUES (?, ?, ?, ?, ?)",
        contracts
    )

    conn.commit()

def print_all_contracts():
    cursor.execute('''
    SELECT 
        c.id, c.date, c.insurance_amount, 
        it.name AS insurance_type, c.tariff_rate, 
        b.name AS branch_name
    FROM Contract c
    JOIN Branch b ON c.branch_id = b.id
    JOIN InsuranceType it ON c.insurance_type_id = it.id
    ''')

    contracts = cursor.fetchall()
    print("\nСписок всех договоров:")
    for contract in contracts:
        print(contract)

def print_total_insurance_by_branch():
    cursor.execute('''
    SELECT 
        b.name AS branch_name, 
        SUM(c.insurance_amount) AS total_amount
    FROM Contract c
    JOIN Branch b ON c.branch_id = b.id
    GROUP BY b.name
    ''')

    totals = cursor.fetchall()
    print("\nСуммарная страховая сумма по филиалам:")
    for branch, total in totals:
        print(f"{branch}: {total} руб.")


def close_connection():
    conn.close()


if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    print_all_contracts()
    print_total_insurance_by_branch()
    close_connection()