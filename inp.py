# import sys,tty,termios
# class _Getch:       
#     def __call__(self):
#             fd = sys.stdin.fileno()
#             old_settings = termios.tcgetattr(fd)
#             try:
#                 tty.setraw(sys.stdin.fileno())
#                 ch = sys.stdin.read(1)
#             finally:
#                 termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#             return ch

# def get():
#     inkey = _Getch()
#     while(1):
#             k=inkey()
#             if k!='':break
#     print ('you pressed', k)

# def main():
#     for i in range(0,25):
#         get()

# if __name__=='__main__':
#     main()




"""Defining input class."""
import sys
import termios
import tty
import signal

class Get:
    """Class to get input."""

    def __call__(self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        except ValueError:
            exit(0)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class AlarmException(Exception):
    """Handling alarm exception."""
    pass


def alarmHandler(signum, frame):
    """Handling timeouts."""
    raise AlarmException


def input_to(getch, timeout=0.3):
    """Taking input from user."""
    # signal.signal(signal.SIGALRM, alarmHandler)
    # signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getch()
        # signal.alarm(0)
        return text
    except AlarmException:
        # signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None
while True:
    getch = Get()
    chbuff = input_to(getch)
    print(chbuff)