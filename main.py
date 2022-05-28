from datetime import datetime
import random
import multiprocessing
import ctypes
import threading
from pynput.keyboard import Key, Listener
import pyautogui
import time
from memory_profiler import profile

H_scr, W_scr = pyautogui.screenshot().size
script_state = 0
action_state = 0
loop_bool = 0

step_to_image_name = {
    'close': 'images_to_find/_then_reconnect_2.png',
    'stopped': 'images_to_find/stopped.png',
    'if_then_reconnect_2': 'images_to_find/if_then_reconnect_2.png',
    'is_running': 'images_to_find/is_running.png',
    'ok': 'images_to_find/ok.png',
    'connect': 'images_to_find/if.png',
    'running': 'images_to_find/running.png',
    'capcha': 'images_to_find/capcha.png',
    'g_drive': 'images_to_find/connect_to_gdrive.png',
    'reconnect': 'images_to_find/reconnect.png',
    'gpu': 'images_to_find/gpu.png',
    'change_acc': 'images_to_find/step--1-coord.png',
    'choose_acc': 'images_to_find/choose acc.png',
    'allow': 'images_to_find/step-0-optional.png',
    'auth': 'images_to_find/step-3.png',
}

account_to_image_name = {
    'deezzy666': 'images_to_find/auth/B.png',
    'dezzerart': 'images_to_find/auth/J.png'
}


def select_next_account(current_account):
    next_account = 'deezzy666'
    if current_account != 'dezzerart':
        next_account = 'dezzerart'
    return next_account


def move_mouse(mouse_coords):
    max_x, max_y = pyautogui.size()
    cur_x, cur_y = mouse_coords

    x_range = max_x - cur_x
    if x_range < 100:
        new_x = cur_x - random.randrange(1, 25, 1)
    else:
        new_x = cur_x + random.randrange(1, 15, 1)

    y_range = max_y - cur_y
    if y_range < 100:
        new_y = cur_y - random.randrange(1, 15, 1)
    else:
        new_y = cur_y + random.randrange(1, 15, 1)

    return (new_x, new_y)


@profile
def search_and_click_on_image(image_to_click_on, conf):
    img_location_box = pyautogui.locateOnScreen(image_to_click_on, confidence=conf)  # image_to_click_on is a path
    if img_location_box:
        img_center = pyautogui.center(img_location_box)
        box_x, box_y = img_center
        pyautogui.click(box_x, box_y)  # clicks the center of where the 7 button was found
    else:
        pass


def press_combination(key1, key2):
    pyautogui.keyDown(key1)
    time.sleep(0.3)
    pyautogui.keyDown(key2)
    time.sleep(0.3)
    pyautogui.keyUp(key1)
    time.sleep(0.3)
    pyautogui.keyUp(key2)


def main_loop():
    global script_state
    while (loop_bool):
        if pyautogui.locateOnScreen('images_to_find/site-colab.png', confidence=0.8) or pyautogui.locateOnScreen(
                'images_to_find/site-auth.png', confidence=0.9):
            script_state = 1

            if pyautogui.locateOnScreen(step_to_image_name['capcha'], confidence=0.8):
                search_and_click_on_image(step_to_image_name['capcha'], 0.8)
                print("Capcha found")

        else:
            script_state = 0
        # print("State %s" % (script_state))
        time.sleep(4)

    print("main_loop ended")


def run():
    global loop_bool

    loop_bool = 1
    ctypes.windll.user32.MessageBoxW(0, "Auto-learning script activated", "Ok", 0x1000)
    print("Activated")

    def on_release(key):

        global loop_bool
        if key == Key.alt_r:
            loop_bool = 1
            ctypes.windll.user32.MessageBoxW(0, "Script is working", "Ok", 0x1000)
            threading.Thread(target=main_loop).start()
            threading.Thread(target=test_loop).start()

            print('working')

        if key == Key.ctrl_r:
            loop_bool = 0
            ctypes.windll.user32.MessageBoxW(0, "Script stopped", "Ok", 0x1000)
            # listener.stop()

        if key == Key.shift_r:
            global action_state
            action_state = 6
            print('ACTION STATE 6')
            # listener.stop()

    with Listener(
            on_press=None,
            on_release=on_release) as listener:
        listener.join()


