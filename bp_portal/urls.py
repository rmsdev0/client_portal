from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bp_portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #admin/auth views ***************
    url(r'^$', 'bp_portal.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'bp_portal.views.home'),
    url(r'^accounts/login/$', 'bp_portal.views.login'),
    url(r'^accounts/auth/$', 'bp_portal.views.auth_view'),
    url(r'^accounts/logout/$', 'bp_portal.views.logout'),
    #url(r'^accounts/loggedin/$', 'bp_portal.views.loggedin'),
    url(r'^accounts/invalid/$', 'bp_portal.views.invalid_login'),
    #begin live demo ****************
    url(r'^demo/$', 'dashboard.views.db_test'),
    #productions dashboard views ****************
    url(r'^dashboard/$', 'dashboard.views.prod_dashboard'),
    url(r'^dashboard-custom/$', 'dashboard.views.prod_dashboard_custom'),
    url(r'^inbox/$', 'dashboard.views.inbox'),
    url(r'^listing/$', 'dashboard.views.crm_listing'),
    url(r'^call-history/$', 'dashboard.views.call_history'),
    url(r'^settings/$', 'dashboard.views.settings'),
    url(r'^api-form-handler/$', 'dashboard.views.api_form_handler'),
    url(r'^ph-search-handler/$', 'dashboard.views.call_history_search'),
    url(r'^hourly-stats/$', 'dashboard.views.hourly_data'),
    url(r'^hourly-stats-custom/$', 'dashboard.views.hourly_data_custom'),
    url(r'^test/$', 'dashboard.views.test'),

)
