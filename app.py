
from flask import Flask
app1 = Flask(__name__)
@app1.route('/')
def show_me_the_money():
  return("+$1000000")
print(__name__)  
if __name__=='__main__':
  app1.run(host='0.0.0.0',debug=True)

