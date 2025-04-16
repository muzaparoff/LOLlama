import os
import subprocess
import logging
import shlex

logger = logging.getLogger("downloader")

def download_video(youtube_url: str, output_dir: str) -> str:
    """
    Download the best quality video from YouTube using yt-dlp.
    Returns the path to the downloaded video file.
    """
    if not os.path.isdir(output_dir):
        logger.error("Output directory does not exist: %s", output_dir)
        return ""
    output_template = os.path.join(output_dir, "%(title)s_%(id)s.%(ext)s")
    command = f"yt-dlp -f best -o \"{output_template}\" {youtube_url}"
    logger.info("Running command: %s", command)
    try:
        subprocess.run(shlex.split(command), check=True)
    except FileNotFoundError:
        logger.error("yt-dlp not found. Please install yt-dlp.")
        return ""
    except subprocess.CalledProcessError as e:
        logger.error("yt-dlp failed: %s", e)
        return ""
    
    # Return the most recent downloaded video file from the output directory
    files = [os.path.join(output_dir, f) for f in os.listdir(output_dir)]
    video_files = [f for f in files if f.lower().endswith((".mp4", ".mkv", ".webm"))]
    if not video_files:
        return ""
    latest_file = max(video_files, key=os.path.getmtime)
    return latest_file