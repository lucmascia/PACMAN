from spinn_machine.virtual_machine import VirtualMachine

def shortest_mesh_path_length(source_x, source_y, destination_x, destination_y):
    """Get the length of a shortest path from source to destination without
    using wrap-around links.

    Parameters
    ----------
    source : (x, y)
    destination : (x, y)

    Returns
    -------
    int
    """
    x_delta = destination_x - source_x
    y_delta = destination_y - source_y

    return max(x_delta, y_delta) - min(x_delta, y_delta)


def least_turns(source_x, source_y, destination_x, destination_y):
    if source_x == destination_x and source_x == destination_x:
        return 0
    x_delta = destination_x - source_x
    y_delta = destination_y - source_y
    if x_delta == y_delta:
        return 1
    else:
        return 2



def _check_east(source_x, destination_x, y, machine):
    while source_x < destination_x:
        if not machine.is_link_at(source_x, y, 0):
            return False
        source_x += 1
    return True

def _check_west(source_x, destination_x, y, machine):
    while source_x > destination_x:
        if not machine.is_link_at(source_x, y, 3):
            return False
        source_x -= 1
    return True

def _check_north(x, source_y, destination_y, y, machine):
    while source_y < destination_y:
        if not machine.is_link_at(x, source_y, 2):
            return False
        source_y += 1
    return True

def _check_south(x, source_y, destination_y, y, machine):
    while source_y > destination_y:
        if not machine.is_link_at(x, source_y, 5):
            return False
        source_y -= 1
    return True

def _check_north_east(source_x, source_y, steps, machine):
    for i in range(steps):
        if not machine.is_link_at(source_x + i, source_y + i, 1):
            return False
    return True

def _check_south_west(source_x, source_y, steps, machine):
    for i in range(steps):
        if not machine.is_link_at(source_x - i, source_y - i, 4):
            return False
    return True

def is_directly_reachable(source_x, source_y, destination_x, destination_y, machine):
    if source_x == destination_x and source_y == destination_y:
        return True
    x_delta = destination_x - source_x
    y_delta = destination_y - source_y
    if x_delta == 0:
        if y_delta < 0:
            return _check_south(source_x, destination_x, destination_y, machine)
        else:
            return _check_north(source_x, destination_x, destination_y, machine)
    if y_delta == 0:
        if x_delta < 0:
            return _check_west(source_x, destination_x, source_y, machine)
        else:
            return _check_east(source_x, destination_x, source_y, machine)
    if x_delta == y_delta:
        if x_delta < 0:
            return _check_south_west(source_x, source_y, x_delta, machine)
        else:
            return _check_north_east(source_x, source_y, x_delta, machine)
    return False


if __name__ == '__main__':
    down_chips = {(1, 1)}
    machine = VirtualMachine(8, 8, down_chips=down_chips)
    print(is_directly_reachable(0, 0, 2, 2, machine))
    #print(route(0, 0, 2, 2))
