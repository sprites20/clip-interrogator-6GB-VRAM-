from PIL import Image
#from clip_interrogator import Interrogator, Config
#@title Setup
import os, subprocess
#ci = Interrogator(Config(clip_model_name="ViT-B-32/openai"))
#print(ci.interrogate(image))

import sys
sys.path.append('src/blip')
sys.path.append('clip-interrogator')

from clip_interrogator import Config, Interrogator

# download cache files
"""
print("Download preprocessed cache files...")
CACHE_URLS = [
    #'https://huggingface.co/pharma/ci-preprocess/raw/main/ViT-L-14_openai_artists.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/raw/main/ViT-L-14_openai_flavors.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/raw/main/ViT-L-14_openai_mediums.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/raw/main/ViT-L-14_openai_movements.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/raw/main/ViT-L-14_openai_trendings.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/resolve/main/ViT-H-14_laion2b_s32b_b79k_artists.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/resolve/main/ViT-H-14_laion2b_s32b_b79k_flavors.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/resolve/main/ViT-H-14_laion2b_s32b_b79k_mediums.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/resolve/main/ViT-H-14_laion2b_s32b_b79k_movements.pkl',
    #'https://huggingface.co/pharma/ci-preprocess/resolve/main/ViT-H-14_laion2b_s32b_b79k_trendings.pkl',
]
os.makedirs('cache', exist_ok=True)
for url in CACHE_URLS:
    print(subprocess.run(['wget', url, '-P', 'cache'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
"""
config = Config()
config.blip_num_beams = 64
config.blip_offload = False
config.chunk_size = 2048
config.flavor_intermediate_count = 2048

ci = Interrogator(config)

def inference(image, mode, clip_model_name, best_max_flavors=32):
    if clip_model_name != ci.config.clip_model_name:
        ci.config.clip_model_name = clip_model_name
        ci.load_clip_model()
    image = image.convert('RGB')
    if mode == 'best':
        return ci.interrogate(image, max_flavors=int(best_max_flavors))
    elif mode == 'classic':
        return ci.interrogate_classic(image)
    else:
        return ci.interrogate_fast(image)

from PIL import Image
#from clip_interrogator import Interrogator, Config

#ci = Interrogator(Config(clip_model_name="ViT-B-32/openai"))
#print(ci.interrogate(image))

import sys
sys.path.append('src/blip')
sys.path.append('clip-interrogator')

from clip_interrogator import Config, Interrogator

config = Config()
config.blip_num_beams = 64
config.blip_offload = False
config.chunk_size = 2048
config.flavor_intermediate_count = 2048

ci = Interrogator(config)

def inference(image, mode, clip_model_name, best_max_flavors=16):
    if clip_model_name != ci.config.clip_model_name:
        ci.config.clip_model_name = clip_model_name
        ci.load_clip_model()
    image = image.convert('RGB')
    if mode == 'best':
        return ci.interrogate(image, max_flavors=int(best_max_flavors))
    elif mode == 'classic':
        return ci.interrogate_classic(image)
    else:
        return ci.interrogate_fast(image)

img = Image.open("C:/Users/NakaMura/Desktop/Screenshot 2022-11-27 180640.jpg").convert('RGB')
print(inference(img, "fast", clip_model_name="ViT-B-32/openai"))

img = Image.open("C:/Users/NakaMura/Desktop/Screenshot 2022-11-27 175414.jpg").convert('RGB')
print(inference(img, "best", clip_model_name="ViT-B-32/openai"))