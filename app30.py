# importa bibliotecas
import pyautogui as aut
import time

link_reposi = input("Digite o link do repositório: ")
versao = input("Digite o nome da versão: ")
# tempo que cada comando demora para executar
aut.PAUSE = 1
# instruções
aut.press('win')
aut.write('vscode')
aut.press('enter')
# espera 10 segundos para abrir o vscode e continuar com os comandos
time.sleep(5)
# continua as instruções
aut.hotkey('ctrl', 'j')
time.sleep(5)

aut.write('git init')
aut.press('enter')
aut.write('git add .')
aut.press('enter')
aut.write(f'git commit -m "{versao}"')
aut.press('enter')
# espera 5 segundos para dar tempo de fazer o commit
time.sleep(5)
# continua as instruções
aut.write('git branch -M main')
aut.press('enter')
aut.write(f'git remote add origin {link_reposi}')
aut.press('enter')

aut.write('git push -u origin main')
aut.press('enter')