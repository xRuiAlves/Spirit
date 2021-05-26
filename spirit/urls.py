# -*- coding: utf-8 -*-

from django.conf.urls import include, re_path

from django_cloud_deployer import runInPaaS, runInFaaS

import spirit.topic.views
import spirit.admin.urls
import spirit.user.urls
import spirit.search.urls
import spirit.category.urls
import spirit.topic.urls
import spirit.comment.urls


app_name = 'spirit'
urlpatterns = [
    runInFaaS(re_path(r'^$', spirit.topic.views.index_active, name='index')),
    runInFaaS(re_path(r'^st/admin/', include(spirit.admin.urls))),
    runInPaaS(re_path(r'^user/', include(spirit.user.urls))),
    runInFaaS(re_path(r'^search/', include(spirit.search.urls))),
    runInFaaS(re_path(r'^category/', include(spirit.category.urls))),
    runInPaaS(re_path(r'^topic/', include(spirit.topic.urls))),
    runInPaaS(re_path(r'^comment/', include(spirit.comment.urls))),
]
