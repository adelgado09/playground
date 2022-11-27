from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def play():
    return render_template("index.html", num = 3, color = "blue")
# defaults as 3 blue blocks

@app.route('/play/<int:num>')
def number(num):
    return render_template("index.html", num = num, color = "blue" )
# changes the number of blocks but still blue blocks

@app.route('/play/<int:num>/<string:color>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def color(num, color):
    return render_template("index.html", num = num, color = color)
# changes the number and color of blocks

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
