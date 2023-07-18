from omni.isaac.kit import SimulationApp

simulation_app = SimulationApp({"headless": False})

# import omni.ext
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
import numpy as np
import service

# --------------------------------- World settings ---------------------------------
# Setting a world and add a ground for it
world = World()
world.scene.add_default_ground_plane()

# Adding a cube in the world
fancy_cube = world.scene.add(
    DynamicCuboid(
        prim_path="/World/random_cube",
        name="fancy_cube",
        position=np.array([0, 0, 1]),
        scale=np.array([0.1, 0.1, 0.1]),
        color=np.array([0, 0, 1.0]),
    )
)

world.reset()

# Register services object(s) and endpoint(s)
service.register(fc=fancy_cube)
service.service_register_endpoint()

# ------------------------------------------------------------------------------------

while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()
