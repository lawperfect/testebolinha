import cv2
import pyautogui
from options import *


def make_verify():
    try:
        left, top, width, height = 1533, 168, 41, 24
        verify = pyautogui.screenshot(region=(left, top, width, height))
        verify.save("prismatic_ring.png")
    except Exception as e:
        print(f"Erro ao tentar a verificação: {e}")


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


make_verify()
