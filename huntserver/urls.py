"""puzzlehunt_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from huntserver import hunt_views, auth_views, info_views, staff_views
from django.contrib.auth import views as base_auth_views
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

urlpatterns = [
    # Auth and Accounts
    url(r'^accounts/create/$', auth_views.create_account, name='create_account'),
    url(r'^login-selection/$', auth_views.login_selection, name='login_selection'),
    url(r'^shib/login$', auth_views.shib_login, name='new_shib_account'),
    url(r'^logout/$', auth_views.account_logout, name='account_logout'),

    # Info Pages
    url(r'^$', info_views.index, name='index'),
    url(r'^hunt/info/$', info_views.current_hunt_info, name='current_hunt_info'),
    url(r'^previous-hunts/$', info_views.previous_hunts, name='previous_hunts'),
    url(r'^resources/$', TemplateView.as_view(template_name="resources.html"), name='resources'),
    url(r'^contact-us/$', TemplateView.as_view(template_name="contact_us.html"), name='contact_us'),
    url(r'^registration/$', info_views.registration, name='registration'),
    url(r'^user-profile/$', info_views.user_profile, name='user_profile'),

    # Hunt Pages
    url(r'^puzzle/(?P<puzzle_id>[0-9a-fA-F]{3})/$', hunt_views.puzzle_view, name='puzzle'),
    url(r'^hunt/(?P<hunt_num>[0-9]+)/$', hunt_views.hunt, name='hunt'),
    url(r'^hunt/current/$', hunt_views.current_hunt, name='current_hunt'),
    url(r'^hunt/(?P<hunt_num>[0-9]+)/prepuzzle/$', hunt_views.hunt_prepuzzle, name='hunt_prepuzzle'),
    url(r'^prepuzzle/(?P<prepuzzle_num>[0-9]+)/$', hunt_views.prepuzzle, name='prepuzzle'),
    url(r'^hunt/current/prepuzzle/$', hunt_views.current_prepuzzle, name='current_prepuzzle'),
    url(r'^chat/$', hunt_views.chat, name='chat'),
    url(r'^objects/$', hunt_views.unlockables, name='unlockables'),
    url(r'^protected/(?P<file_path>.+)$', hunt_views.protected_static, name='protected_static'),

    # Staff pages
    url(r'^staff/', include([
        url(r'^queue/$', staff_views.queue, name='queue'),
        url(r'^queue/(?P<page_num>[0-9]+)/$', staff_views.queue, name='queue_paged'),
        url(r'^progress/$', staff_views.progress, name='progress'),
        url(r'^charts/$', staff_views.charts, name='charts'),
        url(r'^chat/$', staff_views.admin_chat, name='admin_chat'),
        url(r'^control/$', staff_views.control, name='control'),
        url(r'^teams/$', RedirectView.as_view(url='/admin/huntserver/team/', permanent=False)),
        url(r'^puzzles/$', RedirectView.as_view(url='/admin/huntserver/puzzle/', permanent=False)),
        url(r'^emails/$', staff_views.emails, name='emails'),
        url(r'^management/$', staff_views.hunt_management, name='hunt_management'),
        url(r'^info/$', staff_views.hunt_info, name='hunt_info'),
        url(r'^depgraph/$', staff_views.depgraph, name='depgraph'),
    ])),

    url(r'^Shibboleth.sso/Logout', base_auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^Shibboleth.sso/Login', base_auth_views.login),
]
