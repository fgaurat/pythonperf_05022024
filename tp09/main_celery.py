from celery import Celery,signature

def main():
    app = Celery('tasks', broker='amqp://guest@localhost//', backend="redis://localhost:6379/0")
    # add_task = app.send_task('tasks_celery.add')
    # i = add_task.get(2,3)
    # print(i)

    add_task = signature('tasks_celery.add')
    add = add_task.delay(2,3)
    print(add.get())



if __name__=='__main__':
    main()
