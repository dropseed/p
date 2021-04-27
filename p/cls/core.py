def is_enabled():
    return True


def request_permission(force=False):
    """
    Prompt the user for permission to report their usage.
    Only shows the prompt once by default, use force=True to override.
    """
    # prompt the user w/ example of event, etc. making this easy for user to enable
    #
    has_requested = False

    if has_requested and not force:
        return

    should_enable = True

    if should_enable:
        enable()
    else:
        disable()


def reset():
    # clear prompt asked, enabled/disabled, anything else
    pass


def enable():
    # save a marker that we are enabled
    pass


def disable():
    pass


