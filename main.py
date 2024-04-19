from product import Product
from cart import Cart
import streamlit as st


# Function to Display product details
def add_to_cart(product, quantity):
    cart.add_item(product, quantity)
    st.success(f"{quantity} {product.name} added successfully")


# Function to Display product details
def show_cart():
    st.header("Your Cart")
    for item in cart.items:
        st.write(f"{item['quantity']} * {item['product'].name} - {item['product'].price}")

    total_price = cart.calculate_total_price()
    if cart.free_delivery():
        st.write(f"Total Price: {total_price}(free delivery)")
    else:
        st.write(f"Total price: {total_price} (+ 50 Delivery charge if total < 1000)")

    st.write(f"Tax(18%):{cart.tex()}")
    st.write(f"Final Price: {cart.final_price(): .2f}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.title("Online Shopping E-commerce shop system")

    cart = Cart()

    # Adding Products
    products = [
        Product("Laptop", 900),
        Product("Mobile", 50),
        Product("Mouse", 20),
        Product("Keyboard", 50)
    ]

    st.header("Products")
    for product in products:
        col1, col2 = st.columns([1, 3])

        quantity = col1.number_input(f"Quantity for {product.name}", min_value=0, step=1, value=0)
        if quantity > 0:
            add_to_cart(product, quantity)
        with col2:
            st.write(f"!!{product.name} {product.price}")

    # Display Cart
    show_cart()

