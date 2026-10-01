from flask import Flask, render_template, request
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-key')


def calculate_age(dob_string):
    """Calculate age in years from a YYYY-MM-DD date string."""
    dob = date.fromisoformat(dob_string)
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


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

        guardian_name = request.form.get('guardian_name')
        guardian_phone = request.form.get('guardian_phone')
        guardian_relationship = request.form.get('guardian_relationship')

        age = calculate_age(date_of_birth)
        is_minor = age < 18

        if is_minor:
            if not guardian_name or not guardian_phone or not guardian_relationship:
                return "Error: Guardian details (name, phone, relationship) are required for members under 18.", 400

        guardian_info = (
            f" Guardian: {guardian_name} ({guardian_relationship}), {guardian_phone}."
            if is_minor else ""
        )
        return f"Member {full_name} (age {age}) registered successfully!{guardian_info} (Database saving comes in ticket 58)"

    return render_template('add_member.html')


if __name__ == '__main__':
    app.run(debug=True)