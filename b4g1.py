from coupon import Coupon
from constants import *
from course import *

class B4G1(Coupon):

    def __init__(self) -> None:
        self.coupon = "B4G1"
    
    def check_coupon_eligibility(self, program_details):

        final_count = 0

        for course, details in program_details.items():
            final_count += details['count']

            if final_count >= 4:
                return True
        
        return False
    
    def get_discount(self, program_details):
        min_amount = 100000
        for course, details in program_details.items():
            course_amt = details['program_expense']/details['count']
            if min_amount > course_amt:
                min_amount = course_amt
        
        return min_amount

    def get_coupon_name(self):
        return self.coupon