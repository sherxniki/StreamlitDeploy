import streamlit as st

def largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")
    
    st.write("Enter three numbers:")
    a = st.number_input("First number:")
    b = st.number_input("Second number:")
    c = st.number_input("Third number:")
    
    if st.button("Find Largest"):
        result = largest_number(a, b, c)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
