__author__ = 'ismailsunni'
from django.conf.urls import patterns, url
from geosafe.views.analysis import (
    AnalysisListView,
    AnalysisCreateView,
    AnalysisDetailView,
    impact_function_filter,
    layer_tiles)

urlpatterns = patterns(
    '',
    url(
        r'^geosafe/analysis/create/$',
        AnalysisCreateView.as_view(),
        name='analysis-create'
    ),
    url(
        r'^geosafe/analysis/$',
        AnalysisListView.as_view(),
        name='analysis-list'
    ),
    url(
        r'^geosafe/analysis/impact-function-filter$',
        impact_function_filter,
        name='impact-function-filter'
    ),
    url(
        r'^geosafe/analysis/(?P<pk>\d+)$',
        AnalysisDetailView.as_view(),
        name='analysis-detail'
    ),
    url(
        r'^geosafe/analysis/layer-tiles$',
        layer_tiles,
        name='layer-tiles'
    ),
)