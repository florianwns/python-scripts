from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties  import NumericProperty

class WidgetContainer(GridLayout):
    def __init__(self, **kwargs):
        super(WidgetContainer, self).__init__(**kwargs)
        self.cols = 1
        self.freqControl = Slider(min=0, max =100)
        self.add_widget(self.freqControl)
        self.freqValue = Label(text='0')
        self.add_widget(self.freqValue)
        self.freqControl.bind(value=self.on_value)

    def on_value(self, instance, brightness):
        self.freqValue.text = "%d" % brightness


class SliderExample(App):
    def build(self):
        widgetContainer = WidgetContainer()
        return widgetContainer

if __name__ == '__main__':
    SliderExample().run()
