from flask import render_template, request, jsonify
from app import app, celery
from .tasks import send_email


@app.route('/send_email', methods=['POST'])
def send_email_route():
    email = request.form['email']
    send_email.delay(email)  # Chama a tarefa do Celery de forma assíncrona
    return jsonify({"status": "Email is being sent"}), 202
