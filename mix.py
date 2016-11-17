"""Testing pygal"""
import os
import uuid
from pygal import*
def function():
	"""run this file in cmd and then bar_chart.svg was appeared
	you can test it in browser"""
	import pygal                                                
	bar_chart = pygal.Bar()                                            
	bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
	bar_chart.render_to_file('mix.svg')
	pie_chart = Pie()
	pie_chart.title = 'ประชากรไทย ชาย-หญิง พ.ศ.2557 ( คิดเป็น  %)'
	pie_chart.add('ชาย',48.62)
	pie_chart.add('หญิง',51.38)
	pie_chart.render_to_file('mix2.svg')
function()