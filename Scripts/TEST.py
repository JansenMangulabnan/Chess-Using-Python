class Test:
    def __init__(self, dict_shi):
        self.dict_shi = dict_shi
    
    def change(self):
        self.dict_shi["nigga"] = None

dict_shi ={
    "bruh": None
}

test = Test(dict_shi)
test.change()

print(dict_shi)