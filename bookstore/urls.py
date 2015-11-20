from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'bookstore.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )



urlpatterns = [
    # url(r'^', include(router.urls)), # for rest-api

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^about/', 'bookstore.views.about', name='about'),
    url(r'^contact/', 'newsletter.views.contact', name='contact'),
    url(r'^library/', 'book_library.views.library', name="library"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
