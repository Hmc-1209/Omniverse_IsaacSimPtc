from omni.isaac.kit import SimulationApp

simulation_app = SimulationApp({"headless": False})

from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
import numpy as np

from omni.services.core import main


world = World()


# main.register_endpoint("get", "/get_cube_position", get_cube_position)
# main.register_endpoint("get", "/get_cube_name", get_cube_name)
# main.register_endpoint("post", "/move_cube_x", move_cube_x)
# main.register_endpoint("post", "/move_cube_y", move_cube_y)
# main.register_endpoint("post", "/move_cube_z", move_cube_z)


# # ------------------------------------------------------------------------------------
# while simulation_app.is_running():
#     world.step(render=True)

# simulation_app.close()
