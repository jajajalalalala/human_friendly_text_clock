import HumanFriendlyTextClock as clock
import argparse
from datetime import datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", default=datetime.now().strftime("%H:%M"),
                        help="Insert time a time in H:MM or HH:MM format, default current time")
    
    args = vars(parser.parse_args())
    print(clock.get_human_friendly_text(args['time']))
