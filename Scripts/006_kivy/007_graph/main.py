from math import sin
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.app import App

class GraphApp(App):
    def build(self):
        super(GraphApp, self).__init__()
        self.graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
            x_ticks_major=25, y_ticks_major=1,
            y_grid_label=True, x_grid_label=True, padding=5,
            x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        self.graph.add_plot(self.plot)
        return self.graph

if __name__ == '__main__':
    app =  GraphApp()
    try:
        app.run()
    except KeyboardInterrupt:
        app.stop()
