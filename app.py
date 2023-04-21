# psutil is used to get the memory and CPU of ther sever
# to run app: python3 app.py in terminal
# open chrome type http://localhost:5000
import psutil
from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80:
        Message = "High CPU Utilization. Please scale up"
    elif mem_percent > 80:
        Message = "High Memory Utilization. Please scale up"
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')