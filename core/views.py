from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Udhiyah


# 🔍 Donor Search Form Page
def donor_search(request):
    return render(request, 'core/donor_search.html')

# 📊 Donor Status Result Page
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Udhiyah

def donor_status(request):
    udhiyah_id = request.GET.get('udhiyah_id')
    phone = request.GET.get('phone')

    record = Udhiyah.objects.filter(id=udhiyah_id, phone=phone).first()

    if not record:
        return render(request, 'core/donor_status.html', {'status': 'not_found'})

    donor_name = record.name
    current_status = record.status

    # Shared initial steps
    status_sequence = ['paid', 'booked', 'slaughtered', 'cutting']

    # Custom tail based on donation type
    if record.donation_type == 'full':
        status_sequence += ['distributing', 'done']
    else:  # half
        status_sequence += ['half_ready', 'distributing', 'done']

    # Build timeline steps
    timeline_steps = []
    active = True
    for step in status_sequence:
        timeline_steps.append({
            'code': step,
            'label': dict(Udhiyah._meta.get_field('status').choices).get(step, step),
            'active': active
        })
        if step == current_status:
            active = False

    return render(request, 'core/donor_status.html', {
        'udhiyah_id': record.id,
        'phone': record.phone,
        'donor_name': donor_name,
        'status': current_status,
        'timeline_steps': timeline_steps,
    })



from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Udhiyah, STATUS_CHOICES

@csrf_exempt
def admin_panel(request):
    if request.method == "POST":
        udhiyah_id = request.POST.get("udhiyah_id")
        new_status = request.POST.get("status")
        record = Udhiyah.objects.filter(id=udhiyah_id).first()
        if record:
            record.status = new_status
            record.save()
        return redirect('admin_panel')  # ✅ this is inside the if and POST block

    all_udhiyahs = Udhiyah.objects.all().order_by('-updated_at')

    return render(request, 'core/admin_panel.html', {
        'records': all_udhiyahs,
        'status_choices': STATUS_CHOICES
    })  # ✅ this return must be indented under the function
