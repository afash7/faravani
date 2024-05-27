from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from .models import Upload

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            return redirect('upload_list')
    else:
        form = UploadForm()
    return render(request, 'uploads/upload_form.html', {'form': form})

@login_required
def upload_list(request):
    uploads = Upload.objects.filter(user=request.user)
    return render(request, 'uploads/upload_list.html', {'uploads': uploads})
