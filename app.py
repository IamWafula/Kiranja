from flask import Flask, render_template , request

import africastalking

username = "Kiranja"  
api_key = "aee055d33c12a0ab4608a1050e12624e7ccb8e8f57e3131641851bf68bb9be27"      
africastalking.initialize(username, api_key)


sms = africastalking.SMS

sms1 = "Good evening, you have a lesson in 4D in 10 minutes."
sms2 = "Masalkheri, una kipindi katika darasa la 4D kwa dakika 10."



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route('/teachers')
def Setttings():
    return render_template('teachers.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if (request.method == 'POST'):
        num1 = str(int(request.form['Judge1']))
        num2 = str(int(request.form['Judge2']))
        
        num1 = "+254"+num1
        num2 = "+254"+num2
        try:
            sms.send(sms1, [num1]) 
            sms.send(sms2, [num2]) 
        
            return render_template('new.html')
        except:
            return render_template('new2.html')
     
@app.route('/login')
def login():
    return render_template ('login.html')

@app.route('/signup')
def signup():
    return render_template ('signup.html')

if (__name__) == ('__main__'):
    app.debug = True
    app.run()
    