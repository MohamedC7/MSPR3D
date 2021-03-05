from kivy.core.camera import Camera
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import logging
Logger.setLevel(logging.TRACE)


class CameraClick(BoxLayout):
  def capture(self):
    #Function to capture the images and give them the names according to their captured time and date.
    cam = Camera(resolution=(320, 240))
    print("Captured")




class MainApp(App):
  def build(self):
    return CameraClick()

MainApp().run()
