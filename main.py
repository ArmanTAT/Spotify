import speech_recognition as sr
import webbrowser
import time
import pyautogui

confidence = 0.75

# Set up the recognizer
r = sr.Recognizer()

while True:
    # Start listening for audio
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Try to recognize the audio
    try:
        text = r.recognize_google(audio)
        if "spotify" in text.lower():
            print("Spotify detected!")
            webbrowser.open("https://open.spotify.com/")

            # Wait for web page to load
            time.sleep(6)

            # Look for images and click on them
            while True:
                image = pyautogui.locateOnScreen('daily.png', confidence=confidence)
                if image is not None:
                    center = pyautogui.center(image)
                    pyautogui.click(center)

                    # Wait for second image to appear
                    time.sleep(1)

                    image2 = pyautogui.locateOnScreen('play.png', confidence=confidence)
                    if image2 is not None:
                        center2 = pyautogui.center(image2)
                        pyautogui.click(center2)
                        pyautogui.click(center2)

                        # Wait for third image to appear
                        time.sleep(1)

                        image3 = pyautogui.locateOnScreen('forward.png', confidence=confidence)
                        if image3 is not None:
                            center3 = pyautogui.center(image3)
                            time.sleep(0.05)
                            pyautogui.click(center3)
                            time.sleep(0.05)
                            pyautogui.click(center3)
                            time.sleep(0.20)
                            pyautogui.click(center3)
                            print("Found it")
                            break
                        else:
                            print("Didn't find it")
                            break
                    else:
                        print("Didn't find it")
                        break
                time.sleep(1)
        else:
            print("Spotify not detected")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error accessing the API: {0}".format(e))
