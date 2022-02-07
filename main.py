import HumanFriendlyTextClock as clock
import argparse
if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # args = parser.parse_args()
    x = input()
    print(clock.get_human_friendly_text(x))