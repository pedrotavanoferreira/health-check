from microbit import *
import random
quant_agua = 2000
intervalo_agua = 6
intervalo_ativi = 5
intervalo_mensg = 1
atividade_fisica = False

while True:
    if button_a.is_pressed:
        quant_agua = quant_agua -200

    if button_b.is_pressed:
      atividade_fisica = True

    if quant_agua = 0:
        display.scroll("parabens voce completou a meta de agua diaria")

