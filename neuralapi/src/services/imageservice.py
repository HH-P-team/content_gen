from neuro_gateway.stable_diffusion import StableDiffusion
from neuro_gateway.kandinsky import Kandinsky


def get_generate_sd_service() -> list[StableDiffusion]:

    keys = [my, andry, ev_key, alex_key, key]

    path = "downloads"

    instances = []
    for key in keys:
        instances.append(StableDiffusion(key, path))

    return instances


def get_generate_kad_service() -> list[StableDiffusion]:

    token = ""
    path = "downloads"

    return Kandinsky(token, path)
