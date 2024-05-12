class ProSubscription:

    def __init__(self):
        self.pro_membership_cost = 200
        self.pro_membership = False

    def set_pro_membership(self):
        self.pro_membership = True
    
    def is_pro_membership(self):
        return self.pro_membership
    
    def get_pro_membership_discount(self, course):
        if course == "DIPLOMA":
            return 1
        if course == "CERTIFICATION":
            return 2
        if course == "DEGREE":
            return 3
    
    def get_pro_discount_amount(self, course, amount):
        discount_rate = self.get_pro_membership_discount(course)
        return round((amount * discount_rate)/100, 2)
    

    