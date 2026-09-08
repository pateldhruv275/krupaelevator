from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import JobOpening, JobApplication
from .forms import JobApplicationForm


def career_list(request):
    """
    Careers portal displaying company culture, engineering perks, and open positions.
    """
    jobs = JobOpening.objects.filter(active=True).order_by('display_order', '-created_at')

    # Available filter choices
    available_departments = JobOpening.objects.filter(active=True).values_list('department', flat=True).distinct()
    available_locations = JobOpening.objects.filter(active=True).values_list('location', flat=True).distinct()

    selected_department = request.GET.get('department', '').strip()
    selected_location = request.GET.get('location', '').strip()

    if selected_department:
        jobs = jobs.filter(department=selected_department)
    if selected_location:
        jobs = jobs.filter(location__icontains=selected_location)

    context = {
        'jobs': jobs,
        'available_departments': available_departments,
        'available_locations': available_locations,
        'selected_department': selected_department,
        'selected_location': selected_location,
        'total_vacancies': sum(j.number_of_vacancies for j in jobs),
    }
    return render(request, 'careers/career_list.html', context)


def career_detail(request, slug):
    """
    Detailed job role specifications and candidate resume application form.
    """
    job = get_object_or_404(JobOpening, slug=slug, active=True)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(
                request,
                f"Thank you, {application.applicant_name}! Your application for '{job.title}' "
                f"has been submitted successfully (Application Ref #{application.id}). "
                f"Our HR recruitment team will review your resume and contact you at {application.email}."
            )
            return redirect('careers:detail', slug=job.slug)
        else:
            messages.error(request, "There was an issue with your application submission. Please review the errors below.")
    else:
        form = JobApplicationForm()

    other_jobs = JobOpening.objects.filter(
        active=True
    ).exclude(pk=job.pk).order_by('display_order')[:4]

    context = {
        'job': job,
        'form': form,
        'other_jobs': other_jobs,
        'responsibilities': job.get_responsibilities_list(),
        'requirements': job.get_requirements_list(),
        'benefits': job.get_benefits_list(),
    }
    return render(request, 'careers/career_detail.html', context)
