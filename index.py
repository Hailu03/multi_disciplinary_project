from flask import Flask, request, render_template
from models import *

app = Flask(__name__)

@app.route('/index')
def index():
    sensor_list = ['node2','node6']
    sensor_name = request.args.get("choose_node")
    my_sensor_data = []
    pm25 = []
    temp = []
    hum = []

    for sensor in sensor_list:
        my_sensor = MyNode(sensor)
        my_sensor.get_last_data()
        my_sensor_data.append(my_sensor.node_data)

        if sensor == sensor_name:
            my_sensor.get_online_data_chart()
            pm25 = my_sensor.node_data_pm25
            temp = my_sensor.node_data_temp
            hum = my_sensor.node_data_hum

    return render_template('index.html',data=my_sensor_data,pm25=pm25,temp=temp,hum=hum,name=sensor_name,date_time=my_sensor.date_time)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/hai')
def hai():
    return render_template('hai.html')

@app.route('/duy')
def duy():
    return render_template('duy.html')

@app.route('/hao')
def hao():
    return render_template('hao.html')

@app.route('/baohuy')
def baohuy():
    return render_template('baohuy.html')

@app.route('/duchuy')
def duchuy():
    return render_template('duchuy.html')

if __name__ == "__main__":
    app.run(debug=True,)

