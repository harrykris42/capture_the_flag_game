from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_socketio import SocketIO, emit
import time
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

waiting_room_teams = set()
ready_teams = set()
first_team_answers = {}

@app.route('/')
def enter_team_name():
    return render_template('index.html')

@socketio.on('connect', namespace='/waiting_room')
def handle_waiting_room_connect():
    emit('update_waiting_room', {'teams': list(waiting_room_teams)})

    # Calculate the number of remaining teams needed for redirection
    remaining_teams = 4 - len(waiting_room_teams)

    # Emit a message indicating the number of teams needed for redirection
    socketio.emit('waiting_for_teams', {'remaining_teams': remaining_teams}, namespace='/waiting_room')

    # Check if there are three teams, and if yes, emit the 'start_questions' event
    if len(waiting_room_teams) == 4:
        socketio.emit('start_questions', namespace='/waiting_room')

@app.route('/submit_team_name', methods=['POST'])
def submit_team_name():
    team_name = request.form['team_name']
    waiting_room_teams.add(team_name)
    socketio.emit('update_waiting_room', {'teams': list(waiting_room_teams)}, namespace='/waiting_room')
    return redirect(url_for('waiting_room'))

@app.route('/waiting_room')
def waiting_room():
    return render_template('waiting_room.html')

@socketio.on('ready_to_congratulate', namespace='/waiting_room')
def handle_ready_to_congratulate(data):
    team_name = data['team_name']
    ready_teams.add(team_name)
    
    print(f"Team {team_name} is ready. Total ready teams: {len(ready_teams)}")
    print(f"Waiting room teams: {waiting_room_teams}")

    if len(ready_teams) == len(waiting_room_teams):
        print("All teams are ready. Redirecting to the first question page.")
        socketio.emit('start_questions', namespace='/waiting_room')

from flask import jsonify

# ...

@app.route('/questions/<team_name>', methods=['GET', 'POST'])
def questions(team_name):
    global first_team_answers

    if request.method == 'POST':
        answer = request.json['answer'].lower()

        # Check the answer for the common question
        if answer == 'blue':
            # Record the time when the correct answer is submitted
            if team_name not in first_team_answers:
                first_team_answers[team_name] = time.time()

            return jsonify({'result': 'correct'})
        else:
            return jsonify({'result': 'incorrect'})

    return render_template('questions.html', team_name=team_name)

@app.route('/submit_answer/<team_name>', methods=['POST'])
def submit_answer(team_name):
    answer = request.json['answer'].lower()

    # Check the answer for the common question
    if answer == 'blue':
        # Record the time when the correct answer is submitted
        if team_name not in first_team_answers:
            first_team_answers[team_name] = time.time()

        return jsonify({'result': 'correct'})
    else:
        return jsonify({'result': 'incorrect'})

@app.route('/disqualified')
def disqualified():
    return render_template('disqualified.html', disqualified_team_name=None)  # Handle case where disqualified_team_name is not provided

@app.route('/correct_answer_and_congratulate')
def correct_answer_and_congratulate():
    return render_template('correct_answer_and_congratulate.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
