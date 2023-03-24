from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<H1> Nguyễn Bình Dương <H1>"

if __name__ == '__main__':
    app.run(debug=True)
    
