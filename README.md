# YouTube Playlist Downloader

A powerful and user-friendly web application that enables users to download YouTube videos and playlists with ease. Built using Python Flask and yt-dlp, this application provides a seamless experience for managing and downloading YouTube content.

## Key Features

- **Playlist Support**: Download entire YouTube playlists or select specific videos
- **Individual Video Download**: Support for single video downloads
- **Real-time Progress**: Live progress tracking with percentage completion
- **User-friendly Interface**: Clean and intuitive web interface
- **Quality Options**: Downloads highest available video quality
- **Format Consistency**: Outputs videos in MP4 format for maximum compatibility
- **Batch Processing**: Download multiple videos simultaneously
- **Error Handling**: Robust error management and user feedback

## Technical Requirements

### System Requirements
- Windows 10/11 (64-bit)
- 4GB RAM minimum
- Internet connection
- 1GB free disk space (plus space for videos)

### Software Prerequisites
- **Python**: Version 3.7 or higher
- **FFmpeg**: Required for video processing
- **Web Browser**: Chrome, Firefox, or Edge (latest versions)
- **pip**: Python package manager

## Installation Guide

### 1. Python Setup
```bash
# Check Python version
python --version  # Should be 3.7 or higher
```

### 2. Project Setup
```bash
# Clone repository
git clone <your-repository-url>

# Navigate to project directory
cd YoutubePlaylistDownloader

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. FFmpeg Installation
1. Download FFmpeg from [official website](https://ffmpeg.org/download.html)
2. Extract to `C:\ffmpeg-7.1.1-essentials_build`
3. Add to PATH:
   - Open System Properties → Advanced → Environment Variables
   - Add `C:\ffmpeg-7.1.1-essentials_build\bin` to System PATH

## Getting Started

### Starting the Application
1. Activate virtual environment (if not activated):
```bash
venv\Scripts\activate
```

2. Run the application:
```bash
python main.py
```

3. Access the web interface:
- Open your browser
- Navigate to `http://localhost:5000`

### Using the Application

1. **Entering URLs**
   - Paste YouTube playlist or video URL
   - Click "Fetch Videos"

2. **Selecting Videos**
   - Use "Select All" or choose individual videos
   - Review selected videos before downloading

3. **Downloading**
   - Click "Download Selected Videos"
   - Monitor progress in real-time
   - Wait for completion notification

## 📁 File Structure
```
YoutubePlaylistDownloader/
├── main.py              # Main application file
├── downloader.py        # Download functionality
├── requirements.txt     # Python dependencies
├── static/             # Static files (CSS, JS)
├── templates/          # HTML templates
└── downloads/          # Downloaded videos
```

## Configuration

### Default Settings
- Download Path: `./downloads/`
- Video Format: MP4
- Quality: Best available
- Audio Format: AAC

## Troubleshooting

### Common Issues
1. **FFmpeg Not Found**
   - Verify FFmpeg installation
   - Check PATH environment variable

2. **Download Fails**
   - Check internet connection
   - Verify URL validity
   - Ensure sufficient disk space

3. **Video Quality Issues**
   - Check source video quality
   - Verify FFmpeg installation

## 🛡️ Security Features
- Input validation
- Error handling
- Safe file handling
- Progress monitoring

## 🤝 Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 🙏 Acknowledgments
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading capabilities
- [Flask](https://flask.palletsprojects.com/) for web framework
- [FFmpeg](https://ffmpeg.org/) for media processing

## 📞 Support
For issues and feature requests, please use the GitHub issues page.

## 🔄 Updates
Check the repository regularly for updates and improvements.
