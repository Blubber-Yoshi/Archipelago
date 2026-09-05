from collections.abc import Sequence

import asyncio

from worlds.AutoWorld import World
from worlds.LauncherComponents import components, Component, Type


class ProgressionOrderWorld(World):
    """
    A client to display the order that locations have been unlocked based on received progression items order.
    """
    # This is needed to allow building the APWorld
    game = "Progression Order"
    hidden = True
    item_name_to_id = {}
    location_name_to_id = {}


def launch_client(*args: Sequence[str]) -> None:
    from CommonClient import get_base_parser, handle_url_arg
    parser = get_base_parser()
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")

    launch_args = handle_url_arg(parser.parse_args(args))

    import colorama
    colorama.just_fix_windows_console()

    from .Client import launch
    asyncio.run(launch(launch_args))
    colorama.deinit()

components.append(Component("Progression Order", None, func=launch_client, component_type=Type.CLIENT, supports_uri=True, game_name=None))
