from django.shortcuts import render, redirect
import requests

def search_tracks(track_name):
    api_key = "ed11917c769823bc8502f780fd693659"
    api_url = "http://ws.audioscrobbler.com/2.0/"

    params = {
        "method": "track.search",
        "track": track_name,
        "api_key": api_key,
        "format": "json"
    }

    response = requests.get(api_url, params=params)

    data = response.json()

    if 'results' in data and 'trackmatches' in data['results']:
        tracks = data['results']['trackmatches']['track']
        return tracks
    return None

def home(request):
    tracks = []
    if request.method == 'POST':
        track_name = request.POST.get('track_name')
        tracks = search_tracks(track_name)

        if 'search_history' not in request.session:
            request.session['search_history'] = []

        request.session['search_history'].insert(0, track_name)
        request.session.modified = True

    return render(request, 'music/home.html', {'tracks': tracks})

def search_history(request):
    history = request.session.get('search_history', [])
    
    if request.method == 'POST':
        track_to_delete = request.POST.get('delete')
        if track_to_delete in history:
            history.remove(track_to_delete)
            request.session['search_history'] = history
            request.session.modified = True
    
    return render(request, 'music/search_history.html', {'history': history})

