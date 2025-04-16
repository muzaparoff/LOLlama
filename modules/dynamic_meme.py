import os
import torch
from diffusers import StableDiffusionPipeline
import logging
from contextlib import contextmanager

logger = logging.getLogger("dynamic_meme")

@contextmanager
def nullcontext():
    yield

def generate_dynamic_meme(prompt: str, output_path: str) -> str:
    """
    Generate a meme image dynamically using a text prompt.
    Uses Stable Diffusion for text-to-image generation.
    
    Args:
        prompt (str): Text prompt describing the desired meme (e.g., "Russian gamer meme, Cheeki Breeki style, epic Call of Duty moment").
        output_path (str): File path to save the generated meme image.
        
    Returns:
        str: Path to the saved meme image.
    """
    logger.info("Generating dynamic meme with prompt: '%s'", prompt)
    model_id = "CompVis/stable-diffusion-v1-4"  # Change if using a fine-tuned model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    try:
        pipe = StableDiffusionPipeline.from_pretrained(model_id)
        pipe = pipe.to(device)
    except Exception as e:
        logger.error("Failed to load the Stable Diffusion pipeline: %s", e)
        raise e

    # Use autocast if on CUDA (otherwise, use a dummy context)
    context = torch.autocast(device) if device == "cuda" else nullcontext()
    with context:
        # Generate the image
        result = pipe(prompt, num_inference_steps=50)
        image = result["sample"][0]
    
    image.save(output_path)
    logger.info("Meme image saved at: %s", output_path)
    return output_path