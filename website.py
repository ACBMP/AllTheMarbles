import flask
import pandas as pd 
import numpy as np 

app = flask.Flask(__name__)

data_types = {'Player': str, 'W/L': str, 'Game1': np.int32, 'Game2':np.int32, 
			'Game3': np.int32, 'Game4': np.int32, 'Game5': np.int32, 'Game6': np.int32,
			'Game7': np.int32, 'Game8': np.int32}

stats = pd.read_csv('stats.csv', sep='	')
stats.fillna(0, inplace=True)
stats = stats.astype(data_types)

average = []
for i in range(len(stats)):
	row_i = stats.values[i]
	summe = 0 
	counter = 0 
	for n in range(2,9):
		summe = summe + row_i[n]
		if row_i[n] != 0: 
			counter += 1 
	try:
		avg = summe / counter 
	except ZeroDivisionError: 
		avg = 0 
	average.append(avg)

stats['Average'] = average

@app.route('/stats')
def statspage():
	return flask.render_template('stats.html', stats = stats)

if __name__ == '__main__':
		app.run(debug=True)

