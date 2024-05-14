from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.expression = ""
        
        layout = BoxLayout(orientation='vertical')
        
        # Caixa de entrada para exibir a expressão e o resultado
        self.text_input = TextInput(font_size=32, size_hint_y=None, height=100)
        layout.add_widget(self.text_input)
        
        # Adicionando botões
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=32)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        
        return layout
    
    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Erro"
        elif instance.text == 'C':
            self.expression = ""
        else:
            self.expression += instance.text
        self.text_input.text = self.expression


if __name__ == '__main__':
    CalculatorApp().run()
