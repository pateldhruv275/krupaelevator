from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ContactEnquiryForm, QuoteRequestForm


def quote_request_view(request):
    """
    Dedicated Request A Quote page with structured engineering specification inputs.
    """
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote = form.save()
            messages.success(
                request,
                f"Thank you, {quote.customer_name}! Your quotation request for {quote.number_of_elevators} "
                f"{quote.elevator_type} unit(s) has been successfully registered (Ref #{quote.id}). "
                f"Our engineering estimating team will prepare structural clearance notes and send the official proposal to {quote.email}."
            )
            return redirect('enquiries:quote_request')
        else:
            messages.error(request, "There was an error in your submission. Please check the highlighted fields below.")
    else:
        # Pre-fill initial elevator type if passed via query parameter (e.g. from Product Detail page)
        initial_data = {}
        elevator_type_param = request.GET.get('elevator_type') or request.GET.get('type')
        if elevator_type_param:
            initial_data['elevator_type'] = elevator_type_param
        
        city_param = request.GET.get('city')
        if city_param:
            initial_data['city'] = city_param

        form = QuoteRequestForm(initial=initial_data)

    context = {
        'form': form,
        'page_title': 'Request An Engineering Quotation | Krupa Elevator',
    }
    return render(request, 'enquiries/quote_request.html', context)


def contact_view(request):
    """
    Dedicated Contact page and general enquiry handler.
    """
    if request.method == 'POST':
        form = ContactEnquiryForm(request.POST)
        next_url = request.POST.get('next', '').strip()
        if form.is_valid():
            enquiry = form.save()
            messages.success(
                request,
                f"Thank you, {enquiry.name}! Your enquiry has been received (Ref #{enquiry.id}). "
                f"A Krupa Elevator representative will connect with you at {enquiry.phone} shortly."
            )
            if next_url and next_url.startswith('/'):
                return redirect(next_url)
            return redirect('enquiries:contact')
        else:
            messages.error(request, "Please correct the errors in the form below and submit again.")
            if next_url and next_url.startswith('/'):
                # When submitted from homepage or modal, redirect with error notice
                return redirect(f"{next_url}#quote")
    else:
        initial_data = {}
        subject_param = request.GET.get('subject')
        if subject_param:
            initial_data['subject'] = subject_param
        form = ContactEnquiryForm(initial=initial_data)

    context = {
        'form': form,
        'page_title': 'Contact Krupa Elevator | 24/7 Breakdown & Corporate Head Office',
    }
    return render(request, 'enquiries/contact.html', context)
