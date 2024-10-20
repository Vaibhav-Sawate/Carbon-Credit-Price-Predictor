from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('carbon_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        industry = request.form['industry']
        if industry == 'Agriculture' or industry == 'Mechanical':
            val1 = float(request.form['CO2_Emissions'])
            val2 = float(request.form['GDP'])
            val3 = float(request.form['Oil_Price'])
            val4 = float(request.form['Coal_Price'])
            val5 = float(request.form['Gas_Price'])
            val6 = float(request.form['Renewable_Energy_Index'])
            val7 = float(request.form['Temperature'])
            val8 = float(request.form['Trading_Volume'])
            val9 = float(request.form['Regulatory_Changes'])
            val10 = float(request.form['Technological_Advances'])
            val11 = float(request.form['Global_Events'])
            arr = np.array([val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11])
            
            arr = arr.astype(np.float64)
            pred = model.predict([arr])
            return render_template('index.html', data=int(pred))
    except ValueError:
        return render_template('index.html', data="Please enter valid numeric values for all fields.")

if __name__ == '__main__':
    app.run(debug=True)
