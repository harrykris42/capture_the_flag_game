from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

tnl = []
ansd1 = {}
ansd2 = {}
ansd3 = {}
ansd4={}
ansd5={}
ansd6={}
ansd7={}
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
    if len(tnl) == 5:
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
    if len(ansd1) == 5:
        for key, value in ansd1.items():
            if value == "blitzkriegctf{germany}":
                sb[key]=sb.get(key,0)+2.5
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
    if len(ansd2) == 5:
        for key, value in ansd2.items():
            if value == 'blitzkriegctf{alan turing}':
                sb[key]=sb.get(key,0)+5
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
    if len(ansd3) == 5:
        for key, value in ansd3.items():
            if value == 'blitzkriegctf{youfoundm3}':
                sb[key]=sb.get(key,0)+5
            else:
                sb[key]=sb.get(key,0)+0.0
        return redirect(url_for('q4', tn=tn))
    return render_template('wait_q3.html', ansd3=ansd3)

@app.route('/<tn>/q4', methods=['GET', 'POST'])
def q4(tn):
    if request.method == 'POST':
        ans4 = request.form.get('ans4')
        ansd4[tn]=ans4.lower()
        socketio.emit('sansd4', {'ansd4id': ansd4})
        return redirect(url_for('wait_q4', tn=tn))
    return render_template('q4.html', sb=sb, tn=tn)

@app.route('/<tn>/wait_q4')
def wait_q4(tn):
    if len(ansd4) == 5:
        for key, value in ansd4.items():
            if value == 'blitzkriegctf{33}':
                sb[key]=sb.get(key,0)+12.5
            else:
                sb[key]=sb.get(key,0)+0.0
        return redirect(url_for('q5', tn=tn))
    return render_template('wait_q4.html', ansd4=ansd4)

@app.route('/<tn>/q5', methods=['GET', 'POST'])
def q5(tn):
    if request.method == 'POST':
        ans5 = request.form.get('ans5')
        ansd5[tn]=ans5.lower()
        socketio.emit('sansd5', {'ansd5id': ansd5})
        return redirect(url_for('wait_q5', tn=tn))
    return render_template('q5.html', sb=sb, tn=tn)

@app.route('/<tn>/wait_q5')
def wait_q5(tn):
    if len(ansd5) == 5:
        for key, value in ansd5.items():
            if value == 'blitzkriegctf{01}':
                sb[key]=sb.get(key,0)+12.5
            else:
                sb[key]=sb.get(key,0)+0.0
        return redirect(url_for('q6', tn=tn))
    return render_template('wait_q5.html', ansd5=ansd5)

@app.route('/<tn>/q6', methods=['GET', 'POST'])
def q6(tn):
    if request.method == 'POST':
        ans6 = request.form.get('ans6')
        ansd6[tn]=ans6.lower()
        socketio.emit('sansd6', {'ansd6id': ansd6})
        return redirect(url_for('wait_q6', tn=tn))
    return render_template('q6.html', sb=sb, tn=tn)

@app.route('/<tn>/wait_q6')
def wait_q6(tn):
    if len(ansd6) == 5:
        for key, value in ansd6.items():
            if value == 'blitzkriegctf{marcus wanner}':
                sb[key]=sb.get(key,0)+12.5
            else:
                sb[key]=sb.get(key,0)+0.0
        return redirect(url_for('q7', tn=tn))
    return render_template('wait_q6.html', ansd6=ansd6)

@app.route('/<tn>/7', methods=['GET', 'POST'])
def q7(tn):
    if request.method == 'POST':
        ans7 = request.form.get('ans7')
        ansd7[tn]=ans7.lower()
        socketio.emit('sansd7', {'ansd7id': ansd7})
        return redirect(url_for('wait_q7', tn=tn))
    return render_template('q7.html', sb=sb, tn=tn)

@app.route('/<tn>/wait_q7')
def wait_q7(tn):
    if len(ansd7) == 5:
        for key, value in ansd7.items():
            if value == 'blitzkriegctf{cicada 3301}':
                sb[key]=sb.get(key,0)+12.5
            else:
                sb[key]=sb.get(key,0)+0.0
        return redirect(url_for('q8', tn=tn))
    return render_template('wait_q7.html', ansd7=ansd7)

@app.route('/<tn>/8', methods=['GET', 'POST'])
def q8(tn):
    return render_template('q8.html', sb=sb, tn=tn)

if __name__ == '__main__':
    socketio.run(app, host='172.16.36.42' ,port=5000 ,debug=True)
