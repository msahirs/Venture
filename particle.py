import numpy as np


class Particle3DoF:
    """
    3 DoF Particle Class. This means only translational states are stored within this class
    
    """
    def __init__(self, mass, connectivity_matrix = None, collision_radius = 0.0001, particle_id = None) -> None:
        
        self.position = np.zeros((3,1))


        self.velocity = np.zeros((3,1))

        self.acceleration = np.zeros((3,1))

        self.mass = mass

        self.forces = np.zeros((3,1))

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

        self.position = vec[0:3,0][...,None]

        self.velocity = vec[3:6,0][...,None]

    def get_state_vec_derivative(self): #Pack individual derivatives of states to vector:
                                      #  [ velocity
                                      #    acceleration]

        return  np.vstack(( self.velocity,
                            self.acceleration))

    def get_vec_pack(self): #Pack individual derivatives of states to vector:
                                      #  [ position
                                      #    velocity
                                      #    acceleration ]
        
        return  np.vstack(( self.position,
                            self.velocity,
                            self.acceleration))

    def set_forces(self,forces): # Sets forces into object array: #  [[force.x]
                                                                 #    [force.y]
                                                                 #    [force.z]]
        self.forces = forces

    def update_accel(self):

         self.acceleration = self.forces / self.mass

    def update_step(self, delta_t, integrator_func): # Integrates particle
        self.update_accel()
        next_state_vec = self.get_state_vec() + delta_t * self.get_state_vec_derivative() # Euler
        # next_state_vec = integrator_func(self.get_state_vec, self.get_state_vec_derivative, delta_t) # Parametric

        self.update_state_vec(next_state_vec)

def test_func():
    particle_a = Particle3DoF(2)
    const_g = np.array([[0,0,-9.80665]]).T
    t_f = 2
    particle_a.position = np.array([[0,0,500]]).T
    steps = 1000000
    dt = t_f/steps
    particle_a.set_forces(const_g*2)
    for i in range(steps):
        
        
        particle_a.update_step(dt, None)

    print("get_state_vec:\n",particle_a.get_state_vec())
