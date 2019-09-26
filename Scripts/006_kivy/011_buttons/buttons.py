"""
Buttons

doc : https://kivy.org/doc/stable/api-kivy.uix.button.html
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial


class ButtonsWindow(BoxLayout):
    btn1 = Button()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 20

        self.btn1.text = 'Click Me'
        self.btn1.color = (1, 0, 1, 1)
        self.btn1.background_color = (0, 1, 1, 1)
        self.btn1.background_normal = ''
        self.btn1.on_release = partial(self.update_text, "Hello World !!")

        btn2 = Button(text='Click Me Again')
        btn2.bind(on_press=partial(self.update_text, "..."))
        btn2.bind(on_release=partial(self.update_text, "Click Me"))

        self.add_widget(self.btn1)
        self.add_widget(btn2)

    def update_text(self, *args, **kwargs):
        self.btn1.text = args[0]


class ButtonsApp(App):
    def build(self):
        return ButtonsWindow()


if __name__ == '__main__':
    ButtonsApp().run()
