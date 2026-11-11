from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def hello_about():
    return render_template('about.html')

@app.route('/service')
def hello_service():
    return render_template('service.html')

if __name__=='__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )