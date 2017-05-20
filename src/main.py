from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/if')
def name():
    username = request.args.get('username')
    surname = request.args.get('surname')
    if username and surname:
        username = username + ' ' + surname
    elif username and not surname:
        username = username
    elif surname and not username:
        username = surname
    else:
        username = 'World'
    return render_template('index2.html', username=username)

@app.route('/here')
def here():
    username = request.args.get('username') 
    surname =  request.args.get('surname')
    try:
        no_of_times = int(request.args.get('no_of_times'))
    except ValueError:
        no_of_times = 1

    if no_of_times < 1:
        no_of_times = 1
    
    username = (str(username or str()) + ' ' + str(surname or str())) or 'World'

    return render_template('index3.html', username=username, no_of_times=no_of_times)

if __name__ == '__main__':
    app.run(debug=True)

