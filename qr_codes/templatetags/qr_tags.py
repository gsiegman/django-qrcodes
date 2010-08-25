from django import template
from pygooglechart import QRChart

register = template.Library()

@register.inclusion_tag("qr_codes/qr_code.html")
def qr_code(data, size=125, output='url'):
	chart = QRChart(size, size)
	chart.add_data(data)
	chart.set_ec('H', 0)
	
	if output == 'url':
		return chart.get_url()
	elif output == 'image':
		import uuid
		return chart.download(uuid.uuid4 + '.png')
	else:
		raise ValueError("output must be either 'url' or 'image'")
