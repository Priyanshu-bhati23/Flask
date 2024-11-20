from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/results/<int:score>')
def result(score):
    if score > 40:
        return f'The student has passed with a score of {score}.'
    else:
        return f'The student has failed with a score of {score}.'

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        # Fetch form data and calculate the total score
        science = float(request.form.get('science', 0))
        math = float(request.form.get('math', 0))
        hindi = float(request.form.get('hindi', 0))
        social = float(request.form.get('social', 0))
        total_score = science + math + hindi + social

        # Redirect to the results page
        return redirect(url_for('result', score=int(total_score)))

    # Serve the HTML form from templates directory
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True,port=5500)
