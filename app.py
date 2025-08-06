from flask import Flask, render_template, request, redirect, url_for, flash
import os
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# ✅ Google Apps Script URL
GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbwv50Dww2yY2hZrUv1svnEKXnODXhoT4YOluDrfzEhDKaQwQM4HAmVp9xanhuaDF2c5/exec"

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

        if not name or not email or not mobile or not message:
            flash("⚠️ Please fill in all the fields.")
            return redirect(url_for('contact'))

        # ✅ Send data to Google Sheet
        try:
            data = {
                'name': name,
                'email': email,
                'mobile': mobile,
                'message': message
            }
            response = requests.post(GOOGLE_SHEET_URL, json=data)

            if response.status_code == 200:
                flash("✔️ Message sent successfully!")
            else:
                flash("⚠️ Failed to send message to Google Sheet.")
        except Exception as e:
            print("Error sending to Google Sheet:", e)
            flash("⚠️ Something went wrong. Please try again later.")

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
