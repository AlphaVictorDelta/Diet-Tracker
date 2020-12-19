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
def closeDatabaseConnection():
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


# BASIC URL ROUTES 
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/view_day')
def view_day():
	return render_template('day.html')

@app.route('/add_food')
def add_food():
	return render_template('add_food.html')




# MAIN FUNCTION
if __name__ == '__main__':
	app.run()
