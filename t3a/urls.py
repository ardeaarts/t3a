from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^team/?$', TemplateView.as_view(template_name="team.html"), name='team'),
    url(r'^music/?$', TemplateView.as_view(template_name="music.html"), name='music'),
    url(r'^donate/?$', TemplateView.as_view(template_name="donate.html"), name='donate'),
    url(r'^newsletter/?$', TemplateView.as_view(template_name="newsletter.html"), name='newsletter'),
    url(r'^contact/?$', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^humans.txt$', TemplateView.as_view(template_name="humans.txt"), name='humans'),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt"), name='robots'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )