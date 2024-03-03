from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)

# New route for email validation form
@app.route('/validate-email-form')
def email_validation_form():
    return render_template('email_validation.html')

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form['email']
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return 'Valid email'
    else:
        return 'Invalid email'
if __name__ == '__main__':
    app.run(debug=True)
