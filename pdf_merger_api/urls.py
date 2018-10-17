from django.conf.urls import patterns, include, url
from django.contrib import admin
from pdf_merger.views import PdfMergerView
from qr_factory.views import QrGenView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdf_merger_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pdf-merger', PdfMergerView.as_view(), name='pdf_merger'),
    url(r'^qr-gen', QrGenView.as_view(), name='qr_gen'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
