def main():
    print("=== Order Approval System ===")

    # Inputs
    order_amount = float(input("Enter order amount (TRY): "))
    available_stock = int(input("Enter available stock: "))
    requested_quantity = int(input("Enter requested quantity: "))
    is_member_input = input("Is customer a member? (yes/no): ").strip().lower()

    # Convert member input to boolean
    is_member = is_member_input in ["yes", "y", "e", "evet"]

    # Rejection checks: Invalid quantity or insufficient stock
    if requested_quantity <= 0:
        print("\nOrder Rejected: Invalid quantity requested. Quantity must be greater than 0.")
    elif requested_quantity > available_stock:
        print("\nOrder Rejected: Insufficient stock available.")
    else:
        # Approval logic with discount calculation using logical operator 'and'
        discount = 0.0
        if is_member and order_amount >= 500:
            discount = 0.10
            approval_reason = "Approved: Member customer eligible for 10% discount on order >= 500 TRY."
        elif is_member:
            approval_reason = "Approved: Member customer (Order amount below 500 TRY, no discount applied)."
        else:
            approval_reason = "Approved: Standard customer (No discount applied)."

        final_price = order_amount * (1 - discount)

        # Output for approved orders only
        print(f"\n{approval_reason}")
        print(f"Final Price: {final_price:.2f} TRY")


if __name__ == "__main__":
    main()