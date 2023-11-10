#!/usr/bin/python3

  """
    Replace all occurrences of old_element with new_element in a new list.

    Parameters:
    - lst: The input list.
    - old_element: The element to be replaced.
    - new_element: The element to replace old_element.

    Returns:
    A new list with old_element replaced by new_element.
    """

def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
