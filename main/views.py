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
    url = request.POST.get('url')

    # Start convert video
    handler_youtube_video.delay(url)

    return render_to_response('success.html', {'url': url})
