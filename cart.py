
from constants import *

class Cart:

    def __init__(self):
        self.sub_total = 0
        self.coupon_discount = 0
        self.coupon_name = 'NONE'
        self.programs = {}
        self.total_program_count = 0
        self.pro_discount = 0
        self.total = 0
        self.enrollment_fees = 0

    
    def add_program(self, program, count, expense, pro_discount):

        self.total_program_count += count
        expense = round(expense - pro_discount, 2)
        program_expense = round(count * expense, 2)
        self.programs[program] = {'count' : count, 
                                  'program_expense' : program_expense
                                  }
        self.pro_discount += pro_discount * count
    
    def set_sub_total(self, pro_fees):

        for program, program_count_and_total_expense in self.programs.items():
            self.sub_total += round(program_count_and_total_expense['program_expense'],2)

        self.sub_total += pro_fees 
        
    
    def get_sub_total(self):
        return self.sub_total

    def get_discount_amount_and_coupon_name(self):
        return {'discount_amount' : self.coupon_discount, 'coupon_name': self.coupon_name}

    def check_and_set_coupon(self, coupon_discount_rate, coupon_name):
        new_discount_amount = round(((self.sub_total * coupon_discount_rate)/100),2)
        if new_discount_amount > self.coupon_discount:
            self.coupon_discount = new_discount_amount
            self.coupon_name = coupon_name
    
    def set_b4gi_discount(self, low_course_amount, coupon_name):
        self.coupon_discount = low_course_amount
        self.coupon_name = coupon_name
    
    def check_for_enrollment_fee_status_and_apply(self):
        amount_to_check = self.sub_total - self.coupon_discount
        if amount_to_check < MINIMUM_AMOUNT_FOR_ENROLLMENT_FEES:
            self.enrollment_fees = ENROLLMENT_FEES
    
    def get_pro_discount(self):
        return self.pro_discount

    def get_enrollment_fees(self):
        return self.enrollment_fees

    def get_total(self):
        return self.sub_total + self.enrollment_fees - self.coupon_discount

    def get_program_details(self):
        return self.programs
    
    def get_total_count(self):
        return self.total_program_count




