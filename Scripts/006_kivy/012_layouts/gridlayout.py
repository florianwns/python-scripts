"""
Buttons

doc : https://kivy.org/doc/stable/api-kivy.uix.button.html
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class GridLayoutWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # GridLayout
        grid = GridLayout(rows=2)
        for x in range(5):
            grid.add_widget(Button(text="Button" + str(x)))

        self.add_widget(grid)


class GridLayoutApp(App):
    def build(self):
        return GridLayoutWindow()


if __name__ == '__main__':
    GridLayoutApp().run()
