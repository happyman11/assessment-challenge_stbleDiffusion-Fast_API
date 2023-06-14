import torch
from PIL import Image
from diffusers import StableDiffusionPipeline

def stable_diffusion_image(sentence):
    
    if torch.cuda.is_available():
        pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)  
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16) 
        pipe = pipe.to(device)
        image = pipe(sentence).images[0] 
        image.save(f"output_image.png")
        data ={}
        data["GPU"]=1
        data["image_name"]="output_image.png"
        return data
    else:
        data ={}
        data["GPU"]=0
        return data