from flask import Flask,render_template,url_for,request,json
import datetime
import tensorflow as tf
from service_model import pred_lottonumber
app = Flask(__name__)
@app.route("/")
def index_view():
    return render_template(f"index.html")
@app.route("/lotto365/<tdate>/<model>")
def repjson(tdate,model):
    #"2025-08-16 09:00:00"
    tdate=tdate.strip()
    tdate += " 09:00:00"
    timstep = int(model.split("_")[2])
    pred,err_rat,lastfit_date,pred_date =pred_lottonumber(model,\
                         "current_lotto_08.09.csv",tdate,timstep)
    #tardata to json
    testdata = {"pred":pred,"err_rat":err_rat,"lastfit_date":lastfit_date,\
                "pred_date":pred_date}
    jtardata = json.jsonify(testdata)#dict -> json 문자화
    return jtardata

app.run("127.0.0.1",36500,True)