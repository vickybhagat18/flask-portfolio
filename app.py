from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# ✅ HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html')

# ✅ PROJECTS PAGE
@app.route('/projects')
def projects():
    return render_template('projects.html')

# ✅ CONTACT FORM PAGE
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        message = request.form['message']

        print("📩 Message Received:")
        print("👤 Name:", name)
        print("📧 Email:", email)
        print("📱 Mobile:", mobile)
        print("💬 Message:", message)

        return render_template('contact.html', success=True)

    return render_template('contact.html', success=False)

# ✅ RESUME DOWNLOAD
@app.route('/resume')
def resume():
    return send_from_directory('resume', 'Vicky_Bhagat_Resume.pdf')


# ✅ MAIN FUNCTION
if __name__ == '__main__':
    app.run(debug=True)
