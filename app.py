def print_line_one():
    """Prints 'Line 1' to the console."""
    print("Line 1")
    return True

def print_feature_branch_change():
    """Prints 'Feature branch change' to the console."""
    print("Feature branch change")
    return True

# Execute the conditional check with descriptive functions
if print_line_one() and print_feature_branch_change():
    print("Yes")
else:
    print("No")
