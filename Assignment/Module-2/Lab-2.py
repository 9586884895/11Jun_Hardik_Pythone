#Write a Python program to access elements at different index positions.

My_list=['Hardik','Ankita','Bhagirath','Avon','Rajnikant']

print("First index",My_list[0])
print("Element at index 0:", My_list[0])     # First element
print("Element at index 2:", My_list[2])     # Third element
print("Element at index -1:", My_list[-1])   # Last element (using negative index)
print("Element at index -3:", My_list[-3])   # Third from the end

for i in range(len(My_list)):
    print(f"index{i}:{My_list[i]}")