from django.shortcuts import render,  get_object_or_404, redirect
from .models import Image
from .forms import ImageForm


def image_list(request):
    images = Image.objects.all()
    return render(request, 'images/image_list.html', {'images': images})

def image_detail(request, id):
    image = get_object_or_404(Image, id=id)
    return render(request, 'images/image_detail.html', {'image': image})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'images/upload_image.html', {'form': form})

def delete_image(request, id):
    image = get_object_or_404(Image, id=id)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return redirect('image_list')
