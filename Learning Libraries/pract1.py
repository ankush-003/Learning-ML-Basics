# # number of elements
# n = int(input("Enter number of elements : "))

# # Below line read inputs from user using map() function
# a = list(map(int,input("\nEnter the numbers : ").strip().split()))

# print("\nList is - ", a)

f = lambda x: x*x
print([f(x) for x in range(10)])
