import time
import threading

import click
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


class ClickMouse(threading.Thread):
    def __init__(self, delay, button=Button.left):
        super(ClickMouse, self).__init__()
        self.mouse = Controller()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


@click.command()
@click.option('--delay', default=1, help='Delay between clicks')
def main(delay):
    click_thread = ClickMouse(delay)
    click_thread.start()

    start_stop_key = KeyCode(char='a')
    stop_key = KeyCode(char='b')

    def on_press(key):
        if key == start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == stop_key:
            click_thread.exit()
            exit()

    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
