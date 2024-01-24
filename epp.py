import pyautogui
from time import sleep

pyautogui.click(719,385,duration=1)
pyautogui.write('jhonatan')
pyautogui.click(724,411,duration=1)
pyautogui.write('123456')
pyautogui.click(592,441,duration=1)


with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(420,372,duration=0.5)
        pyautogui.write(produto)
        pyautogui.click(416,398,duration=0.5)
        pyautogui.write(quantidade)
        pyautogui.click(435,424,duration=0.5)
        pyautogui.write(preco)
        pyautogui.click(311,585,duration=0.5)

        # sleep(1)

