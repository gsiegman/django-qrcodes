from django import template
from pygooglechart import QRChart

register = template.Library()

@register.inclusion_tag("qr_codes/qr_code.html")
def qr_code(data, size=125):
    chart = QRChart(size, size)
    chart.add_data(data)
    chart.set_ec('H', 0)
	
    return {'qr_code': chart.get_url(), 
        'type': 'url'
    }