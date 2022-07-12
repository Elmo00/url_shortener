from django.shortcuts import render

from .forms import URLShortenerForm
from hashlib import md5


def index(request):
    context = {}
    return render(request, 'shortener/index.html', context)


def general(request):
    if request.method == 'POST':
        form = URLShortenerForm(request.POST)
        print(type(form['url']))
        print(str(form['url'])[:-11])
        new_url = md5(str(form['url']).encode()).hexdigest()
        print(new_url)
        form.new_url = new_url
        if form.is_valid():
            print(form.cleaned_data)
        print(form.fields['url'])
        # def save(self, *args, **kwargs):
        #     self.new_url = md5(self.url.encode()).hexdigest()
        #     print(self.new_url)
        #     return super().save(*args, **kwargs)

    else:
        form = URLShortenerForm()
    context = {
        'form': form,
    }
    return render(request, 'shortener/general.html', context)
