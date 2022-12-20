from datetime import datetime
from time import sleep


def calc_func_duration(func):
    def wrapped_func(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, *kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        res = {
            "Hour": duration.seconds // 3600,
            "Minutes": duration.seconds // 60,
            "seconds": duration.seconds % 60
        }
        print(res)
        return result
    return wrapped_func


@calc_func_duration
def simpletest():
    sleep(5)
    return "This was just a test"


if __name__ == "__main__":
    simpletest()
