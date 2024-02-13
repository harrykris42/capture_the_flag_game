from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

tnl = []
ansd = {}
tndq = {}
tndd = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tn = request.form.get('tn')
        tnl.append(tn)
        socketio.emit('utnl', {'tnlid': tnl})
        return redirect(url_for('wait', tn=tn))
    return render_template('login.html')

@app.route('/<tn>/wait')
def wait(tn):
    if len(tnl) == 3:
        return redirect(url_for('q1', tn=tn))
    return render_template('wait.html', tnl=tnl)

@app.route('/<tn>/q1', methods=['GET', 'POST'])
def q1(tn):
    if request.method == 'POST':
        ans = request.form.get('ans')
        ansd[tn]=ans.lower()
        socketio.emit('uansd', {'ansd': ansd})
        return redirect(url_for('wait_q1', tn=tn))
    return render_template('q1.html', tn=tn)

@app.route('/<tn>/wait_q1')
def wait_q1(tn):
    if len(ansd) == 3:
        return redirect(url_for('rank', tn=tn))
    return render_template('wait_q1.html', ansd=ansd)

@app.route('/<tn>/rank')
def rank(tn):
    global tndq, tndd
    for key, value in ansd.items():
        if value == 'blue':
            tndq[key] = value
        else:
            tndd[key] = value
    return render_template('rank.html', tndq=tndq, tndd=tndd, tn=tn)

if __name__ == '__main__':
    socketio.run(app, debug=True)
