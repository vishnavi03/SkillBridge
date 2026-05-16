from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.received_requests,
        name='requests'
    ),

    path(
        'send/<int:skill_id>/',
        views.send_request,
        name='send_request'
    ),

    path(
        'accept/<int:request_id>/',
        views.accept_request,
        name='accept_request'
    ),

    path(
        'reject/<int:request_id>/',
        views.reject_request,
        name='reject_request'
    ),

    path(
        'review/<int:skill_id>/',
        views.add_review,
        name='add_review'
    ),

]