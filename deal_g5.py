from coupon import Coupon
from constants import *

class DEAL_G5(Coupon):

    def __init__(self) -> None:
        self.coupon = "DEAL_G5"
    
    def check_coupon_eligibility(self, program_details):

        final_count = 0

        for program, details in program_details.items():
            final_count += details['count']
        
        if final_count >= 2:
            return True
        
        return False
    
    def get_discount_rate(self):
        return DEAL_G5_DISCOUNT_RATE

    def get_coupon_name(self):
        return self.coupon