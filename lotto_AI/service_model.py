#1. 모델 불러오는 함수
#2. 데이터 예측 출력 함수
#3. 데이터 전처리 함수
#4. 모델 업그레이드 함수
#5. 모델 정확률 산정함수
#6. 오차율은 테스트 파일로 테스트후 다시 훈련하여 저장후 출력
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import pickle
# configure
OS_DELIM = "\\"
ROOT_PATH = r"D:{}lotto_AI".format(OS_DELIM)
DATA_LABELS = ["year_date", "num_1", "num_2", \
               "num_3", "num_4", "num_5", "num_6", "num_7"]
def callModel(mname):  # 모델 불러오는 함수
    print()
    tmodel = tf.keras.models.load_model( \
        f"{ROOT_PATH}{OS_DELIM}lotto_model{OS_DELIM}{mname}.keras")
    return tmodel
def preproc(data_set, time_step):  # 데이터 전처리 함수
    df = pd.read_csv(f"{ROOT_PATH}{OS_DELIM}last_data{OS_DELIM}{data_set}", \
                     names=DATA_LABELS)
    df["year_date"] = pd.to_datetime(df["year_date"])
    print(df["year_date"][0])
    df["millis"] = df["year_date"].astype("int64") // 10 ** 9
    print(df["millis"][0])
    raw_data = np.array( \
        df.loc[:, ["num_1", "num_2", "num_3", "num_4", \
                   "num_5", "num_6", "num_7", "millis"]])
    print(raw_data.shape)
    print("원본숫자:", raw_data[0])
    raw_data = np.array( \
        [np.concatenate([raw_data[i][:7] / (raw_data[i][7] / (10 ** 8)), \
                         [raw_data[i][7]]]) \
         for i in range(len(raw_data))])
    print("복원숫자:", recoverData(raw_data[0][:7], raw_data[0][7]))
    raw_data = raw_data[::-1]
    x_data = [];
    for i in range(len(raw_data) - time_step):
        x_data.append(raw_data[i:time_step + i])
    return np.array(x_data)
def recoverData(data_arr, millis_sec):  # (unit numpy_arr,milli second)
    millis_sec /= (10 ** 8)
    return data_arr * millis_sec
def printpred(tmodel, x_data, millis_sec):  # 예측 출력함수
    print("훈련데이터의 마지막 일자:", datetime.fromtimestamp(x_data[-1][-1][7]))
    print("예측일 번호:", datetime.fromtimestamp(millis_sec))
    x_data = np.array([x_data[-1]])
    y_pred = tmodel.predict(x_data[:, :, :7])
    print(y_pred)
    return np.round(recoverData(y_pred, millis_sec)),\
        datetime.fromtimestamp(x_data[-1][-1][7]),\
        datetime.fromtimestamp(millis_sec)
def upgradeModel():  # 모델업그레이드
    pass
def current_errRate(pathname):  # 오차율 출력 함수
    err_rat=None
    with open(f"{ROOT_PATH}{OS_DELIM}lotto_model{OS_DELIM}{pathname}","rb") as fp:
        err_rat=pickle.load(fp)
    return err_rat
def pred_lottonumber(model_name, model_file, datestr, time_step):
    tmodel = callModel(model_name)
    x_pred = preproc(model_file, time_step)
    mname,_,tname=model_name.split("_")
    err_rat=current_errRate(mname+"_err_"+tname)
    tmp = err_rat[0].split(",")
    tmp.append(str(round(float(err_rat[-1]), 2)) + "%")
    # u time으로 +9시
    res,lastfit_date,pred_date = printpred(tmodel, x_pred, datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S").timestamp())

    res = res[0].astype("int32").tolist()
    return res,tmp,lastfit_date,pred_date
if __name__=="__main__":
    pred,err_rat,lastfit_date,pred_date =pred_lottonumber("LSTM_model_48","current_lotto_08.09.csv","2025-08-16 09:00:00",48)
                                                         #사용자에 수신값 : 모델의 종류, 예측타입스템,예측 일자
    print(pred,err_rat,lastfit_date,pred_date)

