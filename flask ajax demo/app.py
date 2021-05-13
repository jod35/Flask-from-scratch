from flask import Flask,render_template,request,jsonify

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/add',methods=['POST'])
def add():
    data=request.get_json()

    x=data.get('x')
    y=data.get('y')

    print(x)
    print(y)


    result=x+y
    
    response=jsonify({"result":result})
    return response

    

if __name__ == '__main__':
    app.run(debug=True)