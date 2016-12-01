"""Project 2016: Information Threat"""
import pygal
import csv
from pygal import *
from pygal.style import DarkStyle
import uuid
import os
def main():
    """Project 2016: PSIT OpenData"""
    file = open('D:/project/1.csv')
    data = (csv.reader(file))
    read_list = []
    unread_list = []
    for i in data:
        read_list.append(i[5])
        unread_list.append(i[9])
    line_chart = pygal.Bar()
    line_chart.title = 'Number of population, Show number of read and unread'
    line_chart.x_labels = ['กรุงเทพมหานคร','ภาคกลาง','ภาคเหนือ','ภาคตะวันออกเฉียงเหนือ','ภาคใต้']
    line_chart.add('Read', [int(read_list[8]), int(read_list[24]), int(read_list[41]), int(read_list[56]),   int(read_list[70])])
    line_chart.add('Unread',  [int(unread_list[8]), int(unread_list[24]), int(unread_list[41]), int(unread_list[56]), int(unread_list[70])])
    line_chart.render_to_file('first.svg')
main()
