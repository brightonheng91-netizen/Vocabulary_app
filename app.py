from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return "Welcome to your Vocabulary App!"

# Login page (GET) + process login (POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("Login:", username, password)  # temporary output
        return redirect(url_for('home'))
    return render_template('login.html')


# Register page (GET) + process registration (POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print("Register:", username, password)  # temporary output
        return redirect(url_for('login'))
    return render_template('register.html')


# ---------- Vocabulary Feature ----------

# temporary list to store vocabulary
vocabulary_list = []

@app.route('/add_vocab', methods=['GET', 'POST'])
def add_vocab():
    if request.method == 'POST':
        word = request.form['word']
        definition = request.form['definition']
        translation = request.form['translation']
        vocabulary_list.append({
            'word': word,
            'definition': definition,
            'translation': translation
        })
        print(vocabulary_list)  # just to confirm it's saved
        return redirect(url_for('add_vocab'))

    return render_template('add_vocab.html')

@app.route('/vocab_list')
def vocab_list():
    return render_template('vocab_list.html', vocabulary=vocabulary_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

