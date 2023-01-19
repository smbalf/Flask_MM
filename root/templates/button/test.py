test = {'_fresh': True, 
'_id': '8c89f89ad1cb90e48832fc91f2566de4a44be2c6e06bdf660aa403c5c8a85561d173904dddf46e109a7444b1e96f8884a7ec0893385661512c3ffdaa0adc807e', 
'_user_id': '63c7dc7617cb6978b0769f1b', 'csrf_token': 
'892066c26a78b53437f05f44282ced9410f3e3f1'}

x = '63c7dc7617cb6978b0769f1b'
if x in test['_user_id']:
    print("yes")
elif x not in test['_user_id']:
    print("no")
else:
    print("idk")