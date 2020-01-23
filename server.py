from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    return render_template("index.html", num_times=3)

@app.route('/play/<num>')
def times(num):
    return render_template("index.html", num_times=int(num))

@app.route('/play/<num>/<color>')
def num_color(num, color):
    return render_template('index.html', num_times=int(num), color=color)

if __name__=="__main__":
    app.run(debug=True)