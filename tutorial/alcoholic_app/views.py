from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'alcoholic_app/test.html')
def rsp(request):
    return render(request, 'alcoholic_app/rsp.html')