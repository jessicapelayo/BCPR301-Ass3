import matplotlib.pyplot as plt
import numpy as np
import random

class Chart(object): #abstract product
    def __init__(self, labels, values, title):
        self.labels = labels
        self.values = values
        self.title = title
        self.chart_specific_operations()
        self.draw()

    def chart_specific_operations(self):
        pass

    def draw(self):
        plt.title(self.title)
        plt.show()


class PieChart(Chart): #product
    def chart_specific_operations(self):
        total = 0
        for value in self.values:
            total += value
        label_tuple = tuple(self.labels)
        size = self.values
        plt.pie(size, labels = label_tuple, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')


class ScatterChart(Chart): #product
    def chart_specific_operations(self):
        plt.scatter(range(len(self.values)), self.values)
        plt.ylabel(self.labels[0])


class BarGroupedChart(Chart): #product
    def chart_specific_operations(self):
        sub_groups = len(self.labels[1])
        index = np.arange(sub_groups)
        bar_width = 0.25
        i = 0
        colour = ['b', 'r', 'g', 'k', 'm']
        temp = index
        while i < len(self.labels[0]):
            plt.bar(temp, self.values[i], bar_width, color=colour[i], label=self.labels[0][i])
            i += 1
            temp = index + bar_width
        plt.xlabel(self.labels[2][0])
        plt.ylabel(self.labels[2][1])
        a_tuple = tuple(self.labels[1])
        plt.xticks(index + bar_width, a_tuple)
        plt.legend()

class ChartCreator(object):
    def __init__(self, chart_type, labels_list, values_list, title):
        self.labels = labels_list
        self.values = values_list
        self.title = title
        self.chart = None
        if chart_type == "pie":
            self.chart = self.make_pie_chart()
        if chart_type == "scatter":
            self.chart = self.make_scatter_chart()
        if chart_type == "bargrouped":
            self.chart = self.make_bargrouped_chart()

    def make_pie_chart(self):
        pass

    def make_scatter_chart(self):
        pass

    def make_bargrouped_chart(self):
        pass


class ChartConcreteCreator(ChartCreator):
    def make_pie_chart(self):
        return PieChart(self.labels, self.values, self.title)

    def make_scatter_chart(self):
        return ScatterChart(self.labels, self.values, self.title)

    def make_bargrouped_chart(self):
        return BarGroupedChart(self.labels, self.values, self.title)