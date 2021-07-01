import pandas as pd
from enum import Enum

data = pd.read_csv("../vax_state.csv")

states = ['Johor','Kedah','Kelantan','Melaka',
'Negeri Sembilan','Pahang','Perak','Perlis','Pulau Pinang',
'Sabah','Sarawak','Selangor','Terengganu','W.P. Kuala Lumpur',
'W.P. Labuan','W.P. Putrajaya']

for state in states:
 filtered = data[data.state.str.contains(state)]
 filtered.to_csv(state+".csv",index=False)


