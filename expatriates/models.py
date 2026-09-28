from django.conf import settings
from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Expatriate(models.Model):


    class Gender(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
        OTHER = 'OTHER', 'Other'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='expatriate_profile'
    )

    agency = models.ForeignKey(
        'agencies.Agency',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='expatriates'
    )

    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    passport_number = models.CharField(
        max_length=100,
        unique=True
    )
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )

    phone = models.CharField(max_length=30)
    address_in_uganda = models.CharField(max_length=255)

    job_title = models.CharField(max_length=150)
    employer = models.CharField(max_length=200)

    employment_start_date = models.DateField()
    employment_end_date = models.DateField(
        null=True,
        blank=True
    )

    work_permit_number = models.CharField(
        max_length=100,
        unique=True
    )
    work_permit_expiry = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.passport_number}"

class Document(models.Model):

    class DocumentType(models.TextChoices):
        PASSPORT = 'PASSPORT', 'Passport'
        WORK_PERMIT = 'WORK_PERMIT', 'Work Permit'
        EMPLOYMENT_CONTRACT = 'EMPLOYMENT_CONTRACT', 'Employment Contract'
        OTHER = 'OTHER', 'Other'

    expatriate = models.ForeignKey(
        Expatriate,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    document_type = models.CharField(
        max_length=30,
        choices=DocumentType.choices
    )

    title = models.CharField(max_length=200)

    file = models.FileField(
        upload_to='expatriate_documents/',
        storage=RawMediaCloudinaryStorage()
    )

    expiry_date = models.DateField(
        null=True,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title} - {self.expatriate.user.get_full_name()}"
