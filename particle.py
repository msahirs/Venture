import numpy as np
import Integrators as integrate


class Particle3DoF:
    """
    3 DoF Particle Class. This means only translational states are stored within this class
    
    """
    def __init__(self, mass, init_state = None, connectivity_matrix = None, collision_radius = 0.0001, particle_id = None) -> None:
        
        if init_state == None:
            self.position = np.zeros((3,1))
            self.velocity = np.zeros((3,1))
        
        else:
            self.position = init_state[0:3,0][...,None]
            self.velocity = init_state[3:6,0][...,None]

        self.mass = mass
        self.forces = np.zeros((3,1))
        self.force_list = []
        self.acceleration = np.zeros((3,1))

        self.collision_radius = collision_radius  #[m]
        self.particle_id = particle_id
        self.spawn_time = 0

        self.state_vec = self.get_state_vec()
        self.state_vec_derivative = self.get_state_vec_derivative()
        
    def get_state_vec(self): #Pack individual states into overall state vector:
                            #  [ position
                            #    velocity ]
        
        return  np.vstack(( self.position,
                            self.velocity))
    
    def update_state_vec(self, vec): #Unpacks vector elements into state vector:

        # print(vec)

        self.position = vec[0:3,0][...,None]

        self.velocity = vec[3:6,0][...,None]

    def get_state_vec_derivative(self): #Pack individual derivatives of states to vector:
                                      #  [ velocity
                                      #    acceleration]

        return  np.vstack(( self.velocity,
                            self.acceleration))


    def get_derivative_func(self, t, y):

        return np.sum([f(t,y) for f in self.force_list])


    def get_vec_pack(self): #Pack individual derivatives of states to vector:
                                      #  [ position
                                      #    velocity
                                      #    acceleration ]
        
        return  np.vstack(( self.position,
                            self.velocity,
                            self.acceleration))

    def set_forces(self,forces): # Sets impulse forces into object array: #  [[force.x]
                                                                 #    [force.y]
                                                                 #    [force.z]]
        self.forces = forces

    def set_type_forces(self,force_funcs): # Sets types of forces into object array:
        
        self.force_list = force_funcs

    def update_accel(self,t,y):

        self.forces = np.sum([f(t,y) for f in self.force_list])
        
        self.acceleration = self.forces / self.mass

    def reset_force(self):
        
        self.forces = 0. * self.forces

    def update_step(self, delta_t, integrator_func): # Integrates particle
        
        # next_state_vec = self.get_state_vec() + delta_t * self.get_state_vec_derivative() # Euler
        next_state_vec = integrate.TimeIntegratorOneStep.rkf45_step(self.get_state_vec(),forcing_func, self.spawn_time, delta_t, setAdaptive=False,)
        # next_state_vec = integrate.TimeIntegratorOneStep.euler_step(self.get_state_vec(),forcing_func, self.spawn_time, delta_t)
        # next_state_vec = integrator_func(self.get_state_vec, self.get_state_vec_derivative, delta_t) # Parametric
        
        self.update_state_vec(next_state_vec) #substitute for t+1 state vector
        
        self.spawn_time += delta_t

        # self.reset_force()

class particle6DoF(Particle3DoF):

    def __init__(self, mass, MoI, connectivity_matrix=None, collision_radius=0.0001, particle_id=None) -> None:

        super().__init__(mass, connectivity_matrix, collision_radius, particle_id)
        
        self.MoI = MoI


def forcing_func(t,y):

    rho = 1
    # variance = 1*t**1.4 - t**2
    q = 0.5 * rho * np.abs(y[3:6,0]) * y[3:6,0]

    drag = - q * 1 * 0.1
    
    g = np.array([0,0,-9.80665])
    deriv = np.array((y[3:6,0], g + drag))

    return deriv.reshape(6,1)

def __main__():

    particle_a = Particle3DoF(1)
    
    t_f = 20
    particle_a.position = np.array([[0,0,500]]).T
    steps = 1000
    dt = t_f/steps
    # particle_a.set_type_forces([forcing_func])

    for i in range(steps):
        # print(particle_a.get_state_vec())
        
        particle_a.update_step(dt, None)
        # if i% 100 == 0: 
        #     # print(particle_a.position)
        #     print(i)

    print("get_state_vec:\n",particle_a.get_state_vec())

# cProfile.run("__main__()")

if __name__ == "__main__":
    __main__()


