from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)  

@app.route('/play/<int:num>')
def index(num):
    return render_template("index.html", num=num)

@app.route('/play/<int:num>/<string:color>')
def part_three(num,color):
    return render_template("index.html", id="box", color=color, num=num)


if __name__=="__main__":   
    app.run(debug=True)    

