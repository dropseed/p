import uuid


def command(name):
    return event(name, type="command")


def event(name, type):
    if not is_enabled():
        return

    # need to store the event locally
    # and dispatch them in bulk at some point later?
    data = {
        "name": name,
        "type": type,
        "uuid": uuid.uuid4(),
    }

    # basic machine info? optional? build user "profile"?

    # just append to a file? like a log?

    pass


def purge():
    # delete any local events not dispatched
    pass


def dispatch():
    # project key required by now

    # rename the log for submission
    # (new log created for new events)
    # submit the log
    pass
