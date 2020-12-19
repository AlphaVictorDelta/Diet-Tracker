from flask import Flask, jsonify, request, redirect, url_for, session, render_template, g

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/view_day')
def view_day():
	return render_template('day.html')

@app.route('/add_food')
def add_food():
	return render_template('add_food.html')

if __name__ == '__main__':
	app.run()
