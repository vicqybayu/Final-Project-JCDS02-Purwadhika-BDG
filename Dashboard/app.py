from flask import Flask, render_template, request
from data import naics, states, data_clean
from prediction import prediction
from plots import default_per_state, default_per_ind, default_per_year

## translate Flask to python object
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        data['Term'] = int(data['Term'])
        data['NoEmp'] = int(data['NoEmp'])
        data['DisbursementGross'] = int(data['DisbursementGross'])
        data['SBA_Appv'] = int(data['SBA_Appv'])
        data['Ratio'] = float(data['SBA_Appv']/data['DisbursementGross'])
        hasil = prediction(data)
        if hasil[0] == [0]:
            hasil_alt = 'Paid in Full'
        else:
            hasil_alt = 'Default'
        return render_template('result.html', hasil_prediction=[hasil_alt, str(round(hasil[1][0]*100, 2))+'%'])
    return render_template('prediction.html', data_states=sorted(states), data_naics=naics)

# @app.route('/about')
# def about():
#     return render_template('about.html')

@app.route('/default_per_state')
def plots_graph():
    data = default_per_state()
    return render_template('visualization.html', data=data)

@app.route('/default_per_ind')
def plots_graph2():
    data = default_per_ind()
    return render_template('visualization2.html', data=data)

@app.route('/default_per_year')
def plots_graph3():
    data = default_per_year()
    return render_template('visualization3.html', data=data)

@app.route('/data')
def table_data():
    data = data_clean()
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=1111)