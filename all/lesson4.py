class RAM:
    def __init__(self):
        self.ram = 8192

    def get_ram(self):
        return self.ram

class CPU:
    def __init__(self):
        super().__init__()
        self.brand = 'Intel'
        self.cores = 4
        self.frequency = 3.4

    def get_cores(self):
        return self.cores

    def get_brand(self):
        return self.brand

class Graphics:
    def __init__(self):
        super().__init__()
        self.memory = 1024

    def get_graph_memory(self):
        return self.memory

class PC(CPU, Graphics, RAM):

    def __init__(self):
        super().__init__()

    def print_info(self):
        print("PC info")
        print(f"RAM: {self.get_ram()} GB")
        print(f"CPU: {self.brand} x {self.cores} cores")
        print(f"GPU: {self.get_graph_memory()} GB")

pc = PC()
pc.print_info()

























# class GrandParent:
#
#     def __init__(self, height=189):
#         self.height = height
#
#     def get_height(self):
#         return self.height
#
# class Parent(GrandParent):
#
#     def __init__(self):
#         super().__init__()
#
# class Child(Parent):
#
#     def __init__(self):
#         super().__init__()
#
#
# joe = Child()
# print(joe.get_height())