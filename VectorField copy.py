import plotly.graph_objects as go
import numpy as np


class VectorField:

    def __init__(self, data):
        
        self.data = data
        self.x , self.y, self.z, self.u, self.v, self.w = self.get_vfield()

    def get_vfield(self):


        #if data is a numpy array, return the numpy array into x,y,z,u,v,w components
        if isinstance(self.data, np.ndarray):
            x = self.data[:,0]
            y = self.data[:,1]
            z = self.data[:,2]
            u = self.data[:,3]
            v = self.data[:,4]
            w = self.data[:,5]
            return x,y,z,u,v,w
        #if data is string, read the file and return the numpy array into x,y,z,u,v,w components
        elif isinstance(self.data, str):
            
            return self.field_from_file()
        
        #if data is None, return a random vector field
        elif self.data is None:
            x = np.linspace(-1, 1, 10)
            y = np.linspace(-1, 1, 10)
            z = np.linspace(-1, 1, 10)
            u = np.random.rand(10, 10, 10)
            v = np.random.rand(10, 10, 10)
            w = np.random.rand(10, 10, 10)
            return x,y,z,u,v,w

        else:
            raise TypeError("data must be a numpy array or a string")
        

    def field_from_file(self):

        assert isinstance(self.data, str), "data must be a file"
        #check if file exists
        try:
            with open(self.data, 'r') as f:
                
            #read data line by line to save memory
                data = []
                for line in f:
                    #skip the first seven lines and save each row as a separate numpy array
                    if line.startswith('#'):
                        continue
                    else:
                        data.append(np.array(line.split(), dtype=np.float32))
                #convert the list of numpy arrays into a single numpy array
                data = np.array(data)
                #return the numpy array into x,y,z,u,v,w components
                u = data[:,0]
                v = data[:,1]
                w = data[:,2]
                x = data[:,3]
                y = data[:,4]
                z = data[:,5]
                return x,y,z,u,v,w

        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))

    def plot3dfield(self):

        X, Y, Z = np.meshgrid(self.x, self.y, self.z)
        U =self.u
        V =self.v
        W =self.w

        #plot vector field
        fig = go.Figure(data=go.Cone(x=X.flatten(), y=Y.flatten(), z=Z.flatten(),
                                     u=U.flatten(), v=V.flatten(), w=W.flatten()))
        fig.show()

