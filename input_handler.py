from cart import *
from course import *
from pro import *
from deal_g20 import *
from deal_g5 import *
from b4g1 import *
def create_object(class_name, *args, **kwargs):
    # Use globals() to access the class by its name
    dynamic_class = globals().get(class_name)

    if dynamic_class is not None and callable(dynamic_class):
        # Create an object of the specified class with the given arguments and keyword arguments
        new_object = dynamic_class(*args, **kwargs)
        return new_object
    else:
        raise ValueError(f"Class '{class_name}' not found or not callable.")

def input_handler(lines):

    cart_obj = Cart()
    pro_obj = ProSubscription()
    pro_fees = 0
    b4gi_set = False
    # Cheking pro membership first
    possible_pro_line = lines[-2]
    pro_input = possible_pro_line.strip().split(" ")
    if pro_input[0] == "ADD_PRO_MEMBERSHIP":
        pro_obj.set_pro_membership()
        pro_fees = PRO_MEMBERSHIP_FEES
    
    sub_total_set = False

    for line in lines:

        inputs = line.strip().split(" ")

        if inputs[0] == "ADD_PROGRAMME":
            pro_discount = 0
            course = inputs[1]
            count = float(inputs[2])
            #import ipdb;ipdb.set_trace()
            expense = float(Course.get_course_cost(course))
            if pro_obj.is_pro_membership():
                pro_discount = pro_obj.get_pro_discount_amount(course, expense)
            cart_obj.add_program(course, count, expense, pro_discount)
            
        if inputs[0] == "APPLY_COUPON":

            program_details = cart_obj.get_program_details()

            if not sub_total_set:
                cart_obj.set_sub_total(pro_fees)
                sub_total_set = True
            # import ipdb;ipdb.set_trace()
            if cart_obj.get_total_count() >= 4:
                if not b4gi_set:
                    b4gi_obj= B4G1()
                    b4gi_discount = b4gi_obj.get_discount(program_details)
                    cart_obj.set_b4gi_discount(low_course_amount=b4gi_discount, coupon_name=b4gi_obj.get_coupon_name())
                    b4gi_set = True
            else:
                coupon = inputs[1]
                coupon_class = create_object(coupon)
                coupon_discount_rate = coupon_class.get_discount_rate()
                coupon_name = coupon_class.get_coupon_name()
                
                if coupon_class.check_coupon_eligibility(program_details):
                    cart_obj.check_and_set_coupon(coupon_discount_rate, coupon_name)

        if inputs[0] == "PRINT_BILL":
            sub_total = cart_obj.get_sub_total()
            cart_obj.check_for_enrollment_fee_status_and_apply()
            print("SUB_TOTAL ", "{:.2f}".format(sub_total))

            coupon_and_discount = cart_obj.get_discount_amount_and_coupon_name()
            print("COUPON_DISCOUNT ", coupon_and_discount['coupon_name'], " ", "{:.2f}".format(coupon_and_discount['discount_amount']))

            pro_discount = cart_obj.get_pro_discount()
            print("TOTAL_PRO_DISCOUNT ", "{:.2f}".format(pro_discount))

            if pro_obj.is_pro_membership():
                pro_membership_fee = PRO_MEMBERSHIP_FEES
            else:
                pro_membership_fee = 0
            print("PRO_MEMBERSHIP_FEE ", "{:.2f}".format(pro_membership_fee))

            enrollment_fees = cart_obj.get_enrollment_fees()
            print("ENROLLMENT_FEE ", "{:.2f}".format(enrollment_fees))

            total = cart_obj.get_total()
            print("TOTAL ", "{:.2f}".format(total))