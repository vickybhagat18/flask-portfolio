from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        message = request.form.get('message')

        if not name or not email or not message or not mobile:
            return render_template('contact.html', success=False)

        
        print("\n------ New Contact Form Submission ------")
        print(f"Name    : {name}")
        print(f"Email   : {email}")
        print(f"Mobile  : {mobile}")
        print(f"Message : {message}")
        print("----------------------------------------\n")

        return render_template('contact.html', success=True)

    return render_template('contact.html', success=False)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  
    app.run(host='0.0.0.0', port=port)

