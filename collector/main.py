from tasks import scheduler

if __name__ == '__main__':

    try:
        scheduler.start()

    except KeyboardInterrupt:
        scheduler.shutdown()