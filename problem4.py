def search(lst1, element):
    for index, i in enumerate(lst1):  
        if i == element:
            return index 
    return -1  

# Example usage
print(search([1, 2, 3, 4, 5], 5))  # Output: 4
