import yt_dlp
import os
import asyncio
from typing import Callable
from functools import partial

# ✅ Manually set ffmpeg path
ffmpeg_path = r"C:\ffmpeg-7.1.1-essentials_build\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

def fetch_playlist_videos(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': False
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(url, download=False)
            if 'entries' in result:
                # It's a playlist
                return [{'id': entry['id'], 'title': entry['title']} for entry in result['entries']]
            else:
                # It's a single video
                return [{'id': result['id'], 'title': result['title']}]
        except Exception as e:
            raise Exception(f"Error extracting video info: {str(e)}")

def download_video(url, output_path='downloads'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

async def download_playlist(url, output_path='downloads', progress_callback: Callable = None):
    def progress_hook(loop, d):
        if progress_callback:
            if d['status'] == 'downloading':
                progress = {
                    'status': 'downloading',
                    'filename': d.get('filename', ''),
                    'downloaded_bytes': d.get('downloaded_bytes', 0),
                    'total_bytes': d.get('total_bytes', 0),
                    'speed': d.get('speed', 0),
                    'eta': d.get('eta', 0),
                    'progress': d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100 if d.get('total_bytes', 0) > 0 else 0
                }
                # Convert the callback to a regular function
                loop.call_soon_threadsafe(lambda: progress_callback(progress))
            elif d['status'] == 'finished':
                progress = {
                    'status': 'finished',
                    'filename': d.get('filename', '')
                }
                # Convert the callback to a regular function
                loop.call_soon_threadsafe(lambda: progress_callback(progress))

    loop = asyncio.get_event_loop()
    hook = partial(progress_hook, loop)
    
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': False,
        'progress_hooks': [hook],
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        await asyncio.get_event_loop().run_in_executor(None, ydl.download, [url])

if __name__ == '__main__':
    playlist_url = input("Enter the playlist URL: ")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(download_playlist(playlist_url))
