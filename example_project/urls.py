from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^example_project/', include('example_project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	url(r'^$', 
	 	'django.views.generic.simple.direct_to_template',
	 	{'template': 'qr_codes/index.html', 
	 	    'extra_context': {'hello': 'Hello World!'}
	 	},
	 	name='example_project_index',
	)
)
