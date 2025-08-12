#### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine
''' multiple ways of reading variable from backend to html file we demonstrated one type
{{}}   these are expression to print outpput in html
{%.....%}   this is used for conditional statements,forloop,whileloop
{#....#} this is used for single line comment'''

from flask import Flask,render_template,request,redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name} !'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

#variable rule : ie. in our case we can give only int for score, if float is give there i/p has to be like 65.0
@app.route('/success/<int:score>')    # works with string  if return is 'your score'+score becasue of concat
def success(score):
    res=''
    if score >=50 and score <=100:
        res='********passed'
    elif score >100:
        res='?? enter correct number'
    else:
        res='failed ^^^^^^'
    return render_template('result.html',result=res)  # this {{result}} is jinja2 template accessed in result.html
    


if __name__==  "__main__":    # this is the entry point of all .pyfiles
    app.run(debug=True)   #debug=true will restart the server i.e changes made here will reflect on webpage

