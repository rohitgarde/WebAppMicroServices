from flask import Flask

app = Flask(__name__)

@app.route('/getreq', methods=['GET'])
def getreq():
  return ' Hello User, This is your Get Request.'

@app.route('/get', methods=['GET'])
def get():
    return ' Hello User, This is your Second Get Request.'

@app.route('/post', methods=['POST'])
def post():
    
    return 'Hello User. Your Post request has been received.' 
  
if __name__ == '__main__':
        #app.run(debug=True, port=8083) #run app on port 8080 in debug mode
        app.run(threaded=True,host='0.0.0.0',port=8085)
