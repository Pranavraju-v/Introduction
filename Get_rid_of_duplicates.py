student_data={
    'id_1': {'name': 'Sara', 'class':'V','subject_integretion':'math english science'},
    'id_2':{'name': 'Surya', 'class':'V','subject_integretion':'math,english,science'},
    'id_3':{'name':'Sara', 'class':'V', 'subject_integretion':'math,english,science'}
}
result={}
seen_keys=[]
for student_id, details in student_data.items():
    unique_key=(details['name'], ['class'], ['subject_integretions'])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for k,v in result.items():
    print(k, ":", v)