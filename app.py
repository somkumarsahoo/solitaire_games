from flask import Flask, request, render_template

app = Flask(__name__)

# Import game logic
from game import GuessGame

game = GuessGame()

@app.route('/', methods=['GET', 'POST'])
def play_game():
    if request.method == 'POST':
        guess = request.form['guess'].upper()
        scores = game.calculate_scores(guess)
        return render_template('index.html', scores=scores)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()