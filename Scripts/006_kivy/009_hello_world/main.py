from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class HelloWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Hello World'))


class HelloApp(App):
    def build(self):
        return HelloWindow();


if __name__ == '__main__':
    HelloApp().run()
