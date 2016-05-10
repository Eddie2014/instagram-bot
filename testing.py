import pyautogui
import time

for i in range(10):
    coordinate=pyautogui.locateOnScreen('C:\\Users\\Eddie\\Desktop\\instagrambot\\heart.png');
    center=pyautogui.center(coordinate);
    pyautogui.click(center);

    coordinate=pyautogui.locateOnScreen('C:\\Users\\Eddie\\Desktop\\instagrambot\\follow.png');
    center=pyautogui.center(coordinate);
    pyautogui.click(center);

    coordinate=pyautogui.locateOnScreen('C:\\Users\\Eddie\\Desktop\\instagrambot\\next.png');
    center=pyautogui.center(coordinate);
    pyautogui.click(center);
    time.sleep(2);
