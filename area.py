"""bar style"""
import pygal
from pygal.style import DarkStyle
def function():
	"""bar graph"""
	line_chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DarkStyle)
	line_chart = pygal.Bar()
	line_chart.title = ' Number of population, aged 6 years and over by reading'
	line_chart.x_labels = ['กรุงเทพมหานคร','ภาคกลาง','ภาคเหนือ','ภาคตะวันออกเฉียงเหนือ','ภาคใต้']
	line_chart.add('6-14', [551978, 1667393, 1199783, 2244720,   1030780])
	line_chart.add('15-24',  [1090674, 2312874, 1471375, 2518463, 1188184])
	line_chart.add('25-39',      [2608210, 4292879, 1666781, 2291218, 1712855])
	line_chart.add('40-59',  [2479636, 4334579, 2604361 , 3907339, 1751197])
	line_chart.add('60andover', [782593, 1338296, 1059171, 1707135, 596114])
	line_chart.render_to_file('bar_area.svg')
function()
