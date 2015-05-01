from django.shortcuts import render


def twitter_template(request):
    return render(request, 'landing_page.html')

def test(request):
    return render(request, 'test.html')
