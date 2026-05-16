from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ServiceRequest, Review
from skills.models import Skill


# ➕ Send request
@login_required
def send_request(request, skill_id):

    skill = get_object_or_404(Skill, id=skill_id)

    already_exists = ServiceRequest.objects.filter(
        sender=request.user,
        skill=skill
    ).exists()

    if already_exists:

        messages.warning(request,
                         "Request already sent!")

    else:

        ServiceRequest.objects.create(
            sender=request.user,
            receiver=skill.user,
            skill=skill
        )

        messages.success(request,
                         "Request sent successfully!")

    return redirect('/skills/')


# 📥 View requests
@login_required
def received_requests(request):

    requests = ServiceRequest.objects.filter(
        receiver=request.user
    )

    return render(
        request,
        'requests/received_requests.html',
        {'requests': requests}
    )


# ✅ Accept request
@login_required
def accept_request(request, request_id):

    req = ServiceRequest.objects.get(id=request_id)

    req.status = 'accepted'
    req.save()

    return redirect('/requests/')


# ❌ Reject request
@login_required
def reject_request(request, request_id):

    req = ServiceRequest.objects.get(id=request_id)

    req.status = 'rejected'
    req.save()

    return redirect('/requests/')


# ⭐ Add review
@login_required
def add_review(request, skill_id):

    skill = get_object_or_404(Skill, id=skill_id)

    # prevent duplicate review
    already_reviewed = Review.objects.filter(
        reviewer=request.user,
        skill=skill
    ).exists()

    if already_reviewed:

        messages.warning(
            request,
            "You already reviewed this skill."
        )

        return redirect('/skills/')

    if request.method == 'POST':

        rating = request.POST.get('rating')

        comment = request.POST.get('comment')

        Review.objects.create(
            reviewer=request.user,
            reviewed_user=skill.user,
            skill=skill,
            rating=rating,
            comment=comment
        )

        messages.success(
            request,
            "Review added successfully!"
        )

        return redirect('/skills/')

    return render(
        request,
        'requests/add_review.html',
        {'skill': skill}
    )