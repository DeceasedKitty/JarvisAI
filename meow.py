import speech_recognition as sr
import pyautogui
import time

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.energy_threshold = 100 

def hotkeys_pressed(keys):
    print(f"Pressing: {keys}")
    pyautogui.hotkey(*keys)
    print("Clipped, Stark.")

mic_list = sr.Microphone.list_microphone_names() # selects mic
input_mics = [name for name in mic_list if "microphone" in name.lower() or "input" in name.lower()] # ignores anything that aint got input in it

if not input_mics: # :troll_pixels:
    print("no mic selected")
    exit()

print("mics:")
for index, name in enumerate(input_mics):
    print(f"{index}: {name}")

mic_index = int(input("pick ur mic: "))

print(f"Using: {input_mics[mic_index]}")


while True:
    try:
        with sr.Microphone(device_index=mic_index) as source:
            print(f"Using: {mic_list[mic_index]}")
            recognizer.adjust_for_ambient_noise(source)
            print("Waiting. . .")
            
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio).lower()
            print("Repeat: " + text)

            if "jarvis clip that" in text:  # jarvis clip that :troll:
                trigger_hotkey(['alt', '11'])
            elif "jarvis start" in text:
                trigger_hotkey(['alt', 'f9'])
            elif "jarvis stop" in text:
                trigger_hotkey(['alt', 'f9']) # this one rarely works on nvidia :sob:

    except IndexError:
        print("Mic issue lol, retry") # skill issue
        break
# ts is so ass bruh
