from django.shortcuts import render_to_response

def magnifyingGlass(request):
    return render_to_response('magnifyingGlass.html', {})

def screenDarkening(request):
    return render_to_response('screenDarkening.html', {})