import json
from exercise35 import month_counter
from bokeh.plotting import figure, show, output_file


# This will plot out the infomation from Exercise 34 about birthdays.
# You can use exercise 34 to add and modify the plots
def main():
	data = month_counter()
	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Sep", "Oct", "Nov", "Dec"]
	# month_data = [val for val in data]
	count = [data[months[x]] if months[x] in data else 0 for x in range(len(months))]

	# sorting the months
	output_file("plot.html")
	p = figure(x_range=months, plot_height=400, title="Birthday Counts")
	p.vbar(x=months, top=count, width=0.9)
	p.xgrid.grid_line_color = None
	p.y_range.start = 0

	show(p)

if __name__ == '__main__':
	main()