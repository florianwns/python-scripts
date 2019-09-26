"""
Buttons

doc : https://kivy.org/doc/stable/api-kivy.uix.button.html
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class ButtonsWindow(BoxLayout):
    btn = Button()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 20

        self.btn.text = 'Click Me'
        self.btn.color = (1, 0, 1, 1)
        self.btn.background_color = (0, 1, 1, 1)
        self.btn.background_normal = ''
        self.btn.on_release = self.hello_world
        self.add_widget(self.btn)

    def hello_world(self):
        self.btn.text = "Hello World !!"


class ButtonsApp(App):
    def build(self):
        return ButtonsWindow();


if __name__ == '__main__':
    ButtonsApp().run()
