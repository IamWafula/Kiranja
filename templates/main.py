from firebase import firebase

firebase = firebase.FirebaseApplication('timetable-2c557.firebaseapp.com', None)
result = firebase.get('/users/2', None, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result
{'2': 'Jane Doe'}