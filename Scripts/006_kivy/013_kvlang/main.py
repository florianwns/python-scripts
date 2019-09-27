import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class DemoWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_title(self):
        self.ids.title_lbl.text = 'Button clicked'


class DemoApp(App):
    def build(self):
        return DemoWindow()


if __name__ == '__main__':
    DemoApp().run()
