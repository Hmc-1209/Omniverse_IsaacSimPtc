from omni.isaac.examples.base_sample import BaseSample
from omni.isaac.franka.tasks import PickPlace
from omni.isaac.franka.controllers import PickPlaceController


class HelloWorld(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        return

    def setup_scene(self):
        world = self.get_world()
        world.add_task(PickPlace(name="awesome_task"))
        return

    async def setup_post_load(self):
        self._world = self.get_world()

        task_params = self._world.get_task("awesome_task").get_params()
        self._franka = self._world.scene.get_object(task_params["robot_name"]["value"])
        self._cube_name = task_params["cube_name"]["value"]

        self._controller = PickPlaceController(
            name="pick_place_controller",
            gripper=self._franka.gripper,
            robot_articulation=self._franka,
        )

        self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)

        await self._world.play_async()

        return

    async def setup_post_reset(self):
        self._controller.reset()
        await self._world.play_async()
        return

    def physics_step(self, step_size):
        current_observation = self._world.get_observations()

        actions = self._controller.forward(
            picking_position=current_observation[self._cube_name]["position"],
            placing_position=current_observation[self._cube_name]["target_position"],
            current_joint_positions=current_observation[self._franka.name][
                "joint_positions"
            ],
        )
        self._franka.apply_action(actions)

        if self._controller.is_done():
            self._world.pause()

        return
