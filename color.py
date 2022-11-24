def light_red(string):
    return "\033[91m%s\033[0m" % string


def light_yellow(string):
    return "\033[93m%s\033[0m" % string

def cyan(string):
    return "\033[96m%s\033[0m" % string

def blue(string):
    return "\033[34m%s\033[0m" % string


def light_gray(string):
    return "\033[37m%s\033[0m" % string


def red(string):
    return "\033[31m%s\033[0m" % string


def dark_gray(string):
    return "\033[90m%s\033[0m" % string


def blink(string):
    return "\033[5m\033[90m%s\033[0m" % string


def light_blue(string):
    return "\033[94m%s\033[0m" % string


def light_green(string):
    return "\033[92m%s\033[0m" % string


def white(string):
    return "\033[97m%s\033[0m" % string


def reset():
    return "\033[0m"