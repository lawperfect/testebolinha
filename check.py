import os
import pyautogui
from PIL import Image
import pytesseract
from options import *
import cv2


def start_tibia_window():
    try:
        left, top, width, height = pixel_window
        verify = pyautogui.screenshot(region=(left, top, width, height))
        verify.save("verify.png")
    except Exception as e:
        print(f"Erro ao iniciar a janela do Tibia: {e}")


def verify_tibia_window():
    try:
        # Defina as coordenadas do retângulo na tela
        left, top, width, height = pixel_window

        # Captura a imagem da janela atual
        verify_active = pyautogui.screenshot(region=(left, top, width, height))
        verify_active.save("verify_active.png")

        # Carrega as imagens que você deseja comparar
        verify = cv2.imread("verify.png")
        verify_active = cv2.imread("verify_active.png")

        # Converte as imagens em escala de cinza
        verify_gray = cv2.cvtColor(verify, cv2.COLOR_BGR2GRAY)
        verify_active_gray = cv2.cvtColor(verify_active, cv2.COLOR_BGR2GRAY)

        # Compara as duas imagens em escala de cinza
        difference = cv2.absdiff(verify_gray, verify_active_gray)

        # Se as imagens forem idênticas, a diferença será uma imagem completamente preta
        if cv2.countNonZero(difference) == 0:
            window_check = True
        else:
            window_check = False

        return window_check

    except Exception as e:
        print(f"Erro ao verificar a janela do Tibia: {e}")


# Chame a função para verificar as imagens
result = verify_tibia_window()
if result:
    print("As imagens são idênticas.")
else:
    print("As imagens são diferentes.")


def status_check():
    hp_result_raw = 0
    mp_result_raw = 0
    try:
        # Defina as coordenadas do retângulo na tela
        left, top, width, height = pixel_bar
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot.save("screenshot.png")
        text = pytesseract.image_to_string(Image.open(
            "screenshot.png"), config='--psm 6 -c tessedit_char_whitelist=0123456789')
        try:
            os.remove("screenshot.png")
        except PermissionError:
            print("Erro de permissão ao excluir o arquivo 'screenshot.png'.")

        linhas = text.split("\n")
        if len(linhas) >= 2:
            try:
                hp = int(linhas[0])
                mp = int(linhas[1])
                hp_result_raw = hp_max - hp
                mp_result_raw = mp_max - mp
                print("HP:", hp_result_raw)
                print("MP:", mp_result_raw)
                # Retorna True para indicar que é o Tibia
                return hp_result_raw, mp_result_raw, True
            except ValueError:
                print("Erro ao converter valor HP ou MP para int.")
                return 0, 0, False
        else:
            print("A string não contém pelo menos duas linhas com números.")
            return 0, 0, False  # Retorna False para indicar que não é o Tibia
    except Exception as e:
        print(f"Erro ao verificar o status: {e}")


def ring_check(pixel_ring, verify_ring):
    try:
        # Defina as coordenadas do retângulo na tela
        left, top, width, height = pixel_ring

        # Captura a imagem da janela atual
        active_ring = pyautogui.screenshot(region=(left, top, width, height))
        active_ring.save("active_ring.png")

        # Carrega as imagens que você deseja comparar
        verify = cv2.imread(verify_ring)
        active_ring = cv2.imread("active_ring.png")

        # Compara as duas imagens sem converter para escala de cinza
        difference = cv2.absdiff(verify, active_ring)

        # Converte a diferença para escala de cinza
        difference_gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

        # Se as imagens forem idênticas, a diferença será uma imagem completamente preta
        if cv2.countNonZero(difference_gray) == 0:
            ring_check = True
        else:
            ring_check = False

        return ring_check

    except Exception as e:
        print(f"Erro ao verificar o seu ring: {e}")


def amulet_check(pixel_amulet, verify_amulet):
    try:
        # Defina as coordenadas do retângulo na tela
        left, top, width, height = pixel_amulet

        # Captura a imagem da janela atual
        active_amulet = pyautogui.screenshot(region=(left, top, width, height))
        active_amulet.save("active_amulet.png")

        # Carrega as imagens que você deseja comparar
        verify = cv2.imread(verify_amulet)
        active_amulet = cv2.imread("active_amulet.png")

        # Compara as duas imagens sem converter para escala de cinza
        difference = cv2.absdiff(verify, active_amulet)

        # Converte a diferença para escala de cinza
        difference_gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)

        # Se as imagens forem idênticas, a diferença será uma imagem completamente preta
        if cv2.countNonZero(difference_gray) == 0:
            amulet_check = True
        else:
            amulet_check = False

        return amulet_check

    except Exception as e:
        print(f"Erro ao verificar o seu amulet: {e}")
