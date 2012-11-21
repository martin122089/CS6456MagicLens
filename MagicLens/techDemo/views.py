from django.shortcuts import render_to_response

def magnifyingGlass(request):
    return render_to_response('magnifyingGlass.html', {})

def screenDim(request):
    return render_to_response('screenDim.html', {})

def resizeContent(request):
    return render_to_response('resizeContent.html', {})

def textAnnotate(request):
    return render_to_response('textAnnotate.html', {})

def viewCode(request):
    return render_to_response('viewCode.html', {})

def screenShot(request):
    return render_to_response('screenShot.html', {})

def highlight(request):
    return render_to_response('highlight.html', {})

def dummyWebsite(request):
    return render_to_response('dummyWebsite.html', {})
    