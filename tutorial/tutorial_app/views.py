from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'tutorial_app/test.html')
def rsp(request):
    return render(request, 'tutorial_app/rsp.html')