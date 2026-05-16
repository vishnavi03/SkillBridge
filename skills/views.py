from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Skill, Resource
from requests.models import ServiceRequest


# 💡 SKILLS LIST
def skill_list(request):

    skills = Skill.objects.all()

    query = request.GET.get('q')

    category = request.GET.get('category')

    # SEARCH
    if query:

        skills = skills.filter(

            Q(title__icontains=query) |

            Q(description__icontains=query)

        )

    # FILTER
    if category and category != 'all':

        skills = skills.filter(
            category__iexact=category
        )

    return render(
        request,
        'skills/skill_list.html',
        {
            'skills': skills
        }
    )


# 📄 SKILL DETAIL
def skill_detail(request, skill_id):

    skill = get_object_or_404(
        Skill,
        id=skill_id
    )

    approved = False

    if request.user.is_authenticated:

        approved = ServiceRequest.objects.filter(

            sender=request.user,

            skill=skill,

            status='accepted'

        ).exists()

    return render(
        request,
        'skills/skill_detail.html',
        {
            'skill': skill,
            'approved': approved
        }
    )


# ➕ ADD SKILL
@login_required
def add_skill(request):

    if request.method == 'POST':

        Skill.objects.create(

            user=request.user,

            title=request.POST.get('title'),

            description=request.POST.get(
                'description'
            ),

            category=request.POST.get(
                'category'
            )

        )

        return redirect('/skills/')

    return render(
        request,
        'skills/add_skill.html'
    )


# ✏️ EDIT SKILL
@login_required
def edit_skill(request, skill_id):

    skill = get_object_or_404(
        Skill,
        id=skill_id
    )

    if request.user != skill.user and not request.user.is_staff:

        return redirect('/skills/')

    if request.method == 'POST':

        skill.title = request.POST.get(
            'title'
        )

        skill.description = request.POST.get(
            'description'
        )

        skill.category = request.POST.get(
            'category'
        )

        skill.save()

        return redirect(
            f'/skills/{skill.id}/'
        )

    return render(
        request,
        'skills/edit_skill.html',
        {
            'skill': skill
        }
    )


# 📂 ADD RESOURCE
@login_required
def add_resource(request, skill_id):

    skill = Skill.objects.get(id=skill_id)

    if request.user != skill.user:

        return redirect('/skills/')

    if request.method == 'POST':

        Resource.objects.create(

            skill=skill,

            title=request.POST.get('title'),

            resource_type=request.POST.get(
                'resource_type'
            ),

            link=request.POST.get('link'),

            file=request.FILES.get('file')

        )

        return redirect(
            f'/skills/{skill.id}/'
        )

    return render(
        request,
        'skills/add_resource.html',
        {
            'skill': skill
        }
    )


# 🗑 DELETE RESOURCE
@login_required
def delete_resource(request, resource_id):

    resource = get_object_or_404(
        Resource,
        id=resource_id
    )

    skill = resource.skill

    # owner or admin only
    if request.user != skill.user and not request.user.is_staff:

        return redirect('/skills/')

    if request.method == 'POST':

        resource.delete()

        return redirect(
            f'/skills/{skill.id}/'
        )

    return render(
        request,
        'skills/delete_resource.html',
        {
            'resource': resource
        }
    )


# 🗑 DELETE SKILL
@login_required
def delete_skill(request, skill_id):

    skill = get_object_or_404(
        Skill,
        id=skill_id
    )

    if request.user != skill.user and not request.user.is_staff:

        return redirect('/skills/')

    if request.method == 'POST':

        skill.delete()

        return redirect('/skills/')

    return render(
        request,
        'skills/delete_skill.html',
        {
            'skill': skill
        }
    )