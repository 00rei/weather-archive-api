from src.api.city import router as city_router
from src.api.weather import router as weather_router

all_routers = [
    city_router,
    weather_router
]