import os
import logging
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips, ImageClip
from modules import dynamic_meme

logger = logging.getLogger("meme_overlay")

def overlay_memes_dynamic(video_path: str, highlights: list, output_dir: str, duration=300) -> str:
    """
    Overlays dynamically generated memes onto the video based on contextual analysis.
    Replaces the static local folder approach with AI-generated memes.
    """
    clip = VideoFileClip(video_path)
    
    if not highlights:
        raise ValueError("No highlight segments found for meme overlay.")
    
    # In a real implementation, generate your contextual prompt from analysis.
    # Here we use a dummy prompt based on the first highlight.
    start_time, _ = highlights[0]
    prompt = "Russian gamer meme, Cheeki Breeki style, epic Call of Duty moment"
    dynamic_meme_path = os.path.join(output_dir, f"dynamic_meme_{start_time}.png")
    
    try:
        meme_image_path = dynamic_meme.generate_dynamic_meme(prompt, dynamic_meme_path)
    except Exception as e:
        logger.error("Dynamic meme generation failed: %s", e)
        meme_image_path = None

    if meme_image_path:
        meme_clip = (ImageClip(meme_image_path)
                     .set_duration(5)
                     .resize(width=clip.w)
                     .set_position(("center", "bottom")))
        subclip = clip.subclip(start_time, min(start_time+5, clip.duration))
        composite = CompositeVideoClip([subclip, meme_clip])
        pre = clip.subclip(0, start_time)
        post = clip.subclip(min(start_time+5, clip.duration), clip.duration)
        edited_clip = concatenate_videoclips([pre, composite, post])
        # Ensure the final video is exactly 'duration' seconds long.
        if edited_clip.duration > duration:
            edited_clip = edited_clip.subclip(0, duration)
        elif edited_clip.duration < duration:
            loops = int(duration // edited_clip.duration) + 1
            edited_clip = concatenate_videoclips([edited_clip] * loops).subclip(0, duration)
    else:
        # If dynamic generation fails, return a trimmed clip.
        edited_clip = clip.subclip(0, min(duration, clip.duration))
    
    output_path = os.path.join(output_dir, f"edited_{os.path.basename(video_path).split('.')[0]}_dynamic.mp4")
    edited_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path