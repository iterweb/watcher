#!/usr/bin/python 3.7.8
# -*- coding: utf-8 -*-
import keyboard
from pynput.mouse import Controller
import time
import cv2
import telebot

bot = telebot.TeleBot('') # токен бота телеграм
chat_id = '' # id канала, пример @my_chanel
mouse = Controller()
m_position = (0, 0) # позиция мишки



def on_script(): # функция запуска скрипта
    mouse.position = (500, 500) # переводит курсор, что-бы было понятно, когда скрипт находится в режиме ожидания
    while True:
        time.sleep(0.5)
        if keyboard.is_pressed('ctrl+alt'): # комбинация для запуска
            main()

def main():
    mouse.position = m_position # переводит курсор по заданным координатам из 12 строки
    while mouse.position == m_position: # проверка, находится ли курсор в заданных координатах
        time.sleep(0.5)
        if keyboard.is_pressed('alt+a'): # вкл. ожидания 
            on_script()
        if  mouse.position != m_position:
            run_script()

def run_script():
    p = 0
  
    try:
        cam = cv2.VideoCapture(0) # вкл. камеры
    except:
        cam = cv2.VideoCapture(1) 
    while p < 3: # количество снимков
        p +=1
        ret, frame = cam.read() # делаем снимок
        cv2.imwrite('cam.png', frame) # сохраняем
        photo = open('cam.png', 'rb') # откр. для чтения в двоичном режиме
        try:
            bot.send_photo(chat_id, photo) # отправка в телеграм
        except:
            pass
        time.sleep(1) # задержка 1 сек.
    cam.release() # откл. камеру
    time.sleep(5)
    return main()

if __name__ == '__main__':
    main()
