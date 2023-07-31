import sys


def get_args():
    """
    Reads arguments from cmd and returns them as dictionary.

    """
    device_name = None

    for param in sys.argv:
        if "--deviceName=" in param:
            device_name = str(param).replace('--deviceName=', '')
            print("\n--deviceName={}".format(device_name))

    return {
        'deviceName': device_name,
    }
