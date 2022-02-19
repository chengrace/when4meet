from datetime import datetime

@app.route("/calendar/<title>")
def create_calendar_event(title):
    db.calendar.insert_one({'title': str(title), 'date_created': str(date.today())})
    return jsonify(message="success")

@app.route("/calendar/<user>")
def add_user(user):
    db.calendar.update_one({'title': str(title), {"$set": {'user_id': str(user)}}})
    return jsonify(message="success")
