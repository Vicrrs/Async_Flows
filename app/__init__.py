from flask import Flask
from celery import Celery


def create_app():
    app = Flask(__name__)
    app.config.update(
        CELERY_BROKER_URL='amqp://localhost//',
        CELERY_RESULT_BACKEND='rpc://'  # Corrigido aqui
    )
    return app


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery


app = create_app()
celery = make_celery(app)
