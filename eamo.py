def is_folder_empty(items_in_folder):
    return not items_in_folder

# Example usage:
print(is_folder_empty([]))         # Output: True (because the list is empty)
print(is_folder_empty([1, 2, 3]))  # Output: False (because the list is not empty)
