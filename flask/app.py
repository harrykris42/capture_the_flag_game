from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

tnl = []
ansd1 = {}
ansd2 = {}
ansd3 = {}
sb={}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tn = request.form.get('tn')
        tnl.append(tn)
        socketio.emit('stnl', {'tnlid': tnl})
        return redirect(url_for('wait', tn=tn))
    return render_template('login.html')

@app.route('/<tn>/wait')
def wait(tn):
    if len(tnl) == 2:
        return redirect(url_for('q1', tn=tn))
    return render_template('wait.html', tnl=tnl)

@app.route('/<tn>/q1', methods=['GET', 'POST'])
def q1(tn):
    if request.method == 'POST':
        ans1 = request.form.get('ans1')
        ansd1[tn]=ans1.lower()
        socketio.emit('sansd1', {'ansd1id': ansd1})
        return redirect(url_for('wait_q1', tn=tn))
    return render_template('q1.html', tn=tn)

@app.route('/<tn>/wait_q1')
def wait_q1(tn):
    if len(ansd1) == 2:
        for key, value in ansd1.items():
            if value == 'germany':
                sb[key]=sb.get(key,0)+0.5
            else:
                sb[key]=sb.get(key,0)+0.0
        return redirect(url_for('q2', tn=tn))
    return render_template('wait_q1.html', ansd1=ansd1)

@app.route('/<tn>/q2', methods=['GET', 'POST'])
def q2(tn):
    if request.method == 'POST':
        ans2 = request.form.get('ans2')
        ansd2[tn]=ans2.lower()
        socketio.emit('sansd2', {'ansd2id': ansd2})
        return redirect(url_for('wait_q2', tn=tn))
    return render_template('q2.html', sb=sb, tn=tn)

@app.route('/<tn>/wait_q2')
def wait_q2(tn):
    if len(ansd2) == 2:
        for key, value in ansd2.items():
            if value == 'secret':
                sb[key]=sb.get(key,0)+0.5
            else:
                sb[key]=sb.get(key,0)+0.0
        return redirect(url_for('q3', tn=tn))
    return render_template('wait_q2.html', ansd2=ansd2)

@app.route('/<tn>/q3', methods=['GET', 'POST'])
def q3(tn):
    if request.method == 'POST':
        ans3 = request.form.get('ans3')
        ansd3[tn]=ans3.lower()
        socketio.emit('sansd3', {'ansd3id': ansd3})
        return redirect(url_for('wait_q3', tn=tn))
    return render_template('q3.html', sb=sb, tn=tn)

@app.route('/<tn>/wait_q3')
def wait_q3(tn):
    if len(ansd3) == 2:
        for key, value in ansd3.items():
            if value == 'youfoundm3':
                sb[key]=sb.get(key,0)+0.5
            else:
                sb[key]=sb.get(key,0)+0.0
        return redirect(url_for('q4', tn=tn))
    return render_template('wait_q3.html', ansd3=ansd3)

@app.route('/<tn>/q4', methods=['GET', 'POST'])
def q4(tn):
    return render_template('q4.html', sb=sb, tn=tn)


if __name__ == '__main__':
    socketio.run(app, debug=True)
