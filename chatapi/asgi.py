import os

from channels.routing import URLRouter, ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator  # new
from django.core.asgi import get_asgi_application
from chat import routing  # new
from chatapi.middleware import TokenAuthMiddleware

# from .tokenauth_middleware import TokenAuthMiddleware  # new

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapi.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(  # new
        TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)))
})
