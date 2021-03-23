from flask import Flask
from flask import render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('abc.html')

@app.route('/123')
def indexx():
    f = request.args.get('fname')
    l = request.args.get('lname')
    if( f == '123' and  l =='321'):
        return '321'
    return 'FUCK'

if __name__ == '__main__':
    app.debug = True
    app.run()