from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 
  

@app.route('/login/<username>,<password>', methods = ['GET','POST'])

def login(username,password):
    if username == "mohsin" and password == "admin123" :
      return jsonify({'prompt' : 'Access Granted'})
    elif username == "tabrez" and password == "admin456":
        return jsonify({'prompt': "Access Granted"})
    elif username == "yasir" and password == "admin789":
        return jsonify({'prompt': "Access Granted"})
    elif username == "ahsan" and password == "admin0":
        return jsonify({'prompt': "Access Granted"})
    else:
        return jsonify({'prompt': "User not found"})


# main driver function
if __name__ == '__main__':
    app.run(debug = True , port=5001)

