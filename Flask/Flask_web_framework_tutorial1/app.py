from flask import Flask

### WSGI application is created 
app = Flask(__name__)

### decorator - with first parameter or rule a url in string format
@app.route('/')
def welcome():
    return 'welcome to my GitHUb. Please Please fork, share and like it. '

@app.route('/members')
def members():
    return 'welcome to my GitHUb guys. '


### 4 options in the run such as a host, port, debug
if __name__=='__main__':
    app.run(debug = True)