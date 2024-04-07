'''
Continue this example and implement the following:

User Registration: Implement a user registration functionality where users can create accounts with a username and password. Store the user data in a database and provide login and logout functionalities.

Password Encryption: Enhance the user authentication system by encrypting user passwords before storing them in the database. Use a secure hashing algorithm like bcrypt for password hashing.

Profile Page: Create a profile page where users can view and edit their profile information, such as username, email, and profile picture.

File Upload: Implement a file upload functionality where users can upload images or documents. Validate and store the uploaded files securely on the server.

Email Verification: Implement an email verification process for user registration. Send a verification email to the user's email address with a unique token or link for verification.

Password Reset: Implement a password reset functionality where users can request a password reset link via email if they forget their password.

Admin Dashboard: Create an admin dashboard where administrators can manage user accounts, view user activity logs, and perform other administrative tasks.

RESTful API: Create a RESTful API with Flask for performing CRUD operations (Create, Read, Update, Delete) on resources such as users, posts, comments, etc.

Authentication with OAuth: Implement authentication using OAuth with popular social media platforms like Google, Facebook, or GitHub. Allow users to sign in using their social media accounts.

Error Handling: Improve error handling in your Flask application by implementing custom error pages for different HTTP status codes (e.g., 404 Not Found, 500 Internal Server Error).
'''

from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'my_secret_key'

users = {
    'user1': 'password1',
    'admin': 'admin'
}


@app.route('/')
def index():
    if 'username' in session:
        title = 'Welcome to my flask application!'
        current_year = datetime.now().year
        return f'Logged in as {session["username"]}<br><a href="/logout">Logout</a><br>' + render_template('index.html',
                                                                                                           title=title,
                                                                                                           current_year=current_year)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form data for POST requests
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # If the username and password are correct, save the username
            # in the session and redirect to the home page
            session['username'] = username
            return redirect(url_for('index'))

    # Render the login form for both cases get and post requests
    title = 'Please login'
    # Process the login form data here
    return render_template('login.html', title=title)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/python_exercises_examples')
def python_exercises_examples():
    if ('username' not in session):
        return redirect(url_for('login'))
    else:
        title = "Python exercises examples"
        examples = [{
            'title': 'Example 1',
            'description': 'Write a program to check if a number is even or odd.',
            'code': 'num = 7\nif num % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")'
        },
            {
                'title': 'Example 2',
                'description': 'Write a program to find the factorial of a number.',
                'code': 'num = 5\nfactorial = 1\nfor i in range(1, num + 1):\n    factorial *= i\nprint("Factorial:", factorial)'
            },
            {
                'title': 'Example 3',
                'description': 'Write a program to reverse a string.',
                'code': 'string = "hello"\nreversed_string = string[::-1]\nprint("Reversed string:", reversed_string)'
            }]
        return render_template('python_exercises_examples.html', title=title, examples=examples)
