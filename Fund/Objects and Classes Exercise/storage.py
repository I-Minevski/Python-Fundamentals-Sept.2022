class Storage:
    storage=[]
    
    def __init__(self, capacity):
        self.capacity=capacity
        
    def add_product(self, product: str):
        if len(Storage.storage)<self.capacity:
            Storage.storage.append(product)
    
    def get_products(self):
        return Storage.storage
    
    
strg=Storage(4)
strg.add_product("apple")
strg.add_product("banana")
strg.add_product("potato")
strg.add_product("tomato")
strg.add_product("bread")
print(strg.get_products())
