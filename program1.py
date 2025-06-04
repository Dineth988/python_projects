

class Employee:

    def __init__(self, name, emp_id, base_sal):
        self.name = name
        self.emp_id = emp_id
        self.base_sal = base_sal
    
    def cal_monthly_sal(self):
        self.base_sal + self.base_sal

class part_time_emp(Employee):
    
    def __init__(self, name, emp_id, base_sal, hours, hrate):
        super().__init__(name, emp_id, base_sal)
        self.hours =hours
        self.hrate = hrate

class full_emp(Employee):
    
    def __init__(self, name, emp_id, base_sal, bonus):
        super().__init__(name, emp_id, base_sal)
        self.bonus = bonus
    
    def cal_monthly_sal(self):
        self.base_sal + self.bonus


dic = {
    "k1" : "dineth",
    "k2" : "hari"
}

for value, key in dic.items():
    print(f"{key} : {value}")
