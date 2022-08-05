import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'dynamic_schedular.settings')

app = Celery('dynamic_schedular')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'test-custom-tasks-and-db-tasks': {
    #     'task': 'dynamic_schedular.celery.hello_world_2',
    #     'schedule': 15.0,
    # },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task(bind=True)
def hello_world(self):
    print('Hello world!')

@app.task(bind=True)
def hello_world_2(self):
    print("db and custom schedular simultaneously working")