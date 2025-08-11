from flask import Flask,render_template


app=Flask(__name__)
# it creates an instance of the flask class,which will be your WSGI  application
#web server gateway interface


@app.route("/")     # '/'  basically means home page 
def welcome():
    return "<html>" \
    "<h1>" \
    "welcome to flask and later deployment on other places" \
    "<h1>" \
    "<html>"

@app.route("/index")     # '/'  basically means home page 
def indexwelcome():
    return render_template('index.html') # it will redirect and go check for a folder called templates 'even s is imp in the name

@app.route("/about")
def about():
    return render_template('about.html')

if __name__==  "__main__":    # this is the entry point of all .pyfiles
    app.run(debug=True)   #debug=true will restart the server i.e changes made here will reflect on webpage

