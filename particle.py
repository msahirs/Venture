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

        self.state_vec = self.state_vec_pack()

        self.state_vec_derivative = self.state_vec_derivative_pack()


    def state_vec_pack(self): #Pack individual states into overall state vector:
                            #  [ position
                            #    velocity ]
        
        return  np.vstack(( self.position,
                            self.velocity))
    
    def state_vec_unpack(self, integrated_vec): #Unpacks output vector elements into respective :

        self.position = integrated_vec[0:3,0]

        self.velocity = integrated_vec[3:6,0]

    def state_vec_derivative_pack(self): #Pack individual derivatives of states to vector:
                                      #  [ velocity
                                      #    acceleration]
        
        return  np.vstack(( self.velocity,
                            self.acceleration))

    def net_state_vec_pack(self): #Pack individual derivatives of states to vector:
                                      #  [ position
                                      #    velocity
                                      #    acceleration ]
        
        return  np.vstack(( self.position,
                            self.velocity,
                            self.acceleration))

    def set_forces(self,forces): # Sets forces into object array: #  [ force.x
                                                                 #    force.y
                                                                 #    force.z ]
        self.forces = forces

    def update(self, dt): # Integrates particle

        pass
