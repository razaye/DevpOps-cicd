from flask import Flask

app= Flask(__name__)

@app.route('/')

def home():
    return "CI/CD avec Github Action !"

@app.route('/addition/<int:a>/<int:b>')

def addition(a, b):
   return str(a +b)

if __name__=='__main__':
   app.run(host=='0.0.0.0, port=5000') 
