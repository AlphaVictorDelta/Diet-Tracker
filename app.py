from flask import Flask, jsonify, request, redirect, url_for, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True

# DATABASE HELPERS 
def connectToDatabase():
	conn1 = sqlite3.connect('food_log.sqlite')
	conn1.row_factory = sqlite3.Row
	return conn1

def getDatabase():
	if not hasattr(g, 'sqlite3'):
		g.sqlite_db = connectToDatabase()
	return g.sqlite_db

@app.teardown_appcontext
def closeDatabaseConnection(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


# BASIC URL ROUTES 
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/view_day')
def view_day():
	return render_template('day.html')

@app.route('/add_food', methods=['GET', 'POST'])
def add_food():
	database = getDatabase()
	if request.method == 'POST':
		name = request.form['food-name']
		protein = int(request.form['Protein'])
		carbohydrates = int(request.form['Carbohydrates'])
		fat = int(request.form['Fat'])
		calories = protein*4 + carbohydrates*4 + fat*9

		database.execute('INSERT INTO Food (Name, Protein, Carbohydrates, Fat, Calories) VALUES (?, ?, ?, ?, ?)',\
			[name, protein, carbohydrates, fat, calories])
		database.commit()


	cur = database.execute('SELECT Name, Protein, Carbohydrates, Fat, Calories FROM Food')
	results = cur.fetchall()

	return render_template('add_food.html', results=results)





# MAIN FUNCTION
if __name__ == '__main__':
	app.run()
