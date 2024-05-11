import numpy as np
import cv2
try:
    from cv2.ximgproc import guidedFilter # type: ignore
except ImportError:
    raise ImportError('Please install opencv-contrib-python package with: pip install opencv-contrib-python')
from diffusers import AutoencoderKL
import torch
import numpy as np

vae = AutoencoderKL.from_pretrained("stabilityai/sdxl-vae")
vae.enable_tiling()
vae = vae.to("cuda")
def clean(image: np.ndarray):
    #covert image to tensor
    baseimg = image.copy()
    image = torch.from_numpy(image)
    image = image.to("cuda").float()
    image = image.unsqueeze(0).permute(0, 3, 1, 2)
    if len(image.shape)<4:
        image = image.unsqueeze(0)
    with torch.no_grad():
        latent = vae.encode(image*2 - 1) 
    latents = 0.18215 * latent.latent_dist.sample()
    latents = (1 / 0.18215) * latents
    with torch.no_grad():
        image = vae.decode(latents).sample
    image = (image / 2 + 0.5).clamp(0, 1)
    #rearrange dimensions
    image = image[0]
    image = image.permute(1, 2, 0).detach().cpu().numpy()
    y = image.copy()
    for _ in range(8):
        baseimg = guidedFilter(baseimg, y, 4, 16)
    return baseimg