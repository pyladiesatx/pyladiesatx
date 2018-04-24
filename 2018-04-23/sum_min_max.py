
def get_sum_value(**kwargs):
    """
    :param kwargs: keywords arguments
    :return: sum of the min or max numbers
    """
    # Check if the kwargs argument are correct
    for key, value in kwargs.iteritems():
        if key not in ["raw_list", "max_value", "size"]:
            raise ValueError("incorrect value.")

    # Get the raw_list and the size for which you want sum
    raw_list = kwargs.get("raw_list", [])
    list_size = kwargs.get("size", 4)
    new_list = []

    # Raise exception if the expected size is greater than the actual list
    if list_size > len(raw_list):
        raise ValueError("The raw list size should be greater than expected list size. "
                         "Expected size {}, Got {}".format(list_size, len(raw_list)))

    # Only get the values which matches the size
    for _ in xrange(0, list_size):
        # Get the sum of max values max_value is True otherwise get the sum of min values
        if kwargs.get("max_value") is True:
            val = max(raw_list)
        else:
            val = min(raw_list)
        new_list.append(val)
        raw_list.remove(val)

    # Return the sum of the list
    print "The list values are", new_list
    return sum(new_list)


# Give the sum of max values
new_list_val = get_sum_value(raw_list=[1, 2, 3, 6, 5], max_value=True, size=4)
print "sum of value is ", new_list_val

print "\n"
# Give the sum of min values
new_list_val = get_sum_value(raw_list=[1, 2, 3, 6, 5], max_value=False, size=4)
print "sum of value is ", new_list_val
