from flask import Flask, render_template, redirect, session 

app = Flask(__name__)
# Session secret key code below
app.secret_key = "Watagatapitusberry"


# Page viewed at first vist method code below
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

# "CLICK" link adds two to every visit method code below
@app.route('/count2')
def count():
    if "counter" not in session:
        session['counter'] = session['counter']
    else:
        session['counter'] += 1
    return redirect('/')

# Reset my session code below
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=True)