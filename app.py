from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Contact Form Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In a real app, you would handle this data (e.g., store it in a database)
        return f"Thank you for your message, {name}! We will get back to you at {email}."

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)