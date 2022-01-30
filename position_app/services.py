from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import Coordonne, Position,Location

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_coordonnes_without_cache():
    return list(Coordonne.objects.all())


def get_coordonnes_with_cache():
    if 'coordonnes' in cache:
        coordonnes = cache.get('coordonnes')
    else:
        coordonnes = list(Coordonne.objects.all())
        cache.set('coordonnes', coordonnes, timeout=CACHE_TTL)
    return coordonnes


def get_positions_without_cache():
    return list(Location.nodes.all())

def get_positions_with_cache():
    if 'positions' in cache:
        positions = cache.get('positions')
    else:
        positions = list(Location.nodes.all())
        cache.set('positions', positions, timeout=CACHE_TTL)
    return positions
