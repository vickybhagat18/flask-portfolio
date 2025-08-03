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
        message = request.form.get('message')

        if not name or not email or not message:
            flash("Please fill in all the fields.")
            return redirect(url_for('contact'))

        print(f"📩 Message from {name} ({email}): {message}")
        flash("Message sent successfully!")
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Compatible with Render
    app.run(host='0.0.0.0', port=port)

