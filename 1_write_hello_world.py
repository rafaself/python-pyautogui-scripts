import pyautogui

# Pressiona a tecla windows
pyautogui.press('win')
pyautogui.press('space')
pyautogui.write("notepad")
pyautogui.press('enter', interval=1)

# Segura CTRL esquerdo e pressiona a tecla n
with pyautogui.hold('ctrlleft'):
        pyautogui.press('n')
        
# Digita o texto com um intervalo de 0,25 segundos
pyautogui.write("Hello World!", interval=0.25)