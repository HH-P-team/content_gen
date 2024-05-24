from neuro_gateway.stable_diffusion import StableDiffusion
from neuro_gateway.kandinsky import Kandinsky
from neuro_gateway.fusionbrain import Fusionbrain
from core.settings import settings


def get_generate_sd_service() -> list[StableDiffusion]:

    instances = []
    for key in settings.sd_keys:
        instances.append(StableDiffusion(key, settings.path_to_downloads))

    return instances


def get_generate_kad_service() -> list[StableDiffusion]:

    token = ""
    path = "downloads"

    return Kandinsky(token, path)


def get_generate_fb_service() -> list[StableDiffusion]:

    return Fusionbrain(
        settings.fb_api_key,
        settings.fb_secret_key,
        settings.path_to_downloads,
    )
