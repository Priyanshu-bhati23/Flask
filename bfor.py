from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is " + str(score)

if __name__ == '__main__':
    app.run(debug=True,port=5500)
