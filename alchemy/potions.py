from .elements import create_air as air
from .elements import create_earth as earth
from elements import create_fire as fire
from elements import create_water as water


def healing_potion() -> str:
    return f"Healing potion brewed with '{earth()}' and '{air()}'"


def strength_potion() -> str:
    return f"Strength potion brewed with '{fire()}' and '{water()}'"
