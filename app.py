from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def contact_form():
    return render_template('/contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    message = request.form.get('message')
    subject = request.form.get('subject')
    preferred_contact = request.form.get('preferred_contact')
    agreement = request.form.get('agreement')

    return render_template(
        'Confirmation.html',
        name=name,
        email=email,
        phone_number=phone_number,
        message=message,
        subject=subject,
        preferred_contact=preferred_contact,
        agreement=agreement,
     )


if __name__ == '__name__':
    app.run(debug=True)