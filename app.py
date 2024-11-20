
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/result/<int:score>')
def result(score):
    if score > 50:
        return redirect(url_for('success', score=score))
    else:
        return redirect(url_for('fail', score=score))

@app.route('/fail/<int:score>')
def fail(score):
    return f'The student has {score} marks and he has failed.'

@app.route('/success/<int:score>')
def success(score):
    return f'The student has {score} marks and he has passed.'

if __name__ == '__main__':
    app.run(debug=True)
