from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-key')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        date_of_birth = request.form.get('date_of_birth')
        return f"Member {full_name} registered successfully! (Database saving comes in ticket 58)"
    return render_template('add_member.html')

if __name__ == '__main__':
    app.run(debug=True)