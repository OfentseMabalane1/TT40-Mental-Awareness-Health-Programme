from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post-traumatic-stress-disorder')
def ptsd():
    return render_template('post-traumatic-stress-disorder.html')

@app.route('/obsessive-compulsive-disorder')
def ocd():
    return render_template('obsessive-compulsive-disorder.html')

@app.route('/panic-disorder')
def panic_disorder():
    return render_template('panic-disorder.html')

@app.route('/generalized-anxiety-disorder')
def gad():
    return render_template('generalized-anxiety-disorder.html')

@app.route('/specific-phobias')
def specific_phobias():
    return render_template('specific-phobias.html')

if __name__ == '__main__':
    app.run(debug=True)
