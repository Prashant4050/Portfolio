from flask import Flask, render_template, request, send_file
from flask_mail import Mail, Message

app = Flask(__name__)

# ✅ Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'malaviyaprashant4050@gmail.com'      
app.config['MAIL_PASSWORD'] = 'iree jarw zsbz rboq'              
app.config['MAIL_DEFAULT_SENDER'] = 'malaviyaprashant4050@gmail.com'

mail = Mail(app)

projects = [
    {
        'title': 'Face Recognition Attendance System',
        'description': 'A Python-React based app that marks attendance using face recognition.',
        'tech': 'Python, React, MongoDB, Node.js',
        'github': 'https://github.com/yourusername/face-attendance'
    },
    {
        'title': 'Book Swap App',
        'description': 'React-based web app for Hindu literature book exchange.',
        'tech': 'React, Firebase',
        'github': 'https://github.com/yourusername/book-swap'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/resume')
def resume():
    return send_file("resume.pdf", as_attachment=True)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # ✅ Compose and send the email
        msg = Message(
            subject=f"New message from {name}",
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=['yourgmail@gmail.com'],  # where you receive the message
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)

        return render_template('contact.html', success=True)

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
