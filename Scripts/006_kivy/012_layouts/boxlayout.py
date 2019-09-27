"""
Buttons

doc : https://kivy.org/doc/stable/api-kivy.uix.button.html
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class BoxLayoutWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # BoxLayout
        box = BoxLayout(orientation='vertical')
        lbl = Label(text='first')
        btn = Button(text='second')
        box.add_widget(lbl)
        box.add_widget(btn)
        self.add_widget(box)


class BoxLayoutApp(App):
    def build(self):
        return BoxLayoutWindow()


if __name__ == '__main__':
    BoxLayoutApp().run()
