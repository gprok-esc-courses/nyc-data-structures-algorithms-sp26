

def move(disk, from_pin, to_pin, helper_pin):
    if disk > 0:
        move(disk-1, from_pin, helper_pin, to_pin)
        print(f"Move {disk} from {from_pin} to {to_pin}")
        move(disk-1, helper_pin, to_pin, from_pin)



def hanoi_towers(size):
    disk = size
    move(disk, "A", "C", "B")


hanoi_towers(64)