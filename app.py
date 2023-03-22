from flask import Flask 
app = Flask(__name__)

@app.route('/')
def main():
    return "<H1> Nguyễn Bình Dương <H1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
    
