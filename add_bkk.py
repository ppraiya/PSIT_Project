"""Project 2016: Information Threat"""
import pygal
import csv
from pygal import *
from pygal.style import DarkStyle
import uuid
import os
def main():
    """test"""
    file = open('D:/project/1.csv')
    data = (csv.reader(file))
    listsum_reading = []
    listmen_reading_bkk = []
    listwomen_reading_bkk = []
    listmen_unreading_bkk = []
    listwomen_unreading_bkk = []
    for i in data:
        listsum_reading.append(i[5])
        listmen_reading_bkk.append(i[6])
        listwomen_reading_bkk.append(i[7])
        listmen_unreading_bkk.append(i[10])
        listwomen_unreading_bkk.append(i[11])

    line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DarkStyle)
    line_chart = pygal.Bar()
    line_chart.title = ' Number of population, aged 6 years and over by reading'
    line_chart.x_labels = ['กรุงเทพมหานคร','ภาคกลาง','ภาคเหนือ','ภาคตะวันออกเฉียงเหนือ','ภาคใต้']
    line_chart.add('6-14 ปี', [int(listsum_reading[9]), int(listsum_reading[26]), int(listsum_reading[42]), int(listsum_reading[57]),   int(listsum_reading[71])])
    line_chart.add('15-24 ปี',  [int(listsum_reading[10]), int(listsum_reading[27]), int(listsum_reading[43]), int(listsum_reading[58]), int(listsum_reading[72])])
    line_chart.add('25-39 ปี',  [int(listsum_reading[11]), int(listsum_reading[28]), int(listsum_reading[44]), int(listsum_reading[59]), int(listsum_reading[73])])
    line_chart.add('40-59 ปี',  [int(listsum_reading[12]), int(listsum_reading[29]), int(listsum_reading[45]), int(listsum_reading[60]), int(listsum_reading[74])])
    line_chart.add('60andover', [int(listsum_reading[13]), int(listsum_reading[30]), int(listsum_reading[46]), int(listsum_reading[61]), int(listsum_reading[75])])
    line_chart.render_to_file('bar_area_1.svg')

    bkk_pie = pygal.Pie(inner_radius=.4)
    bkk_pie.title = 'Number of population, reading and unreading , age 6-14 yearsold'
    bkk_pie.add('ชาย อ่าน', int(listmen_reading_bkk[9]))
    bkk_pie.add('หญิง อ่าน', int(listwomen_reading_bkk[9]))
    bkk_pie.add('ชาย ไม่อ่าน', int(listmen_unreading_bkk[9]))
    bkk_pie.add('หญิง ไม่อ่าน',int(listwomen_unreading_bkk[9]))
    bkk_pie.render_to_file('bkk.svg')


main()
