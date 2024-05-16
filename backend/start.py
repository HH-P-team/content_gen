import uvicorn

from commons.config import get_settings


settings = get_settings()

if __name__ == '__main__':

    uvicorn.run(
        'app.main:app',
        host="0.0.0.0",
        port=settings.api_port,
        reload=True,
        loop='uvloop',
    )