import sqlite3

conn1 = sqlite3.connect('food_log.sqlite')
cur1 = conn1.cursor()

cur1.executescript('''
CREATE TABLE IF NOT EXISTS "log_date" (
	"ID"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Entry_Date" DATE NOT NUll
);

CREATE TABLE IF NOT EXISTS "Food" (
	"ID"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Name"  TEXT NOT NULL,
	"Protien"  INTEGER NOT NULL,
	"Carbohydrates"  INTEGER NOT NULL,
	"Fat"  INTEGER NOT NULL,
	"Calories"  INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "Food_Date" (
	"Food_ID"    INTEGER NOT NULL,
	"Log_Date_ID"  TEXT NOT NULL,
	primary key(Food_ID, Log_Date_ID)
);


''')