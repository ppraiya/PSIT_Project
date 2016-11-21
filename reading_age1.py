"""Testing pygal"""
import os
import uuid
from pygal import*
def function():
	"""run this file in cmd and then bar_chart.svg was appeared
	you can test it in browser"""
	import pygal                                                
	pie_chart = Pie()
	pie_chart.title = 'จำนวนประชากรที่อ่านหนังสือ แบ่งตามช่วงอายุ ปีพ.ศ.2558' #Table15
	pie_chart.add('อายุ 6-14',6694654 )
	pie_chart.add('อายุ 15-24',8581570)
	pie_chart.add('อายุ 25-39',12571923)
	pie_chart.add('อายุ 40-59',15077111)
	pie_chart.add('อายุ 60+',5483310)
	pie_chart.render_to_file('age_read.svg')
function()
