import pyautogui
import time
import speech_recognition as sr


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='de')
            print(f"user said:{statement}\n")

        except Exception as e:
            return "None"
        return statement


def Spotifystart():
    pyautogui.click(320, 1060)  # Position of the SpotifyIcon in Toolbar
    time.sleep(3)
    pyautogui.press("space")
    pyautogui.click(320, 1060)


def Spotifystart1():
    pyautogui.click(320, 1060)
    time.sleep(3)
    pyautogui.press("space")
    pyautogui.click(320, 1060)


def Spotifynext():
    pyautogui.click(320, 1060)
    pyautogui.hotkey('ctrlleft', 'right')
    time.sleep(1)
    pyautogui.click(320, 1060)


def Spotifyquit():
    pyautogui.click(320, 1060)
    pyautogui.hotkey('ctrlleft', 'shiftleft', "q")


def Spotifylouder():
    pyautogui.click(320, 1060)
    for i in range(2):
        pyautogui.hotkey('ctrlleft', 'up')
    time.sleep(1)
    pyautogui.click(320, 1060)


def Spotifyshuffle():
    pyautogui.click(320, 1060)
    pyautogui.hotkey('ctrlleft', 's')
    time.sleep(1)
    pyautogui.click(320, 1060)


def Spotifysearch():
    pyautogui.click(320, 1060)
    pyautogui.hotkey('ctrlleft', 'l')
    time.sleep(1)
    songwunsch = takeCommand().lower()
    pyautogui.typewrite(songwunsch)
    time.sleep(2)
    pyautogui.click(1250, 200)
    time.sleep(1)
    pyautogui.click(320, 1060)


def Spotifypause():
    pyautogui.click(320, 1060)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.click(320, 1060)


def Spotifyquieter():
    pyautogui.click(320, 1060)
    for i in range(2):
        pyautogui.hotkey('ctrlleft', 'down')
    time.sleep(1)
    pyautogui.click(320, 1060)


while 1 != 0:
    statement = takeCommand().lower()
    if "spotify" in statement:
        Spotifystart()
        while 1 != 0:
            statement2 = takeCommand().lower()
            if "next" in statement2:
                Spotifynext()
                continue
            elif "lauter" in statement2:
                Spotifylouder()
                continue
            elif "leiser" in statement2:
                Spotifyquieter()
                continue
            elif "pause" in statement2:
                Spotifypause()
                continue
            elif "aus" in statement2:
                Spotifyquit()
            elif "suche" in statement2:
                Spotifysearch()
                continue
            elif "shuffle" in statement2:
                Spotifyshuffle()
                continue
            elif "spotify" in statement2:
                Spotifystart1()
                continue
            elif "stopp" in statement2:
                quit()
            else:
                continue