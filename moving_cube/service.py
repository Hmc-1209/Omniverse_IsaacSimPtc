from omni.services.core import main


# Register objects
def register(fc):
    global fancy_cube
    fancy_cube = fc


def cube_pos():
    position, _ = fancy_cube.get_world_pose()
    return position


def get_cube_position():
    return "The cube's position is: " + str(cube_pos(fancy_cube))


def get_cube_name():
    return "The cube's name is: " + fancy_cube.name


def move_cube_x():
    try:
        pos = cube_pos()
        pos[0] += 0.1
        fancy_cube.set_world_pose(pos)
    except:
        return "Movement failed!"
    return "Movement success!"


def move_cube_y():
    try:
        pos = cube_pos()
        pos[1] += 0.1
        fancy_cube.set_world_pose(pos)
    except:
        return "Movement failed!"
    return "Movement success!"


def move_cube_z():
    try:
        pos = cube_pos()
        pos[2] += 2
        fancy_cube.set_world_pose(pos)
    except:
        return "Movement failed!"
    return "Movement success!"


# Register endpoints
def service_register_endpoint():
    main.register_endpoint("get", "/get_cube_position", get_cube_position)
    main.register_endpoint("get", "/get_cube_name", get_cube_name)
    main.register_endpoint("post", "/move_cube_x", move_cube_x)
    main.register_endpoint("post", "/move_cube_y", move_cube_y)
    main.register_endpoint("post", "/move_cube_z", move_cube_z)
