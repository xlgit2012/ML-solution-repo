import pickle
id2record = pickle.load(open('id2record.pkl', mode='rb'))
print(id2record)

alarm_fault_dict= pickle.load(open('alarm_fault_dict.pkl', mode='rb'))
print(alarm_fault_dict)