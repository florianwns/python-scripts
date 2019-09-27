import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('1.11.1')


class SpacingSizingWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_title(self):
        self.ids.title_lbl.text = 'Button clicked'


class SpacingSizingApp(App):
    def build(self):
        return SpacingSizingWindow()


if __name__ == '__main__':
    SpacingSizingApp().run()
