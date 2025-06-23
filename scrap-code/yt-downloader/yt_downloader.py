'''
Python YouTube Video Downloader using yt-dlp

Dependencies:
  - yt-dlp (pip install yt-dlp)

Usage:
  python yt_downloader.py --url <VIDEO_URL> [--output <OUTPUT_DIR>] [--resolution <RESOLUTION>]
  python yt_downloader.py --playlist <PLAYLIST_URL> [--output <OUTPUT_DIR>] [--resolution <RESOLUTION>]
'''
import argparse
import os
from yt_dlp import YoutubeDL

def build_opts(output_path: str, resolution: str = None, playlist: bool = False):
    if playlist:
        outtmpl = os.path.join(output_path, '%(playlist_title)s', '%(title)s.%(ext)s')
    else:
        outtmpl = os.path.join(output_path, '%(title)s.%(ext)s')

    if resolution:
        height = resolution.rstrip('p') if resolution.endswith('p') else resolution
        fmt = f"bestvideo[height<={height}]+bestaudio/best"
    else:
        fmt = 'best'

    return {
        'outtmpl': outtmpl,
        'format': fmt,
        'noplaylist': not playlist,
        'ignoreerrors': True,
        'quiet': False,
        'no_warnings': True,
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]
    }


def download_urls(urls, output_path: str, resolution: str = None, playlist: bool = False):
    opts = build_opts(output_path, resolution, playlist)
    with YoutubeDL(opts) as ydl:
        ydl.download(urls)


def main():
    parser = argparse.ArgumentParser(description="Python YouTube Video Downloader using yt-dlp")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url', help='Single video URL to download')
    group.add_argument('--playlist', help='Playlist URL to download')
    parser.add_argument('--output', '-o', default='.', help='Output directory')
    parser.add_argument('--resolution', '-r', help='Desired resolution (e.g., 720p)')

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    if args.url:
        print(f"Downloading video: {args.url}")
        download_urls([args.url], args.output, args.resolution, playlist=False)
    elif args.playlist:
        print(f"Downloading playlist: {args.playlist}")
        download_urls([args.playlist], args.output, args.resolution, playlist=True)

if __name__ == '__main__':
    main()
