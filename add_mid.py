"""Project 2016: Information Threat"""
import pygal
import csv
from pygal import *
from pygal.style import DarkStyle
import uuid
import os
def main():
    """bkk"""
    file = open('D:/project/1.csv')
    data = (csv.reader(file))
    listmen_reading_mid = []
    listwomen_reading_mid = []
    listmen_unreading_mid = []
    listwomen_unreading_mid = []
    for i in data:
        listmen_reading_mid.append(i[6])
        listwomen_reading_mid.append(i[7])
        listmen_unreading_mid.append(i[10])
        listwomen_unreading_mid.append(i[11])

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading and unreading , age 6-14 yearsold'
    mid_pie.add('ชาย อ่าน', int(listmen_reading_mid[26]))
    mid_pie.add('หญิง อ่าน', int(listwomen_reading_mid[26]))
    mid_pie.add('ชาย ไม่อ่าน', int(listmen_unreading_mid[26]))
    mid_pie.add('หญิง ไม่อ่าน',int(listwomen_unreading_mid[26]))
    mid_pie.render_to_file('mid6_14.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading and unreading , age 15-24 yearsold'
    mid_pie.add('ชาย อ่าน', int(listmen_reading_mid[27]))
    mid_pie.add('หญิง อ่าน', int(listwomen_reading_mid[27]))
    mid_pie.add('ชาย ไม่อ่าน', int(listmen_unreading_mid[27]))
    mid_pie.add('หญิง ไม่อ่าน',int(listwomen_unreading_mid[27]))
    mid_pie.render_to_file('mid15_24.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading and unreading , age 25-39 yearsold'
    mid_pie.add('ชาย อ่าน', int(listmen_reading_mid[28]))
    mid_pie.add('หญิง อ่าน', int(listwomen_reading_mid[28]))
    mid_pie.add('ชาย ไม่อ่าน', int(listmen_unreading_mid[28]))
    mid_pie.add('หญิง ไม่อ่าน',int(listwomen_unreading_mid[28]))
    mid_pie.render_to_file('mid25_39.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading and unreading , age 40-59 yearsold'
    mid_pie.add('ชาย อ่าน', int(listmen_reading_mid[29]))
    mid_pie.add('หญิง อ่าน', int(listwomen_reading_mid[29]))
    mid_pie.add('ชาย ไม่อ่าน', int(listmen_unreading_mid[29]))
    mid_pie.add('หญิง ไม่อ่าน',int(listwomen_unreading_mid[29]))
    mid_pie.render_to_file('mid40_59.svg')

    mid_pie = Pie()
    mid_pie.title = 'Number of population, reading and unreading , age 60andover yearsold'
    mid_pie.add('ชาย อ่าน', int(listmen_reading_mid[30]))
    mid_pie.add('หญิง อ่าน', int(listwomen_reading_mid[30]))
    mid_pie.add('ชาย ไม่อ่าน', int(listmen_unreading_mid[30]))
    mid_pie.add('หญิง ไม่อ่าน',int(listwomen_unreading_mid[30]))
    mid_pie.render_to_file('mid60.svg')
main()
