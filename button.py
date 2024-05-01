from kivy.app import App
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        return Button(text='Clique Aqui')

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        return Button(text='Clique Aqui', font_size=50)

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Button(text='Clique Aqui', background_color=get_color_from_hex('#3498db'))

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.button import Button

def botao_pressionado(instance):
    print("Botão pressionado!")

class MinhaApp(App):
    def build(self):
        btn = Button(text='Clique Aqui')
        btn.bind(on_press=botao_pressionado)
        return btn

if __name__ == "__main__":
    MinhaApp().run()

        
from kivy.app import App
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        return Button(text='Clique Aqui', size_hint=(0.5, 0.2))
    #Botão ocupará metade da largura e 20% da altura do layout pai

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.checkbox import Checkbox

class MinhaApp(App):
    def build(self):
        return Checkbox(active=False)

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        return Image(source='/Users/usuario/OneDrive/Imagens/2d402af5293a89474558184ee7977bc6.jpg')

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):

        return AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png')

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.slider import Slider

class MinhaApp(App):
    def build(self):
        return Slider(min=0, max=100, value=50)

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label


class MinhaApp(App):
    def build(self):
        #Layout principal
        layout = BoxLayout(orientation='vertical', padding=20)

        #Slider 
        slider = Slider(min=0, max=100, value=50, step=1)
        #Definindo step=1 para prmitir apenas valores inteiros
        slider.bind(value=self.atualizar_label)

        #Label para mostrar o valor do slider
        self.label = Label(text="Valor do Slider: {}".format(int(slider.value)))
        #Exibir apenas o valor inteiro 
        
        #Adicionando os widgets ao layout
        layout.add_widget(slider)
        layout.add_widget(self.label)

        return layout

    def atualizar_label(self,instance,valor):
        #Atualizar o texto do label com o valor inteiro atual do slider
        self.label.text = "Valor do Slider: {}".format(int(valor))

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.progressbar import ProgressBar 

class MinhaApp(App):
    def build(self):
        return ProgressBar(value=50)

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.textinput import TextInput

class MinhaApp(App):
    def build(self):
        return TextInput(text='Digite aqui')

if __name__ == "__main__":
    MinhaApp().run()


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MinhaApp(App):
    def build(self):
        #Layout principal
        layout_principal = BoxLayout(orientation='vertical')

        #widget de entrada para o nome do usuário
        self.input_nome = TextInput(hint_text='Digite seu nome')
        layout_principal.add_widget(self.input_nome)

        #Botão para enviar o nome e exibir a mensagem
        botao_enviar = Button(text='Enviar', on_press=self.exibir_mensagem)
        layout_principal.add_widget(botao_enviar)

        #Label para exibir a mensagem 
        self.label_mensagem = Label()
        layout_principal.add_widget(self.label_mensagem)

        return layout_principal

    def exibir_mensagem(self, instance):
        nome_usuario = self.input_nome.text
        mensagem = f'Olá {nome_usuario}, você está avançando no Kivy! Parabéns SESIANO!'
        self.label_mensagem.text = mensagem 

if __name__ == "__main__":
    MinhaApp().run()