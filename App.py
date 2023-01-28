from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/Hai')
def Hai():
    return 'This is My first Project on Flask'



@FAI.route('/Wish/<name>')
def Wish(name):
    return f'Good Evening {name} Sir'

@FAI.route('/First')
def First():
    return render_template('First.html')

if __name__=='__main__':
    FAI.run(debug=True)
