from django.shortcuts import render_to_response

def magnifyingGlass(request):
    return render_to_response('magnifyingGlass.html', {})

def screenDim(request):
    return render_to_response('screenDim.html', {})

def resizeContent(request):
    return render_to_response('resizeContent.html', {})

def textAnnotation(request):
    return render_to_response('textAnnotation.html', {})

def viewCode(request):
    return render_to_response('viewCode.html', {})

def screenShot(request):
    return render_to_response('screenShot.html', {})

def textHighlight(request):
    return render_to_response('textHighlight.html', {})

def dummyWebsite(request):
    return render_to_response('dummyWebsite.html', {})
    