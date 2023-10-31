from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    
    context = {
        'users_froyo_flavor': users_froyo_flavor,
        'users_froyo_toppings': users_froyo_toppings
    }
    
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What are your favorite things? </br>
        <label for="color">Favorite Color</label>
        <input id="color" type="text" name="color"> <br/>
        <label for="animal">Favorite Animal</label>
        <input id="animal" type="text" name="animal"> <br/>
        <label for="city">Favorite City</label>
        <input id="city" type="text" name="city"> <br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    color = request.args.get('color')
    animal = request.args.get('animal')
    city = request.args.get('city')
    
    return f"Wow, I didn't know {color} {animal} lived in {city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        What's your secret message? <br/>
        <label for="message">Message</label>
        <input id="message" type="text" name="message"> <br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form['message']
    return f"{sort_letters(message)}"

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    # get values
    operand1 = int(request.args.get('operand1'))
    operand2 = int(request.args.get('operand2'))
    operation = request.args.get('operation')
    
    # do math
    if operation == 'add':
        result = operand1 + operand2
    if operation == 'subtract':
        result = operand1 - operand2
    if operation == 'multiply':
        result = operand1 * operand2
    if operation == 'divide':
        result = operand1 / operand2
        
    context = {
        'operand1': operand1,
        'operand2': operand2,
        'operation': operation,
        'result': result
    }

    return render_template('calculator_results.html', **context)

HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES[horoscope_sign]

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1, 99)
    
    # get user's name
    users_name = request.args.get('users_name')

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number,
        'users_name': users_name.capitalize()
    }

    return render_template('horoscope_results.html', **context)

# quiz testing
@app.route('/tasks')
def task_tracker():
    """Show the user what they have to do."""
    users_tasks = [    # Could contain any number of string values
        'Call mom',
        'Walk dog',
        'Pay bills',
        'Buy groceries',
    ]
    return render_template('task_list.html', tasks=users_tasks)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
