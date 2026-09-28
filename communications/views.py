from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import (
    RequestForm,
    ComplaintForm,
    ComplaintResponseForm,
    RequestResponseForm,
)
from django.contrib import messages
from .models import Request, Complaint, Notification

@login_required
def create_request(request):


    expatriate = request.user.expatriate_profile

    if request.method == 'POST':

        form = RequestForm(request.POST)

        if form.is_valid():

            new_request = form.save(commit=False)

            new_request.expatriate = expatriate
            new_request.save()

            return redirect('my_requests')

    else:
        form = RequestForm()

    return render(
        request,
        'communications/create_request.html',
        {
            'form': form,
        }
    )


@login_required
def my_requests(request):


    expatriate = request.user.expatriate_profile

    requests = expatriate.requests.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'communications/my_requests.html',
        {
            'requests': requests,
        }
    )

@login_required
def create_complaint(request):

    expatriate = request.user.expatriate_profile

    if request.method == 'POST':

        form = ComplaintForm(request.POST)

        if form.is_valid():

            new_complaint = form.save(commit=False)

            new_complaint.expatriate = expatriate
            new_complaint.save()

            return redirect('my_complaints')

    else:
        form = ComplaintForm()

    return render(
        request,
        'communications/create_complaint.html',
        {
            'form': form,
        }
    )


@login_required
def my_complaints(request):

    expatriate = request.user.expatriate_profile

    complaints = expatriate.complaints.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'communications/my_complaints.html',
        {
            'complaints': complaints,
        }
    )

@login_required
def officer_requests(request):

    if request.user.role not in ['AGENCY', 'GOVERNMENT']:
        return redirect('dashboard')

    if request.user.role == 'AGENCY':

        agency = request.user.agencies.first()

        requests = Request.objects.filter(
            expatriate__agency=agency
        ).order_by(
            '-created_at'
        )

    else:

        requests = Request.objects.all().order_by(
            '-created_at'
        )

    return render(
        request,
        'communications/officer_requests.html',
        {
            'requests': requests,
        }
    )

@login_required
def officer_complaints(request):

    if request.user.role not in ['AGENCY', 'GOVERNMENT']:
        return redirect('dashboard')

    if request.user.role == 'AGENCY':

        agency = request.user.agencies.first()

        complaints = Complaint.objects.filter(
            expatriate__agency=agency
        ).order_by(
            '-created_at'
        )

    else:

        complaints = Complaint.objects.all().order_by(
            '-created_at'
        )

    return render(
        request,
        'communications/officer_complaints.html',
        {
            'complaints': complaints,
        }
    )

@login_required
def handle_complaint(request, complaint_id):

    if request.user.role not in ['AGENCY', 'GOVERNMENT']:
        return redirect('dashboard')

    complaint = Complaint.objects.get(
        id=complaint_id
    )

    if request.method == 'POST':

        form = ComplaintResponseForm(
            request.POST,
            instance=complaint
        )

        if form.is_valid():

            updated_complaint = form.save(
                commit=False
            )
            updated_complaint.responded_by = request.user

            updated_complaint.save()

            Notification.objects.create(
                recipient=updated_complaint.expatriate.user,
                title='Complaint Updated',
                message=f'Your complaint "{updated_complaint.subject}" has been updated. Status: {updated_complaint.get_status_display()}.'
            )

            return redirect('officer_complaints')

    else:

        form = ComplaintResponseForm(
            instance=complaint
        )

    return render(
        request,
        'communications/handle_complaint.html',
        {
            'complaint': complaint,
            'form': form,
        }
    )

@login_required
def handle_request(request, request_id):

    if request.user.role not in ['AGENCY', 'GOVERNMENT']:
        return redirect('dashboard')

    request_item = Request.objects.get(
        id=request_id
    )

    if request.method == 'POST':

        form = RequestResponseForm(
            request.POST,
            instance=request_item
        )

        if form.is_valid():

            updated_request = form.save(
                commit=False
            )

            updated_request.responded_by = request.user

            updated_request.save()

            Notification.objects.create(
                recipient=updated_request.expatriate.user,
                title='Request Updated',
                message=f'Your request "{updated_request.subject}" has been updated. Status: {updated_request.get_status_display()}.'
            )

            return redirect('officer_requests')

    else:

        form = RequestResponseForm(
            instance=request_item
        )

    return render(
        request,
        'communications/handle_request.html',
        {
            'request_item': request_item,
            'form': form,
        }
    )

@login_required
def my_notifications(request):

    notifications = request.user.notifications.all().order_by(
        '-created_at'
    )

    notifications.filter(
        is_read=False
    ).update(
        is_read=True
    )

    return render(
        request,
        'communications/my_notifications.html',
        {
            'notifications': notifications,
        }
    )