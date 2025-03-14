class People(object):
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.full_name=fname + " " + lname
    @classmethod
    def from_full_name(cls,name,age):
        if " " not in name:
            raise ValueError
        fname,lname=name.split(" ",2)
        return cls(fname,lname,age)
    def greet(self):
        print("my fullname is",self.full_name)    
c=People("victor","kyalo",24)
v=People.from_full_name("mbithi torvic",24)
c.greet()
v.greet()

