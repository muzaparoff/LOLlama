import os
import logging
from moviepy.editor import VideoFileClip
from PIL import Image

logger = logging.getLogger("thumbnail")

def generate_thumbnail(video_path: str, output_dir: str) -> str:
    """
    Extract a thumbnail from the middle of the video.
    """
    try:
        clip = VideoFileClip(video_path)
        thumb_time = clip.duration / 2
        frame = clip.get_frame(thumb_time)
        image = Image.fromarray(frame)
        thumbnail_path = os.path.join(output_dir, f"thumbnail_{os.path.basename(video_path).split('.')[0]}.png")
        image.save(thumbnail_path)
        return thumbnail_path
    except Exception as e:
        logger.error("Failed to generate thumbnail: %s", e)
        return ""