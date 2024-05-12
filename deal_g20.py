from coupon import Coupon
from constants import *
from course import *

class DEAL_G20(Coupon):

    def __init__(self) -> None:
        self.coupon = "DEAL_G20"
    
    def check_coupon_eligibility(self, program_details):

        final_count = 0

        for course, details in program_details.items():
            course_amount = Coupon.get_coupon_discount(course)
            final_count += details['program_expense']

            if final_count >= 10000:
                return True
        
        return False
    
    def get_discount_rate(self):
        return DEAL_G20_DISCOUNT_RATE

    def get_coupon_name(self):
        return self.coupon