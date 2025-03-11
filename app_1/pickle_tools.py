import pickle


class PickleTools:
    """
    ############### Example ###############
    
    p = PickleTools('/home/mohsen/Desktop/x.pkl')
    data = ['mohsen', 'ali', 'hassan']
    
    p.dump(data)
    x = p.load()
    
    print(x)
    #######################################
    """
    def __init__(self, file_path):
        self.file_path = file_path
        
    def dump(self, data):
        with open(self.file_path, 'wb') as file:
            pickle.dump(data, file)
            
    def load(self):
        with open(self.file_path, 'rb') as file:
            data = pickle.load(file)
        return data