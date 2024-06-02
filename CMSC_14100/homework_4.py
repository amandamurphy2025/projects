"""
CMSC 14100, Autumn 2022
Homework #4

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import math

# Exercise 1
def prefix_distance(u, v):
    """
    Computes the prefix distance of u and v. The prefix distance is the total
    number of characters that do not belong to the longest common prefix shared
    by u and v.

    For example, the prefix distance of "morning" and "mourning" is 11, since
    the longest common prefix of the two strings is "mo".

    Input:
        u (str): first input string
        v (str): second input string

    Output: prefix distance of u and v (int)
    """

    count_lst = []

    for n in range(0, len(max(u, v))):
        if u[0:n + 1] == v[0:n + 1]:
            count_lst.append(1)

    u_leftover = len(u) - sum(count_lst)

    v_leftover = len(v) - sum(count_lst)

    result = u_leftover + v_leftover

    return result

# Exercise 2
def suffix_distance(u, v):
    """
    Computes the suffix distance of u and v.  The suffix distance is the total
    number of characters that do not belong to the longest common suffix shared
    by u and v

    For example, the suffix distance of "tomato" and "potato" is 6, since the
    longest common suffix of the two strings is "ato"

    Input:
        u (str): first input string
        v (str): second input string

    Output: suffix distance of u and v (int)
    """

    count_lst = []

    reverse_u = u[len(u)::-1]

    reverse_v = v[len(v)::-1]

    for n in range(0, len(max(u, v))):
        if reverse_u[0:n + 1] == reverse_v[0:n + 1]:
            count_lst.append(1)
  
    u_leftover = len(u) - sum(count_lst)

    v_leftover = len(v) - sum(count_lst)

    result = u_leftover + v_leftover

    return result

# Exercise 3
def total_badness(text, width):
    """
    Computes the total badness of a string of given text when it is split into
    lines of a given width. Badness is the sum of the cubes of the trailing
    spaces of each line.

    Inputs:
        text (str): string of any length and characters
        width (int): maximum length of each line

    Output: badness of the given text having been split into lines (int)
    """

    split_txt = text.split()

    list_of_lines = []

    adding_list = ""

    for idx, n in enumerate(split_txt):
        if len(n) + len(adding_list) <= width:
            adding_list = adding_list + n + " "
        elif len(adding_list) != 0:
            adding_list = adding_list[:-1]
            list_of_lines.append(adding_list)
            adding_list = n + " "
        elif len(adding_list) == 0:
            adding_list = n + " "
    adding_list = adding_list[:-1]
    list_of_lines.append(adding_list)

    for idx, n in enumerate(list_of_lines):
        dif = width - len(n)
        if dif > 0:
            list_of_lines[idx] = n + ("_" * dif)
        if dif < 0:
            list_of_lines[idx] = n + ("_" * abs(dif))

    list_of_blanks = []

    for idx, n in enumerate(list_of_lines):
        blanks = n.count("_")
        list_of_blanks.append(blanks)

    list_of_blanks.remove(list_of_blanks[-1])

    for idx, n in enumerate(list_of_blanks):
        list_of_blanks[idx] = n * n * n

    return sum(list_of_blanks)

# Exercise 4
def split_lines(text, width):
    """
    Splits a given text into lines that have a length that is at most the given
    width where no words are broken between lines

    Input:
        text (str): string of any length and characters
        width (int): maximum length of each line

    Output: list of lines split so that no line length exceeds the width (str)
    """

    split_txt = text.split()

    list_of_lines = []

    adding_list = ""

    for _, n in enumerate(split_txt):
        if len(n) + len(adding_list) <= width:
            adding_list = adding_list + n + " "
        elif len(adding_list) != 0:
            adding_list = adding_list[:-1]
            list_of_lines.append(adding_list)
            adding_list = n + " "
        elif len(adding_list) == 0:
            adding_list = n + " "
    adding_list = adding_list[:-1]
    list_of_lines.append(adding_list)

    return list_of_lines

# Exercise 5
def arrange_lines(text, width, blanks_visible=False):
    """
    Produces a single string of a given text broken into lines that have a
    length that is at most the given width.

    If the flag is any value other than False (which is its default),
    the trailing space (the number of spaces a line has left to reach the given
    width) is shown by "_"

    Input:
        text (str): string of any length and characters
        width (int): maximum length of each line
        blanks_visible: optional flag that shows trailing spaces (bool)

    Output: single string of text split into lines (str)
    """

    split_txt = text.split()

    list_of_lines = []

    adding_list = ""

    for idx, n in enumerate(split_txt):
        if len(n) + len(adding_list) <= width:
            adding_list = adding_list + n + " "
        elif len(adding_list) != 0:
            adding_list = adding_list[:-1]
            list_of_lines.append(adding_list)
            adding_list = n + " "
        elif len(adding_list) == 0:
            adding_list = n + " "
    adding_list = adding_list[:-1]
    list_of_lines.append(adding_list)

    if blanks_visible == True:
        for idx, n in enumerate(list_of_lines):
            dif = width - len(n)
            list_of_lines[idx] = n + ("_" * dif)

    list_of_lines = "\n".join(list_of_lines)

    return list_of_lines

# Exercise 6
def optimal_width(text, min_width=0, max_width=80):
    """
    Finds the optimal line width for a given text to be split to between given
    bounds (inclusive).  The optimal width is the width which results in the
    minimum badness.  Badness is the sum of the cubes of the trailing spaces
    of each line.

    Input:
        text (str): string of any length and characters
        min_width (int): default to 0. Lower bound of widths being tested
        max_width (int): default to 80. Upper bound of widths being tested

    Output: the optimal width for the given text to be split into lines of (int)
    """

    list_of_bad = []

    for width in range(min_width, max_width + 1):
        list_of_bad.append(total_badness(text, width))

    return (min_width + list_of_bad.index(min(list_of_bad)))