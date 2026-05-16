from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.skill_list,
        name='skill_list'
    ),

    path(
        'add/',
        views.add_skill,
        name='add_skill'
    ),

    # 📄 DETAIL
    path(
        '<int:skill_id>/',
        views.skill_detail,
        name='skill_detail'
    ),

    # ✏️ EDIT
    path(
        'edit/<int:skill_id>/',
        views.edit_skill,
        name='edit_skill'
    ),

    # 📂 ADD RESOURCE
    path(
        'resource/add/<int:skill_id>/',
        views.add_resource,
        name='add_resource'
    ),

    # 🗑 DELETE RESOURCE
    path(
        'resource/delete/<int:resource_id>/',
        views.delete_resource,
        name='delete_resource'
    ),

    # 🗑 DELETE SKILL
    path(
        'delete/<int:skill_id>/',
        views.delete_skill,
        name='delete_skill'
    ),

]