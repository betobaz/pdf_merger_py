from django.conf.urls import patterns, include, url
from django.contrib import admin
from pdf_merger.views import PdfMergerView 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdf_merger_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pdf-merger', PdfMergerView.as_view(), name='pdf_merger'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
