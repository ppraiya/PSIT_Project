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
    listsum_reading = []
    listmen_reading = []
    listwomen_reading = []
    listmen_unreading = []
    listwomen_unreading = []
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

    for i in data:
        listsum_reading.append(i[5])
        listmen_reading.append(i[6])
        listwomen_reading.append(i[7])
        listmen_unreading.append(i[10])
        listwomen_unreading.append(i[11])

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
    bkk_pie.title = 'Number of population, reading, age 6-14 yearsold'
    bkk_pie.add('ชาย', int(listmen_reading[9]))
    bkk_pie.add('หญิง', int(listwomen_reading[9]))
    bkk_pie.render_to_file('bkk.svg')
    bkk_pie_ur = pygal.Pie(inner_radius=.4)
    bkk_pie_ur.title = 'Number of population, unreading, age 6-14 yearsold'
    bkk_pie_ur.add('ชาย', int(listmen_unreading[9]))
    bkk_pie_ur.add('หญิง',int(listwomen_unreading[9]))
    bkk_pie_ur.render_to_file('bkk_ur.svg')

    bkk_pie2 = pygal.Pie(inner_radius=.4)
    bkk_pie2.title = 'Number of population, reading, age 15-24 yearsold'
    bkk_pie2.add('ชาย', int(listmen_reading[10]))
    bkk_pie2.add('หญิง', int(listwomen_reading[10]))
    bkk_pie2.render_to_file('bkk2.svg')
    bkk_pie2 = pygal.Pie(inner_radius=.4)
    bkk_pie2.title = 'Number of population, unreading, age 15-24 yearsold'
    bkk_pie_ur2.add('ชาย', int(listmen_unreading[10]))
    bkk_pie_ur2.add('หญิง',int(listwomen_unreading[10]))
    bkk_pie2.render_to_file('bkk2_ur.svg')

    bkk_pie3 = pygal.Pie(inner_radius=.4)
    bkk_pie3.title = 'Number of population, reading, age 25-39 yearsold'
    bkk_pie3.add('ชาย', int(listmen_reading[11]))
    bkk_pie3.add('หญิง', int(listwomen_reading[11]))
    bkk_pie3.render_to_file('bkk3.svg')
    bkk_pie_ur3 = pygal.Pie(inner_radius=.4)
    bkk_pie_ur3.title = 'Number of population, unreading, age 25-39 yearsold'
    bkk_pie_ur3.add('ชาย', int(listmen_unreading[11]))
    bkk_pie_ur3.add('หญิง',int(listwomen_unreading[11]))
    bkk_pie_ur3.render_to_file('bkk3_ur.svg')

    bkk_pie4 = pygal.Pie(inner_radius=.4)
    bkk_pie4.title = 'Number of population, reading, age 40-59 yearsold'
    bkk_pie4.add('ชาย อ่าน', int(listmen_reading[12]))
    bkk_pie4.add('หญิง อ่าน', int(listwomen_reading[12]))
    bkk_pie4.render_to_file('bkk4.svg')
    bkk_pie_ur4 = pygal.Pie(inner_radius=.4)
    bkk_pie_ur4.title = 'Number of population, unreading, age 40-59 yearsold'
    bkk_pie_ur4.add('ชาย', int(listmen_unreading[12]))
    bkk_pie_ur4.add('หญิง',int(listwomen_unreading[12]))
    bkk_pie_ur4.render_to_file('bkk4_ur.svg')


    bkk_pie5 = pygal.Pie(inner_radius=.4)
    bkk_pie5.title = 'Number of population, reading, age 60 and over yearsold'
    bkk_pie5.add('ชาย', int(listmen_reading[13]))
    bkk_pie5.add('หญิง', int(listwomen_reading[13]))
    bkk_pie5.render_to_file('bkk5.svg')
    bkk_pie_ur5 = pygal.Pie(inner_radius=.4)
    bkk_pie_ur5.title = 'Number of population, unreading, age 60 and over yearsold'
    bkk_pie_ur5.add('ชาย', int(listmen_unreading[13]))
    bkk_pie_ur5.add('หญิง',int(listwomen_unreading[13]))
    bkk_pie_ur5.render_to_file('bkk5_ur.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading, age 6-14 yearsold'
    mid_pie.add('ชาย', int(listmen_reading[26]))
    mid_pie.add('หญิง', int(listwomen_reading[26]))
    mid_pie.render_to_file('mid6_14.svg')
    mid_pie_ur = Pie()
    mid_pie_ur.title = 'Number of population, unreading, age 6-14 yearsold'
    mid_pie_ur.add('ชาย', int(listmen_unreading[26]))
    mid_pie_ur.add('หญิง',int(listwomen_unreading[26]))
    mid_pie_ur.render_to_file('mid6_ur14.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading, age 15-24 yearsold'
    mid_pie.add('ชาย', int(listmen_reading[27]))
    mid_pie.add('หญิง', int(listwomen_reading[27]))
    mid_pie.render_to_file('mid15_24.svg')
    mid_pie_ur = Pie()
    mid_pie_ur.title = 'Number of population, unreading, age 15-24 yearsold'
    mid_pie_ur.add('ชาย', int(listmen_unreading[27]))
    mid_pie_ur.add('หญิง',int(listwomen_unreading[27]))
    mid_pie_ur.render_to_file('mid15_ur24.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading, age 25-39 yearsold'
    mid_pie.add('ชาย', int(listmen_reading[28]))
    mid_pie.add('หญิง', int(listwomen_reading[28]))
    mid_pie.render_to_file('mid25_39.svg')
    mid_pie_ur = Pie()
    mid_pie_ur.title = 'Number of population, unreading, age 25-39 yearsold'
    mid_pie_ur.add('ชาย', int(listmen_unreading[28]))
    mid_pie_ur.add('หญิง',int(listwomen_unreading[28]))
    mid_pie_ur.render_to_file('mid25_ur39.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading, age 40-59 yearsold'
    mid_pie.add('ชาย', int(listmen_reading[29]))
    mid_pie.add('หญิง', int(listwomen_reading[29]))
    mid_pie.render_to_file('mid40_59.svg')
    mid_pie_ur = Pie()
    mid_pie_ur.title = 'Number of population, unreading, age 40-59 yearsold'
    mid_pie_ur.add('ชาย', int(listmen_unreading[29]))
    mid_pie_ur.add('หญิง',int(listwomen_unreading[29]))
    mid_pie_ur.render_to_file('mid40_ur59.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading, age 60andover yearsold'
    mid_pie.add('ชาย', int(listmen_reading[30]))
    mid_pie.add('หญิง', int(listwomen_reading[30]))
    mid_pie.render_to_file('mid60.svg')
    mid_pie_ur = Pie()
    mid_pie_ur.title = 'Number of population, unreading, age 60andover yearsold'
    mid_pie_ur.add('ชาย', int(listmen_unreading[30]))
    mid_pie_ur.add('หญิง',int(listwomen_unreading[30]))
    mid_pie_ur.render_to_file('mid60_ur.svg')

    north_pie = pygal.Pie(inner_radius=.4)
    north_pie.title = 'Number of population, reading, age 6-14 yearsold'
    north_pie.add('ชาย', int(listmen_reading[42]))
    north_pie.add('หญิง', int(listwomen_reading[42]))
    north_pie.render_to_file('north.svg')
    north_pie_ur = pygal.Pie(inner_radius=.4)
    north_pie_ur.title = 'Number of population, unreading, age 6-14 yearsold'
    north_pie_ur.add('ชาย', int(listmen_unreading[42]))
    north_pie_ur.add('หญิง',int(listwomen_unreading[42]))
    north_pie_ur.render_to_file('north_ur.svg')

    north_pie2 = pygal.Pie(inner_radius=.4)
    north_pie2.title = 'Number of population, reading, age 15-24 yearsold'
    north_pie2.add('ชาย', int(listmen_reading[43]))
    north_pie2.add('หญิง', int(listwomen_reading[43]))
    north_pie2.render_to_file('north2.svg')
    north_pie2_ur = pygal.Pie(inner_radius=.4)
    north_pie2_ur.title = 'Number of population, unreading, age 15-24 yearsold'
    north_pie2_ur.add('ชาย', int(listmen_unreading[43]))
    north_pie2_ur.add('หญิง',int(listwomen_unreading[43]))
    north_pie2_ur.render_to_file('north2_ur.svg')

    north_pie3 = pygal.Pie(inner_radius=.4)
    north_pie3.title = 'Number of population, reading, age 25-39 yearsold'
    north_pie3.add('ชาย อ่าน', int(listmen_reading[44]))
    north_pie3.add('หญิง อ่าน', int(listwomen_reading[44]))
    north_pie3.render_to_file('north3.svg')
    north_pie3_ur = pygal.Pie(inner_radius=.4)
    north_pie3_ur.title = 'Number of population, unreading, age 25-39 yearsold'
    north_pie3_ur.add('ชาย', int(listmen_unreading[44]))
    north_pie3_ur.add('หญิง',int(listwomen_unreading[44]))
    north_pie3_ur.render_to_file('north3_ur.svg')

    north_pie4 = pygal.Pie(inner_radius=.4)
    north_pie4.title = 'Number of population, reading, age 40-59 yearsold'
    north_pie4.add('ชาย', int(listmen_reading[45]))
    north_pie4.add('หญิง', int(listwomen_reading[45]))
    north_pie4.render_to_file('north4.svg')
    north_pie4_ur = pygal.Pie(inner_radius=.4)
    north_pie4_ur.title = 'Number of population, unreading, age 40-59 yearsold'
    north_pie4_ur.add('ชาย', int(listmen_unreading[45]))
    north_pie4_ur.add('หญิง',int(listwomen_unreading[45]))
    north_pie4_ur.render_to_file('north4_ur.svg')

    north_pie5 = pygal.Pie(inner_radius=.4)
    north_pie5.title = 'Number of population, reading, age 60 and over yearsold'
    north_pie5.add('ชาย', int(listmen_reading[46]))
    north_pie5.add('หญิง', int(listwomen_reading[46]))
    north_pie5.render_to_file('north5.svg')
    north_pie5_ur = pygal.Pie(inner_radius=.4)
    north_pie5_ur.title = 'Number of population, unreading, age 60 and over yearsold'
    north_pie5_ur.add('ชาย', int(listmen_unreading[46]))
    north_pie5_ur.add('หญิง',int(listwomen_unreading[46]))
    north_pie5_ur.render_to_file('north5_ur.svg')

    north_e_pie = pygal.Pie(inner_radius=.4)
    north_e_pie.title = 'Number of population, reading, age 6-14 yearsold'
    north_e_pie.add('ชาย', int(listmen_reading[57]))
    north_e_pie.add('หญิง', int(listwomen_reading[57]))
    north_e_pie.render_to_file('north_e.svg')
    north_e_pie_ur = pygal.Pie(inner_radius=.4)
    north_e_pie_ur.title = 'Number of population, unreading, age 6-14 yearsold'
    north_e_pie_ur.add('ชาย', int(listmen_unreading[57]))
    north_e_pie_ur.add('หญิง',int(listwomen_unreading[57]))
    north_e_pie_ur.render_to_file('north_e_ur.svg')

    north_e_pie2 = pygal.Pie(inner_radius=.4)
    north_e_pie2.title = 'Number of population, reading, age 15-24 yearsold'
    north_e_pie2.add('ชาย', int(listmen_reading[58]))
    north_e_pie2.add('หญิง', int(listwomen_reading[58]))
    north_e_pie2.render_to_file('north_e2.svg')
    north_e_pie2_ur = pygal.Pie(inner_radius=.4)
    north_e_pie2_ur.title = 'Number of population, unreading, age 15-24 yearsold'
    north_e_pie2_ur.add('ชาย', int(listmen_unreading[58]))
    north_e_pie2_ur.add('หญิง',int(listwomen_unreading[58]))
    north_e_pie2_ur.render_to_file('north_e2_ur.svg')

    north_e_pie3 = pygal.Pie(inner_radius=.4)
    north_e_pie3.title = 'Number of population, reading, age 25-39 yearsold'
    north_e_pie3.add('ชาย', int(listmen_reading[59]))
    north_e_pie3.add('หญิง', int(listwomen_reading[59]))
    north_e_pie3.render_to_file('north_e3.svg')
    north_e_pie3_ur = pygal.Pie(inner_radius=.4)
    north_e_pie3_ur.title = 'Number of population, unreading, age 25-39 yearsold'
    north_e_pie3_ur.add('ชาย', int(listmen_unreading[59]))
    north_e_pie3_ur.add('หญิง',int(listwomen_unreading[59]))
    north_e_pie3_ur.render_to_file('north_e3_ur.svg')

    north_e_pie4 = pygal.Pie(inner_radius=.4)
    north_e_pie4.title = 'Number of population, reading, age 40-59 yearsold'
    north_e_pie4.add('ชาย', int(listmen_reading[60]))
    north_e_pie4.add('หญิง', int(listwomen_reading[60]))
    north_e_pie4.render_to_file('north_e4.svg')
    north_e_pie4_ur = pygal.Pie(inner_radius=.4)
    north_e_pie4_ur.title = 'Number of population, unreading, age 40-59 yearsold'
    north_e_pie4_ur.add('ชาย', int(listmen_unreading[60]))
    north_e_pie4_ur.add('หญิง',int(listwomen_unreading[60]))
    north_e_pie4_ur.render_to_file('north_e4_ur.svg')


    north_e_pie5 = pygal.Pie(inner_radius=.4)
    north_e_pie5.title = 'Number of population, reading, age 60 and over yearsold'
    north_e_pie5.add('ชาย', int(listmen_reading[61]))
    north_e_pie5.add('หญิง', int(listwomen_reading[61]))
    north_e_pie5.render_to_file('north_e5.svg')
    north_e_pie5_ur = pygal.Pie(inner_radius=.4)
    north_e_pie5_ur.title = 'Number of population, unreading, age 60 and over yearsold'
    north_e_pie5_ur.add('ชาย', int(listmen_unreading[61]))
    north_e_pie5_ur.add('หญิง',int(listwomen_unreading[61]))
    north_e_pie5_ur.render_to_file('north_e5_ur.svg')

    south_pie = pygal.Pie(inner_radius=.4)
    south_pie.title = 'Number of population, reading, age 6-14 yearsold'
    south_pie.add('ชาย', int(listmen_reading[71]))
    south_pie.add('หญิง', int(listwomen_reading[71]))
    south_pie.render_to_file('south.svg')
    south_pie_ur = pygal.Pie(inner_radius=.4)
    south_pie_ur.title = 'Number of population, unreading, age 6-14 yearsold'
    south_pie_ur.add('ชาย', int(listmen_unreading[71]))
    south_pie_ur.add('หญิง',int(listwomen_unreading[71]))
    south_pie_ur.render_to_file('south_ur.svg')

    south_pie2 = pygal.Pie(inner_radius=.4)
    south_pie2.title = 'Number of population, reading, age 15-24 yearsold'
    south_pie2.add('ชาย', int(listmen_reading[72]))
    south_pie2.add('หญิง', int(listwomen_reading[72]))
    south_pie2.render_to_file('south2.svg')
    south_pie2_ur = pygal.Pie(inner_radius=.4)
    south_pie2_ur.title = 'Number of population, unreading, age 15-24 yearsold'
    south_pie2_ur.add('ชาย', int(listmen_unreading[72]))
    south_pie2_ur.add('หญิง',int(listwomen_unreading[72]))
    south_pie2_ur.render_to_file('south2_ur.svg')

    south_pie3 = pygal.Pie(inner_radius=.4)
    south_pie3.title = 'Number of population, reading, age 25-39 yearsold'
    south_pie3.add('ชาย', int(listmen_reading[73]))
    south_pie3.add('หญิง', int(listwomen_reading[73]))
    south_pie3.render_to_file('south3.svg')
    south_pie3_ur = pygal.Pie(inner_radius=.4)
    south_pie3_ur.title = 'Number of population, unreading, age 25-39 yearsold'
    south_pie3_ur.add('ชาย', int(listmen_unreading[73]))
    south_pie3_ur.add('หญิง',int(listwomen_unreading[73]))
    south_pie3_ur.render_to_file('south3_ur.svg')

    south_pie4 = pygal.Pie(inner_radius=.4)
    south_pie4.title = 'Number of population, reading, age 40-59 yearsold'
    south_pie4.add('ชาย', int(listmen_reading[74]))
    south_pie4.add('หญิง', int(listwomen_reading[74]))
    south_pie4.render_to_file('south4.svg')
    south_pie4_ur = pygal.Pie(inner_radius=.4)
    south_pie4_ur.title = 'Number of population, unreading, age 40-59 yearsold'
    south_pie4_ur.add('ชาย', int(listmen_unreading[74]))
    south_pie4_ur.add('หญิง',int(listwomen_unreading[74]))
    south_pie4_ur.render_to_file('south4_ur.svg')

    south_pie5 = pygal.Pie(inner_radius=.4)
    south_pie5.title = 'Number of population, reading, age 60 and over yearsold'
    south_pie5.add('ชาย', int(listmen_reading[75]))
    south_pie5.add('หญิง', int(listwomen_reading[75]))
    south_pie5.render_to_file('south5.svg')
    south_pie5_ur = pygal.Pie(inner_radius=.4)
    south_pie5_ur.title = 'Number of population, unreading, age 60 and over yearsold'
    south_pie5_ur.add('ชาย', int(listmen_unreading[75]))
    south_pie5_ur.add('หญิง',int(listwomen_unreading[75]))
    south_pie5_ur.render_to_file('south5_ur.svg')

main()

