from app import celery


@celery.task
def send_email(email):
    print(f"Sending email to {email}")  # Simula o envio de um e-mail
    return f"Email sent to {email}"
