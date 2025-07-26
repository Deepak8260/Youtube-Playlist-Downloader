from flask import Flask, render_template, request, jsonify
import yt_dlp
from downloader import download_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_playlist_videos', methods=['POST'])
def get_playlist_videos():
    playlist_url = request.form['playlist_url']
    try:
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'cookiefile': 'cookies.txt',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(playlist_url, download=False)
            entries = info_dict.get('entries', [])

        videos = [{
            'title': video['title'],
            'url': f"https://www.youtube.com/watch?v={video['id']}"
        } for video in entries]

        return jsonify({'videos': videos})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/download_video', methods=['POST'])
def download_selected_video():
    video_url = request.form['video_url']
    try:
        download_video(video_url)
        return jsonify({'status': 'Download successful'})
    except Exception as e:
        return jsonify({'status': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
