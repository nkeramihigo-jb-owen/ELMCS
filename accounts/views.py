from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from expatriates.models import Expatriate, Document
from agencies.models import Agency
from django.utils import timezone
from communications.models import Request, Complaint
from monitoring.models import Verification
from expatriates.forms import ExpatriateForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {'error': 'Invalid username or password.'}
        )

    return render(request, 'accounts/login.html')


@login_required
def dashboard(request):

    unread_notifications = request.user.notifications.filter(
        is_read=False
    ).count()

    if request.user.role == 'EXPATRIATE':
        return render(
            request,
            'accounts/expatriate_dashboard.html',
            {
                'unread_notifications': unread_notifications,
            }
        )

    if request.user.role == 'AGENCY':
        return render(
            request,
            'accounts/agency_dashboard.html',
            {
                'unread_notifications': unread_notifications,
            }
        )

    if request.user.role == 'GOVERNMENT':

        total_expatriates = Expatriate.objects.count()

        total_agencies = Agency.objects.count()

        pending_verifications = Verification.objects.filter(
            status=Verification.Status.PENDING
        ).count()

        active_work_permits = Expatriate.objects.filter(
            work_permit_expiry__gte=timezone.now().date()
        ).count()

        pending_requests = Request.objects.filter(
            status=Request.Status.PENDING
        ).count()

        pending_complaints = Complaint.objects.filter(
            status=Complaint.Status.PENDING
        ).count()

    return render(
        request,
        'accounts/government_dashboard.html',
        {
            'unread_notifications': unread_notifications,
            'total_expatriates': total_expatriates,
            'total_agencies': total_agencies,
            'pending_verifications': pending_verifications,
            'active_work_permits': active_work_permits,
            'pending_requests': pending_requests,
            'pending_complaints': pending_complaints,
        }
    )

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def expatriate_profile(request):
    expatriate = request.user.expatriate_profile


    return render(
        request,
        'accounts/expatriate_profile.html',
        {
            'expatriate': expatriate
        }
    )

@login_required
def expatriate_documents(request):
    expatriate = request.user.expatriate_profile
    documents = expatriate.documents.all()


    return render(
        request,
        'accounts/expatriate_documents.html',
        {
            'expatriate': expatriate,
            'documents': documents,
        }
    )

@login_required
def expatriate_detail(request, expatriate_id):

    if request.user.role not in ['AGENCY', 'GOVERNMENT']:
        return redirect('dashboard')

    expatriate = get_object_or_404(
        Expatriate.objects.select_related(
            'user',
            'agency'
        ),
        id=expatriate_id
    )

    if request.user.role == 'AGENCY':

        agency = request.user.agencies.first()

        if expatriate.agency != agency:
            return redirect('agency_expatriates')

    documents = expatriate.documents.all().order_by(
        '-uploaded_at'
    )

    verification = expatriate.verifications.select_related(
        'verified_by'
    ).order_by(
        '-created_at'
    ).first()

    return render(
        request,
        'accounts/expatriate_detail.html',
        {
            'expatriate': expatriate,
            'documents': documents,
            'verification': verification,
        }
    )

@login_required
def agency_expatriates(request):

    if request.user.role != 'AGENCY':
        return redirect('dashboard')

    agency = request.user.agencies.first()

    expatriates = Expatriate.objects.filter(
        agency=agency
    ).order_by(
        'user__first_name',
        'user__last_name'
    )

    return render(
        request,
        'accounts/agency_expatriates.html',
        {
            'agency': agency,
            'expatriates': expatriates,
        }
    )

@login_required
def my_agency(request):

    if request.user.role != 'AGENCY':
        return redirect('dashboard')

    agency = request.user.agencies.first()

    return render(
        request,
        'accounts/my_agency.html',
        {
            'agency': agency,
        }
    )

@login_required
def agency_documents(request):

    if request.user.role != 'AGENCY':
        return redirect('dashboard')

    agency = request.user.agencies.first()

    documents = Document.objects.filter(
        expatriate__agency=agency
    ).select_related(
        'expatriate__user'
    ).order_by(
        '-uploaded_at'
    )

    return render(
        request,
        'accounts/agency_documents.html',
        {
            'agency': agency,
            'documents': documents,
        }
    )

@login_required
def government_agencies(request):

    if request.user.role != 'GOVERNMENT':
        return redirect('dashboard')

    agencies = Agency.objects.all().order_by('name')

    return render(
        request,
        'accounts/government_agencies.html',
        {
            'agencies': agencies,
        }
    )

@login_required
def government_expatriates(request):

    if request.user.role != 'GOVERNMENT':
        return redirect('dashboard')

    expatriates = Expatriate.objects.select_related(
        'user',
        'agency'
    ).order_by(
        'user__first_name',
        'user__last_name'
    )

    return render(
        request,
        'accounts/government_expatriates.html',
        {
            'expatriates': expatriates,
        }
    )

@login_required
def government_documents(request):

    if request.user.role != 'GOVERNMENT':
        return redirect('dashboard')

    documents = Document.objects.select_related(
        'expatriate__user',
        'expatriate__agency'
    ).order_by(
        '-uploaded_at'
    )

    return render(
        request,
        'accounts/government_documents.html',
        {
            'documents': documents,
        }
    )

@login_required
def government_work_permits(request):

    if request.user.role != 'GOVERNMENT':
        return redirect('dashboard')

    expatriates = Expatriate.objects.select_related(
        'user',
        'agency'
    ).order_by(
        'work_permit_expiry'
    )

    return render(
        request,
        'accounts/government_work_permits.html',
        {
            'expatriates': expatriates,
            'today': timezone.now().date(),
        }
    )

@login_required
def edit_expatriate(request, expatriate_id):

    if request.user.role != 'GOVERNMENT':
        return redirect('dashboard')

    expatriate = get_object_or_404(
        Expatriate,
        id=expatriate_id
    )

    if request.method == 'POST':

        form = ExpatriateForm(
            request.POST,
            instance=expatriate
        )

        if form.is_valid():

            form.save()

            return redirect(
                'expatriate_detail',
                expatriate_id=expatriate.id
            )

    else:

        form = ExpatriateForm(
            instance=expatriate
        )

    return render(
        request,
        'accounts/edit_expatriate.html',
        {
            'expatriate': expatriate,
            'form': form,
        }
    )