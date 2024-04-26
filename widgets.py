from kivy.app import App 
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(text='Olá SENAI!')
if _name_ == "_main_":
    MinhaApp().run()

from kivy.app import App 
from kivy.uix.label import Label

from kivy.app import App 
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(text='Olá SENAI!', font_size=100)
if _name_ == "_main_":
    MinhaApp().run()

from kivy.app import App 
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Label(text='Olá SENAI!', font_size=100, font_name='Arial', color=get_color_from_hex('#FF5733'))

if _name_ == "_main_":
    MinhaApp().run()

from kivy.app import App 
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        return Label(
            text='Olá, SENAI!', 
            halign='left', #Alinha o texto a esquerda
            valign='top'   #Alinha o texto no topo 
        )
        
if _name_ == "_main_":
    MinhaApp().run()


class MinhaApp(App):
    def build(self):
        return Label(
            text='Olá, SENAI!', 
            halign='left',   #Alinha o texto a esquerda
            valign='top',     #Alinha o texto no topo 
            size_hint=(None, None), #Desativa o ajuste automático do tamanho
            size=(150,50),   #Define o tamanho do rótulo
            text_size=(150, None)   #Define a largura máxima do texto
        )
        
if __name__ == "__main__":
    MinhaApp().run()


