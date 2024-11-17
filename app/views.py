from django.shortcuts import render, redirect
from .models import Testimonial
from .forms import TestimonialForm

# Create your views here.

def index(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {'testimonials': testimonials})

def create_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = TestimonialForm()
    return render(request, 'create_testimonial.html', {'form': form})

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial_list.html', {'testimonials': testimonials})

def update_testimonial(request, pk):
    testimonial = Testimonial.objects.get(pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
        else:
            form = TestimonialForm(instance=testimonial)
            return render(request, 'update_testimonial.html', {'form': form})

def delete_testimonial(request, pk):
    testimonial = Testimonial.objects.get(pk=pk)
    testimonial.delete()
    return redirect('testimonial_list')

