import os
import base64
import numpy as np
from PIL import Image
from io import BytesIO
from fastapi import FastAPI,Request
from  utility import  stable_diffusion_image


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

app = FastAPI()

cwd=os.getcwd()
path=os.path.join(cwd,"Data_generated")

@app.post("/diffusuion_stable")
async def diffusion(info : Request):
    req_info = await info.json()
    if str(req_info["data"]).strip():
        data=str(req_info["data"])
        data_diffusion= stable_diffusion_image(data)
        if data_diffusion["GPU"]:
            
            image_name=data_diffusion["image_name"]
            path_image=os.path.join(path,image_name)
            image = Image.open(path_image)
            byte_stream = BytesIO()
            image.save(byte_stream, format='PNG')
            byte_stream.seek(0)
            image=base64.b64encode(byte_stream.getvalue()).decode("utf-8")
        
        
            dev={}
            dev["status_code"]=200
            dev["response"]="The Image is shown below"
            dev["sentence"]=req_info["data"]
            dev["image"]=image
        
            return dev
        
        else:
            dev={}
            dev["status_code"]=200
            dev["response"]="GPU is not present!!!OOps"
            dev["sentence"]=req_info["data"]
            
            return dev
        
            
        
    else:
        
        dev={}
        dev["status_code"]=422
        dev["response"]="Check the  Payload Format"
        dev["sent_payload"]=req_info
             
        return dev
