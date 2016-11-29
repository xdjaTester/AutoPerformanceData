from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def get_fps(request):
    return render(request, 'get_fps.html')

def get_memory(request):
    return render(request, 'get_memory.html')

def get_cpu(request):
    return render(request, 'get_cpu.html')

def get_flow(request):
    return render(request, 'get_flow.html')

def get_kpi(request):
    return render(request, 'get_kpi.html')

def get_power(request):
    return render(request, 'get_power.html')