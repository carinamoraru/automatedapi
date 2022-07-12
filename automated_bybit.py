from flask import Flask, render_template, request
app =  Flask(__name__)
import my_bybit

api_key = "cSBL3DAXa2S2Hhv5MO"
secret_key = "QaTm9Y9DAz5aCGe3T4chjCBvV9zpN73GMbyv"

@app.route('/', methods=['GET', 'POST'])
# @app.route('/<int:uid>', methods=['GET','POST'])
def index():
    isTest = True
    if request.method == 'POST' or isTest:
        isTest = True
        # name = request.form['name']
        # context = request.form['context']
    else:
        return render_template('fail.html')

    myBybit = my_bybit.Mybybit(api_key, secret_key)
    json_result = myBybit.get_json("ETHUSD", "D", "1653408000")
    return render_template('home.html', json_result=json_result['result'], len=len(json_result['result']))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    myBybit = my_bybit.Mybybit(api_key, secret_key)
    json_result = myBybit.get_json("ETHUSD", "D", "1653408000")
    return render_template('index.html', alpaca_orders=json_result)


if __name__ == "__main__":
    app.run()