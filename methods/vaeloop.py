from diffusers import AutoencoderKL
import torch
import numpy as np

vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix")
vae.enable_tiling()
vae = vae.to("cuda")

def clean(image: np.ndarray):
    #covert image to tensor
    image = torch.from_numpy(image)
    image = image.to("cuda").float()
    image = image.unsqueeze(0).permute(0, 3, 1, 2)
    
    if len(image.shape)<4:
        image = image.unsqueeze(0)
    
    with torch.no_grad():
        latents = vae.encode(image).latent_dist.sample()

    latents = 0.13025 * latents
    with torch.no_grad():
        image = vae.decode(latents).sample
    image = (image).clamp(0, 1) * 255
    
    #rearrange dimensions
    image = image[0]
    image = image.permute(1, 2, 0).detach().cpu().numpy()
    
    return image