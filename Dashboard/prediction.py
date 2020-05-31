import pickle
from pandas import DataFrame, get_dummies

model = pickle.load(open('xgb_1.sav', 'rb'))
one_hot_columns = pickle.load(open('xgb_1_onehot.sav', 'rb'))

def prediction(data):
    df = DataFrame(data, index=[0])
    df = get_dummies(df, drop_first=True)
    df = df.reindex(columns=one_hot_columns, fill_value=0)
    hasil = list(map(lambda x: 1 if x == True else 0, (model.predict_proba(df)[:,1] > 0.37)))
    hasil_proba = model.predict_proba(df)[:,1]
    return hasil, hasil_proba