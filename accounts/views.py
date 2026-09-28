from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from expatriates.models import Expatriate, Document
from agencies.models import Agency


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
        return render(
            request,
            'accounts/government_dashboard.html',
            {
                'unread_notifications': unread_notifications,
            }
        )

    return render(
        request,
        'accounts/dashboard.html',
        {
            'unread_notifications': unread_notifications,
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