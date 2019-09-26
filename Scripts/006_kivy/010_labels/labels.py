from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase
import os

path = os.path.dirname(__file__)
fonts_path = os.path.join(path, f"fonts{os.sep}")
LabelBase.register(name='DejaVuSans', fn_regular=fonts_path + 'DejaVuSans.ttf')
LabelBase.register(name='Icons', fn_regular=fonts_path + 'Icons.ttf')

class LabelsWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # simple label
        label1 = Label()
        label1.text = 'Hello Florian, \nWhat\'s up ?'
        label1.font_size = 42
        label1.bold = True
        label1.underline = True
        label1.halign = 'center'
        label1.color = (0, 1, 0, 1)
        self.add_widget(label1)

        # markup text
        label2 = Label()
        label2.text = '[size=30]I try to [u]code[/u] a [b]kivy app[/b] ![/size]'
        label2.halign = 'center'
        label2.markup = True
        label2.color = (0, 0, 1, 1)
        self.add_widget(label2)

        # unicode text
        label3 = Label()
        label3.text = 'هل يمكن تأجير عربات للأطفال؟'
        label3.font_name = 'DejaVuSans'
        self.add_widget(label3)

        # Icons text
        label4 = Label()
        label4.font_size = 60
        label4.text = '\uF00A'
        label4.font_name = 'Icons'
        self.add_widget(label4)


class LabelsApp(App):
    def build(self):
        return LabelsWindow()


if __name__ == '__main__':
    LabelsApp().run()
