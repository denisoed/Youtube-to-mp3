from django.shortcuts import render, render_to_response, redirect
from .forms import YoutubeForms
import  os
from .tasks import handler_youtube_video

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'main/static')

# Main view for init page
def main(request):
    form = YoutubeForms()
    return render(request, 'main.html', {'form': form})

def accept_data(request):
    if request.method == 'POST':
        form = YoutubeForms(request.POST)
        if form.is_valid():
            url = request.POST.get('url')
            email = request.POST.get('email')

            # Start download video from youtube
            handler_youtube_video.delay(url, email)

            return render_to_response('success.html', {'email': email})
    else:
        return redirect('/')
