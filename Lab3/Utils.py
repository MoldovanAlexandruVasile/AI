def rotateY(cube):
    cube[1], cube[2], cube[4], cube[5] = cube[2], cube[4], cube[5], cube[1]
    return cube


def rotateX(cube):
    cube[0], cube[5], cube[3], cube[2] = cube[5], cube[3], cube[2], cube[0]
    return cube


def rotateZ(cube):
    cube[3], cube[4], cube[0], cube[1] = cube[4], cube[0], cube[1], cube[3]
    return cube


def rotate(number, cube):
    no = 0
    while no < number:
        cube = rotateX(cube)
        if no % 8 == 0:
            cube = rotateZ(cube)
        elif no % 8 == 4:
            cube = rotateY(cube)
        no += 1
    return cube


def remove(elem):
    return elem[:2] + elem[3:5]
