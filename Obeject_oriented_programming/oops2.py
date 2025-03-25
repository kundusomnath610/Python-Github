class Employee:
    company_name = 'Code'
    def work(self): ## Self is always hold odd current object..
        print(self.name,' is working')
    def play(self):
        print(self.name,' is playing')
e1 = Employee()
e1.name = 'AK'
e1.id = 101
e1.work()
e2 = Employee()
e2.name = 'Pk'
e2.id = 102
e2.work()
e2.play()

'''
    1. for instance variable separate copy will be created for each object ..
    2. class level object.
'''