def press_Tab_N_times_and_Enter(n):
    for t in range(0, n):
        pyautogui.keyDown('tab')
        time.sleep(0.1)
        pyautogui.keyUp('tab')
        time.sleep(0.1)
    pyautogui.keyDown('enter')
    time.sleep(0.3)
    pyautogui.keyUp('enter')


def test_loop():
    global loop_bool
    global script_state
    global action_state
    current_account = ''
    prev_mouse_coords = pyautogui.position()

    while (loop_bool):
        if script_state == 1:
            try:
                print(action_state)

                if action_state == 0:
                    if pyautogui.locateOnScreen(step_to_image_name['connect'], confidence=0.9) or \
                            pyautogui.locateOnScreen(step_to_image_name['reconnect'], confidence=0.9):
                        print("Start learning!")
                        press_combination('ctrl', 'f9')
                        time.sleep(2)
                    elif pyautogui.locateOnScreen(step_to_image_name['running'], confidence=0.9):
                        action_state = 6
                        continue

                    if pyautogui.locateOnScreen(step_to_image_name['allow'], confidence=0.9):
                        search_and_click_on_image(step_to_image_name['allow'], 0.9)
                        action_state = 0
                        print(action_state)
                        time.sleep(2)
                    if pyautogui.locateOnScreen(step_to_image_name['ok'], confidence=0.9):
                        search_and_click_on_image(step_to_image_name['ok'], 0.9)
                        action_state = 0
                        print(action_state)
                        time.sleep(2)

                    if pyautogui.locateOnScreen(step_to_image_name['g_drive'], confidence=0.7):
                        search_and_click_on_image(step_to_image_name['g_drive'], 0.8)
                        action_state = 2
                        print(action_state)
                        time.sleep(0.5)

                if action_state == 2:

                    if pyautogui.locateOnScreen(step_to_image_name['gpu'], confidence=0.7):
                        search_and_click_on_image(step_to_image_name['gpu'], 0.9)
                        print(action_state)
                        action_state = -1
                        time.sleep(0.5)
                    img_path = step_to_image_name['choose_acc']
                    if pyautogui.locateOnScreen(img_path, confidence=0.8):
                        # TABS
                        print("tab pressed")
                        press_Tab_N_times_and_Enter(2)
                        time.sleep(4)
                        press_Tab_N_times_and_Enter(14)

                        time.sleep(2)
                        action_state = 6

                if action_state == 6:
                    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    # press_combination('alt', 'tab')
                    time.sleep(15)
                    ##TODO check if @state-6-check or @capcha-ceck or @turnoff-check
                    if pyautogui.locateOnScreen(step_to_image_name['connect'], confidence=0.9) or \
                            pyautogui.locateOnScreen(step_to_image_name['reconnect'], confidence=0.9):
                        search_and_click_on_image(step_to_image_name['reconnect'], 0.9)
                        print("Connecting")
                        action_state = 0
                    elif pyautogui.locateOnScreen(step_to_image_name['if_then_reconnect_2'], confidence=0.9):
                        search_and_click_on_image(step_to_image_name['close'], 0.9)
                        print("Reconnecting")
                        action_state = 0
                    else:
                        mouse_coords = pyautogui.position()
                        if prev_mouse_coords == mouse_coords:
                            new_coords = move_mouse(mouse_coords)
                            pyautogui.moveTo(new_coords)
                            prev_mouse_coords = new_coords
                            print(prev_mouse_coords)
                        prev_mouse_coords = mouse_coords
                        print("Mouse cords:", mouse_coords)

                if action_state == -1:
                    for el in account_to_image_name.keys():
                        img_path = account_to_image_name[el]
                        if pyautogui.locateOnScreen(img_path, confidence=0.95):
                            search_and_click_on_image(img_path, 0.95)
                            print(img_path)
                            current_account = el
                            print(current_account)
                            action_state = -2
                            break
                if action_state == -2:
                    current_account = select_next_account(current_account)

                    img_path = account_to_image_name[current_account]
                    if pyautogui.locateOnScreen(img_path, confidence=0.95):
                        search_and_click_on_image(img_path, 0.95)
                        print(img_path)
                        action_state = 0
                        time.sleep(0.5)

                time.sleep(1)
                print("action_state: ", action_state)

            except KeyError as e:
                raise ValueError('Undefined unit: {}'.format(e.args[0]))
    print("test_loop ended")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(multiprocessing.cpu_count())
    threading.Thread(target=run).start()
    threading.Thread(target=main_loop).start()
    threading.Thread(target=test_loop).start()
