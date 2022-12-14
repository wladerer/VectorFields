import plotly.graph_objects as go
import pandas as pd
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
        '''
        Skips lines that contain # and reads the rest of the lines into a pandas dataframe.
        Headers are u,v,w,x,y,z
        '''
        assert isinstance(self.data, str), "data must be a file"
        #check if file exists
        try:
            with open(self.data, 'r') as f:
                #skip the first seven lines
                for i in range(7):
                    next(f)
                #read 100 lines into a pandas dataframe
                df = pd.read_csv(f, sep='\s+', nrows=100, header=None, names=['u','v','w','x','y','z'])
                #convert the dataframe into a numpy array
                data = df.to_numpy()
                #return the numpy array into x,y,z,u,v,w components
                x = data[:,3]/3
                y = data[:,4]/3
                z = data[:,5]/3
                u = data[:,0]
                v = data[:,1]
                w = data[:,2]
                return x,y,z,u,v,w

        except FileNotFoundError:
            print("File not found")
            return None

    def plot3dfield(self):

        X, Y, Z = np.meshgrid(self.x, self.y, self.z)
        U =self.u
        V =self.v
        W =self.w

        #plot vector field
        fig = go.Figure(data=go.Cone(x=X.flatten(), y=Y.flatten(), z=Z.flatten(),
                                     u=U.flatten(), v=V.flatten(), w=W.flatten()))
        fig.show()

