from flask import Flask,request,render_template#library used retrieve any post information we want

app=Flask(__name__)

#Route
@app.route('/')
def welcome():
    return render_template("index.html")
@app.route('//aboutus')
def aboutus():
    return "We are ineuron"

@app.route('/demo',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=0
        
        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=="division":
            result=num1/num2
        else:
            result=num1-num2
        return "The operation is {} and the result is {} ".format(operation,result)


@app.route('/operation',methods=['POST'])
def operation():
    if(request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0
        
        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=="division":
            result=num1/num2
        else:
            result=num1-num2
        return render_template("result.html",result=result)

#it will tell the entry point of the function
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)#0.0.0.0local address=>127.0.0.0it will map 
"""git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/vamsiva/flask.git
git push -u origin main"""