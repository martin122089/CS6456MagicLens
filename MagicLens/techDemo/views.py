from django.shortcuts import render_to_response

def magnifyingGlass(request):
    return render_to_response('magnifyingGlass.html', {})

def screenDim(request):
    return render_to_response('screenDim.html', {})

def resizeContent(request):
    return render_to_response('resizeContent.html', {})

def textAnnotate(request):
    return render_to_response('textAnnotate.html', {})
    