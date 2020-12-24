#!/usr/bin/python 3.7.8
# -*- coding: utf-8 -*-
import keyboard
import time
import cv2
import telebot
import random
from pynput.mouse import Controller
from mss import mss
from telebot.types import InputMediaPhoto


bot = telebot.TeleBot('')  # токен бота телеграм
chat_id = ''  # id канала, пример @my_chanel

mouse = Controller()

sct = mss()


class Watch():

    m_position = (0, 0)  # стартовая позиция мишки

    def __init__(self):
        super().__init__()
        self.main()

    def start_script(self):  # функция запуска скрипта
        mouse.position = (500, 500)  # переводит курсор, что-бы было понятно, когда скрипт находится в режиме ожидания
        while True:

            if keyboard.is_pressed('ctrl+alt'):  # комбинация для запуска
                self.main()

    def main(self):
        mouse.position = self.m_position  # переводит курсор по заданным координатам из 22 строки

        while mouse.position == self.m_position:  # проверка, находится ли курсор в заданных координатах

            if keyboard.is_pressed('alt+a'):  # вкл. ожидания
                self.start_script()
            if mouse.position != self.m_position:
                self.catch()

    def catch(self):
        p = 0

        try:
            cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # вкл. камеры
        except:
            cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

        while p < 2:  # количество снимков
            p += 1
            ret, frame = cam.read()  # делаем снимок

            cv2.imwrite('cam.png', frame)  # сохраняем снимок камеры
            sct.shot(output='scr.png')

            photo = open('cam.png', 'rb')  # откр. для чтения в двоичном режиме
            screen = open('scr.png', 'rb')  # сохраняем скриншот экрана

            media = [InputMediaPhoto(photo), InputMediaPhoto(screen)]

            try:
                bot.send_media_group(chat_id, media)  # отправка в телеграм
            except:
                pass

            time.sleep(random.uniform(1, 3))  # задержка от 1 до 3 сек.

        cam.release()  # откл. камеру

        time.sleep(5)
        self.m_position = mouse.position  # переназначим позицию мышки
        return self.main()


if __name__ == '__main__':
    Watch()
