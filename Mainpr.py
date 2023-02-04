import numpy as np
import matplotlib.pyplot as plt

class Box():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bead():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class System():
    def __init__(self, n, r, box):
        self.r = r 
        self.n = n
        self.box = box
    def generation_beads(self):
        self.lst_beads = [Bead(np.random.uniform(-self.box.x + self.r, self.box.x - self.r), np.random.uniform(-self.box.y + self.r, self.box.y - self.r))]
        flg = 0
        reps = 0
        for _ in range(self.n):
            while True: # creation of new bead until satisfies the conditions: 1)stay in box  2) don't intersect with already created beads
                flg = 0 #  condition violation flag           
                angle = np.random.uniform(0, 2 * np.pi)
                bead_x = self.lst_beads[-1].x + 2*self.r * np.cos(angle) 
                bead_y = self.lst_beads[-1].y + 2*self.r * np.sin(angle)
                flg += check_overlap(coor_x=bead_x, coor_y=bead_y, list_of_beads=self.lst_beads, radius=self.r)#check for intersection with other beads
                flg += check_boandaries(coor_x=bead_x, coor_y=bead_y, box=self.box, radius=self.r) # check for being in box
                if flg == 0:
                    self.lst_beads.append(Bead(bead_x,bead_y))
                    reps = 0
                    break
                elif reps > (100 + self.box.x / np.sqrt((2 * self.r))): #checking the possibility of creating a new bead in the given constraints
                    print(f'Sorry, it is not possible to create a chain of more than {len(self.lst_beads)} beads under the given conditions for this iteration')
                    return
                else:
                    reps += 1
                    continue    
def check_boandaries(coor_x, coor_y, box, radius):
    if (abs(coor_x) > (box.x - radius)) or (abs(coor_y) > (box.y - radius)): # check for being in box
        return 1
    else:
        return 0

def check_overlap(coor_x, coor_y, list_of_beads, radius): #check for intersection with other beads
    for i in range(len(list_of_beads)-1):                
        if np.sqrt((coor_x - list_of_beads[i].x) ** 2 + (coor_y - list_of_beads[i].y) ** 2) <= 2*radius:
            return 1
    return 0
    
def show_beads(sys):
    plt.figure(figsize=(5, 5))
    x = [bead.x for bead in sys.lst_beads]
    y = [bead.y for bead in sys.lst_beads]
    plt.plot(x, y, '-*', color="r")
    for i in range(len(sys.lst_beads)):
        circles = plt.Circle((x[i], y[i]), sys.r, color=(0 + i/len(sys.lst_beads), 0 + i/len(sys.lst_beads), 0)) #black end is the beginning 
        plt.gca().add_artist(circles)
    plt.xlim(-sys.box.x, sys.box.x)
    plt.ylim(-sys.box.y, sys.box.y)
    plt.grid()
    plt.show()

def main():
    box = Box(x=10, y=10)
    sys = System(n=40, r=0.7, box=box)
    sys.generation_beads()
    show_beads(sys)    

if __name__ == '__main__':
    main()

