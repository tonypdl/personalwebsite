def example_function(a, b):
    if a == b:
        return True
    elif a != b:
        return False
    else:
        return None

result = example_function(10, 20)
print(result)  # This should print False

# Other examples of ligatures:
x = 10
y = 20
z = x <= y  # Less than or equal to
print(z)  # This should print True

arrow_function = lambda x: x * 2  # Arrow function
print(arrow_function(5))  # This should print 10