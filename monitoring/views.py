from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from expatriates.models import Expatriate
from .models import Verification


@login_required
def government_verification(request, expatriate_id):

    if request.user.role != 'GOVERNMENT':
        return redirect('dashboard')

    expatriate = get_object_or_404(
        Expatriate,
        id=expatriate_id
    )

    verification = expatriate.verifications.order_by(
        '-created_at'
    ).first()

    if request.method == 'POST':

        status = request.POST.get('status')
        notes = request.POST.get('notes', '').strip()

        verification, created = Verification.objects.get_or_create(
            expatriate=expatriate,
            defaults={
                'status': Verification.Status.PENDING
            }
        )

        verification.status = status
        verification.notes = notes
        verification.verified_by = request.user
        verification.verified_at = timezone.now()

        verification.save()

        return redirect(
            'government_verification',
            expatriate_id=expatriate.id
        )

    return render(
        request,
        'monitoring/government_verification.html',
        {
            'expatriate': expatriate,
            'verification': verification,
        }
    )

@login_required
def government_verifications(request):

    if request.user.role != 'GOVERNMENT':
        return redirect('dashboard')

    verifications = Verification.objects.select_related(
        'expatriate__user',
        'expatriate__agency',
        'verified_by'
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'monitoring/government_verifications.html',
        {
            'verifications': verifications,
        }
    )