class Atom:
    def __init__(self, x, y, z, xvel):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        self.vx = xvel
        self.vy = 0.0
        self.vz = 0.0


def add_ball(atoms, xpos, xvel):
    r = 8
    s = 1.55                                        # 原子間距離のルート2倍
    h = 0.5 * s
    for ix in range(-r, r+1):
        for iy in range(-r, r+1):
            for iz in range(-r, r+1):
                x = ix * s
                y = iy * s
                z = iz * s
                if (x**2 + y**2 + z**2 > r**2):     # 原子を球状に配置するため
                    continue
                x = x + xpos                        # 空間中に原子を配置
                atoms.append(Atom(x, y, z, xvel))   # 斜め方向に原子を配置
                atoms.append(Atom(x, y+h, z+h, xvel))
                atoms.append(Atom(x+h, y, z+h, xvel))
                atoms.append(Atom(x+h, y+h, z, xvel))

def add_one_ball(atoms, xpos, xvel):
    y = 0
    z = 0
    x = xpos
    atoms.append(Atom(x, y, z, xvel))

def save_file(filename, atoms):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("{} atoms\n".format(len(atoms)))
        f.write("1 atom types\n\n")
        f.write("-80.00 80.00 xlo xhi\n")
        f.write("-40.00 40.00 ylo yhi\n")
        f.write("-40.00 40.00 zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
    print("Generated {}".format(filename))


atoms = []

add_ball(atoms, 10, -1)
add_ball(atoms, -10, 1)

save_file("collision.atoms", atoms)
