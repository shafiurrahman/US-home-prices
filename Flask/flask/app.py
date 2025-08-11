from flask import Flask


app=Flask(__name__)
# it creates an instance of the flask class,which will be your WSGI  application
#web server gateway interface


@app.route("/")     # '/'  basically means home page 
def welcome():
    return '***Welcome to flask , the time spent here would be fruitful -----*****$$$$'

@app.route("/index")     # '/'  basically means home page 
def indexwelcome():
    return '***Welcome to flask ,index*$$$$'


if __name__==  "__main__":    # this is the entry point of all .pyfiles
    app.run(debug=True)   #debug=true will restart the server i.e changes made here will reflect on webpage

