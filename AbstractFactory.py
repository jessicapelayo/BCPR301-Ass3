import matplotlib.pyplot as plt
import numpy as np

class Chart(object): #abstract product
    def __init__(self, labels, values, title):
        self.labels = labels
        self.values = values
        self.title = title
        self.draw()

    def draw(self):
        pass


class PieChart(Chart): #product
    def draw(self):
        total = 0
        for value in self.values:
            total += value
        label_tuple = tuple(self.labels)
        size = self.values
        plt.pie(size, labels = label_tuple, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.title(self.title)
        plt.show()


class ChartCreator(object):
    def __init__(self, chart_type, labels_list, values_list, title):
        self.labels = labels_list
        self.values = values_list
        self.title = title
        self.chart = None
        if chart_type == "pie":
            self.chart = self.make_pie_chart()

    def make_pie_chart(self):
        pass


class ChartConcreteCreator(ChartCreator):
    def make_pie_chart(self):
        return PieChart(self.labels, self.values, self.title)

