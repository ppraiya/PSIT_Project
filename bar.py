"""bar style"""
import pygal
def function():
	"""bar graph"""
	line_chart = pygal.Bar()
	line_chart.title = 'Browser usage evolution (in %)'
	line_chart.x_labels = ['กรุงเทพมหานคร','ภาคกลาง','ภาคตะวันออกเฉียงเหนือ','ภาคเหนือ','ภาคใต้']
	line_chart.add('ชาย', [3669631, 7015293, 6150197, 4025286, 3063481])
	line_chart.add('หญิง',  [3843461, 6930728, 6518678, 3976164, 3215648])
	line_chart.render_to_file('bar_test2.svg')
function()
