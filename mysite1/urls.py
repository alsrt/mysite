from django.conf.urls.defaults import patterns, include, url
from django.views.generic import list_detail
from django.views.generic import date_based
from mysite1.polls.models import Publisher, Book, Author
from mysite1.polls.views import register, profile
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

publisher_info = {
    "queryset" : Publisher.objects.all(),

     }
author_detail_info = {
    "queryset" : Author.objects.all(),
    "template_object_name" : "author",

    }
book_info = {
    "queryset"   : Book.objects.all(),
    "date_field" : "publication_date",
    "template_object_name":"book",
}
urlpatterns = patterns('',
                     (r'^publishers/$', list_detail.object_list, publisher_info),
                     #(r'^publishers/$', list_detail.object_list, publisher_info),
                     (r'^authors/(?P<object_id>\d+)/$', list_detail.object_detail, author_detail_info),
                     (r'^books/$', date_based.archive_index, book_info),
                     (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', date_based.archive_month, book_info),
                     (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})/$', date_based.archive_day, book_info),
)

from django.contrib.auth.views import login, logout

urlpatterns += patterns('',
                       # existing patterns here...
                       (r'^accounts/login/$',  login),
                       (r'^accounts/logout/$', logout),
                       (r'^accounts/register/$', register),
                       (r'^accounts/profile/$', profile),
                                             )

urlpatterns += staticfiles_urlpatterns()
