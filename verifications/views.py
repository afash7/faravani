from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import VerificationCode
from .forms import VerificationForm
from .tasks import send_verification_code

@login_required
def verify_phone(request):
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                verification = VerificationCode.objects.get(user=request.user, code=code)
                verification.is_verified = True
                verification.save()
                messages.success(request, 'Phone number verified successfully.')
                return redirect('profile')
            except VerificationCode.DoesNotExist:
                messages.error(request, 'Invalid verification code.')
    else:
        form = VerificationForm()
    return render(request, 'verification/verify_phone.html', {'form': form})

@login_required
def resend_verification_code(request):
    send_verification_code(request.user.profile.phone_number)
    messages.success(request, 'Verification code resent.')
    return redirect('verify_phone')
