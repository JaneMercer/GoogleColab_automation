from datetime import datetime
import random
import multiprocessing
import ctypes
import threading
from pynput.keyboard import Key, Listener
import pyautogui
import time

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
    'reconnect': 'images_to_find/reconnect.png',
    'change_acc': 'images_to_find/step--1-coord.png',
    'allow': 'images_to_find/step-0-optional.png',
    'gpu': 'images_to_find/gpu.png',
    'g_drive': 'images_to_find/step-1.png',
    'pick_drive': 'images_to_find/step-2.png',
    'auth': 'images_to_find/step-3.png',
    'copy': 'images_to_find/step-4.png',
    'paste': 'images_to_find/step-5.png',
    'paste2': 'images_to_find/step-5_2.png',
}

account_to_image_name = {
    'lusy': 'images_to_find/auth/A.png',
    'white': 'images_to_find/auth/A-orange.png',
    # 'deezzy666': 'images_to_find/auth/B.png',
    '580': 'images_to_find/auth/I.png',
    'dezzerart': 'images_to_find/auth/J.png',
    'bubzik': 'images_to_find/auth/bubzik.png'
}


def select_next_account(current_account):
    next_account = '580'
    if current_account == 'lusy':
        next_account = 'white'
    elif current_account == 'white':
        # next_account = 'deezzy666'
        next_account = 'dezzerart'

    # elif current_account == 'deezzy666':
    #     next_account = 'dezzerart'

    elif current_account == 'dezzerart':
        next_account = '580'

    elif current_account == '580':
        next_account = 'bubzik'

    elif current_account == 'bubzik':
        next_account = 'lusy'
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
                        search_and_click_on_image(step_to_image_name['g_drive'], 0.9)
                        action_state = 2
                        print(action_state)
                        time.sleep(0.5)
                    elif pyautogui.locateOnScreen(step_to_image_name['gpu'], confidence=0.7):
                        search_and_click_on_image(step_to_image_name['gpu'], 0.9)
                        print(action_state)
                        action_state = -1
                        time.sleep(0.5)

                if action_state == 2:
                    img_path = step_to_image_name['pick_drive']
                    if pyautogui.locateOnScreen(img_path, confidence=0.9):
                        search_and_click_on_image(img_path, 0.9)
                        print(img_path)
                        action_state = 3
                        time.sleep(0.5)
                if action_state == 3:
                    img_path = step_to_image_name['auth']
                    if pyautogui.locateOnScreen(img_path, confidence=0.9):
                        search_and_click_on_image(img_path, 0.9)
                        print(img_path)
                        action_state = 4
                        time.sleep(0.5)
                if action_state == 4:
                    img_path = step_to_image_name['copy']
                    if pyautogui.locateOnScreen(img_path, confidence=0.9):
                        search_and_click_on_image(img_path, 0.9)
                        action_state = 5
                        print("Closing tab!")
                        time.sleep(0.5)
                        press_combination('ctrl', 'w')
                        time.sleep(0.5)
                if action_state == 5:
                    img_path = step_to_image_name['paste']

                    img_path_2 = step_to_image_name['paste2']
                    if pyautogui.locateOnScreen(img_path, confidence=0.75) or pyautogui.locateOnScreen(img_path_2, confidence=0.75) :
                        search_and_click_on_image(img_path, 0.75)
                        search_and_click_on_image(img_path_2, 0.75)
                        action_state = 6

                        print("Pasting!")
                        press_combination('ctrl', 'v')
                        time.sleep(0.3)
                        pyautogui.keyDown('enter')
                        time.sleep(0.3)
                        pyautogui.keyUp('enter')

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
                        """
                    elif pyautogui.locateOnScreen(step_to_image_name['stopped'], confidence=0.9):

                        press_combination('ctrl', 'm')
                        time.sleep(0.3)
                        print("Restarting")
                        action_state = 0

                        time.sleep(3)
                        """
                    else:
                        mouse_coords = pyautogui.position()
                        if prev_mouse_coords == mouse_coords:
                            new_coords = move_mouse(mouse_coords)
                            pyautogui.moveTo(new_coords)
                            prev_mouse_coords = new_coords
                            print(prev_mouse_coords)
                        prev_mouse_coords = mouse_coords
                        print("Mouse cords:",mouse_coords)

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
                # можно также присвоить значение по умолчанию вместо бросания исключения
                raise ValueError('Undefined unit: {}'.format(e.args[0]))
    print("test_loop ended")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(multiprocessing.cpu_count())
    threading.Thread(target=run).start()
    threading.Thread(target=main_loop).start()
    threading.Thread(target=test_loop).start()
