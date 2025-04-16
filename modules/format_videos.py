import os
import logging
from moviepy.editor import VideoFileClip

logger = logging.getLogger("format_videos")

def format_video_for_platform(video_path: str, platform: str, output_dir: str) -> str:
    """
    Format the provided video for a specific social platform.
    For TikTok and Instagram, produce a vertical (9:16) version.
    """
    logger.info("Formatting video for %s: %s", platform, video_path)
    if not os.path.isfile(video_path):
        logger.error("Video file does not exist: %s", video_path)
        return video_path
    if not os.path.isdir(output_dir):
        logger.error("Output directory does not exist: %s", output_dir)
        return video_path
    if platform.lower() not in ["tiktok", "instagram"]:
        logger.error("Unsupported platform: %s", platform)
        return video_path
    if not video_path.lower().endswith((".mp4", ".mkv", ".webm")):
        logger.error("Unsupported video format: %s", video_path)
        return video_path
    try:
        clip = VideoFileClip(video_path)
        w, h = clip.size
        if platform.lower() in ["tiktok", "instagram"]:
            target_width = 540
            target_height = 960
            # Simple center crop: calculate crop region and resize.
            new_w = w
            new_h = int(w * (16/9))
            if new_h > h:
                new_h = h
                new_w = int(h * (9/16))
            crop_x = (w - new_w) // 2
            crop_y = (h - new_h) // 2
            cropped = clip.crop(x1=crop_x, y1=crop_y, x2=crop_x+new_w, y2=crop_y+new_h)
            resized = cropped.resize(newsize=(target_width, target_height))
            output_path = os.path.join(output_dir, f"{platform}_{os.path.basename(video_path)}")
            resized.write_videofile(output_path, codec="libx264", audio_codec="aac")
            return output_path
        else:
            logger.error("Unsupported platform for formatting: %s", platform)
            return video_path
    except Exception as e:
        logger.error("Failed to format video for %s: %s", platform, e)
        return video_path