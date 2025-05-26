from flask import Flask, render_template, request, redirect, url_for, flash, Response, session
from downloader import fetch_playlist_videos, download_video
import os
import threading
import time
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'downloads'

# Global variable to store download progress
progress_data = {
    'downloading': False,
    'current_file': '',
    'progress': 0
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        playlist_url = request.form.get('playlist_url')
        if not playlist_url:
            return render_template('index.html', error="Please enter a playlist URL.", progress_data=progress_data)

        try:
            videos = fetch_playlist_videos(playlist_url)
            return render_template('index.html', videos=videos, playlist_url=playlist_url, progress_data=progress_data)
        except Exception as e:
            return render_template('index.html', error=f"Error fetching playlist: {str(e)}", progress_data=progress_data)

    return render_template('index.html', progress_data=progress_data)

@app.route('/download', methods=['POST'])
def download():
    video_urls = request.form.getlist('video_urls')
    if not video_urls:
        return redirect(url_for('index'))
    
    try:
        global progress_data
        progress_data['downloading'] = True
        progress_data['progress'] = 0
        progress_data['current_file'] = ''

        total_videos = len(video_urls)
        for i, url in enumerate(video_urls, 1):
            progress_data['current_file'] = f"Video {i} of {total_videos}"
            progress_data['progress'] = int((i / total_videos) * 100)
            download_video(url, app.config['UPLOAD_FOLDER'])

        progress_data['downloading'] = False
        progress_data['progress'] = 100
        flash('Download completed successfully!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        progress_data['downloading'] = False
        flash(f'Error during download: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/progress')
def progress():
    def generate():
        while True:
            data = json.dumps(progress_data)
            yield f"data: {data}\n\n"
            if not progress_data['downloading']:
                break
            time.sleep(1)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
