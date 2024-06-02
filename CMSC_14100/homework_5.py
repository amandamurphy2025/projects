"""
CMSC 14100, Autumn 2022
Homework #5

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

# A constant for the color black
BLACK = (0, 0, 0)

def make_grey(row):
    """
    This is a helper function for create_greyscale.
    Takes a row (list) of pixels (tuples) and makes a new row that is the
    weighted average greyscale of the original row

    Input:
        row (list of tuples): a list of tuples with three values (int) each

    Output:
        row_in_grey (list): a list of tuples with three of the same value (int)
    """

    row_in_grey = []

    for r, g, b in row:
        r = 77 * r
        g = 150 * g
        b = 29 * b
        almost_grey_pixel = (r, g, b)
        grey = (sum(almost_grey_pixel) // 256)
        grey_pixel = (grey, grey, grey)
        row_in_grey.append(grey_pixel)

    return row_in_grey

def create_greyscale(image):
    """
    This takes a colorful image and makes it into a greyscale version using
    the weighted average of the RGB Values.

    Input:
        image (list of lists of tuples): List of list of tuples of three
        values (int) representing the RGB values of the pixel

    Output:
        greyscale (list of lists of tuples): image but greyscale
    """

    greyscale = []

    for row in image:
        greyscale.append(make_grey(row))

    return greyscale

def image_to_locations(image):
    """
    helper for exercise 4

    Input:
        image (list of lists of tuples): List of list of tuples of three
        values (int) representing the RGB values of the pixel

    Output:
        row_loc (list of tuples): list of tuples with two values (int)
        representing the column and row position of the corresponiding pixel
    """

    row_loc = []

    for idx, row in enumerate(image):
        for idx_pix, _ in enumerate(row):
            t = (idx, idx_pix)
            row_loc.append(t)

    return row_loc

def find_region_locations(image, loc, radius):
    """
    Finds the region of locations around a specified pixel location.

    Input:
        image (list of lists of tuples): image with multiple RBG values
        loc (tuple): location (column and row) to find region around
        radius (int): how many pixels from loc to assess region.  measures how
        many units to right, left, up, and down to assess, and fills in corners
        so the region is a perfect square.

    Output:
        region (list of tuples): locations around loc within the radius
    """

    row_loc = []

    for idx, row in enumerate(image):
        for idx_pix, _ in enumerate(row):
            t = (idx, idx_pix)
            row_loc.append(t)

    region = []

    for c, r in row_loc:
        if (((loc[0] - radius) <= c <= (loc[0] + radius)) and
            ((loc[1] - radius) <= r <= (loc[1]+radius))):
            region.append((c, r))

    return region

def blackout_region(image, loc, radius):
    """
    Finds the region of locations around a specified pixel location and makes
    every pixel in that region black.  This changes the input image.

    Input:
        image (list of lists of tuples): List of list of tuples of three
        values (int) representing the RGB values of the pixel
        loc (tuple): location (column and row, both int) to find region around
        radius (int): how far from loc to assess region.  measures how many
        units to right, left, up, and down to assess, and fills in corners so
        the region is a perfect square

    Output:
        Modifies the image that is inputed so that all the pixels in the region
        are black.
Instructor
| 11/16 at 7:02 pm
Grading comment:
[Code Quality] Be sure to specify None here

    """

    region = find_region_locations(image, loc, radius)

    for c, r in region:
        image[c][r] = (0, 0, 0)

def average(row):
    """
    This is a helper for blur_image.
    Finds the average of each variable in a list of tuples and makes a new tuple
    witht three values (int) that are each the average of each respective
    variable

    Input:
        row (list of tuples): list of tuples with different RGB values (int)

    Output:
        blur_pixel (tuple): tuple with three values that are the average of each
        variable (int) of all tuples from row
    """

    r_avg = []
    g_avg = []
    b_avg = []

    for r, g, b in row:
        r_avg.append(r)
        g_avg.append(g)
        b_avg.append(b)

    r_len = len(r_avg)
    r_avg = sum(r_avg)
    r_avg = r_avg // r_len

    g_len = len(g_avg)
    g_avg = sum(g_avg)
    g_avg = g_avg // g_len

    b_len = len(b_avg)
    b_avg = sum(b_avg)
    b_avg = b_avg // b_len

    blur_pixel = (r_avg, g_avg, b_avg)

    return blur_pixel

def blur_image(image, radius):
    """
    Computes new image where each pixel from image is blurred using the region
    from the specified radius.

    Input:
        image (list of lists of tuples): List of list of tuples of three
        values (int) representing the RGB values of the pixel
        radius (int): how far from loc to assess region.  measures how many
        units to right, left, up, and down to assess, and fills in corners so
        the region is a perfect square

    Output:
        blur (list of lists of tuples): new image with each pixel from image
        blurred.  Each tuple has three values (int)
    """

    locations = image_to_locations(image)

    region = []

    for loc in locations:
        row_region = find_region_locations(image, loc, radius)
        region.append(row_region)

    image_region = []
    pixel_region = []

    for row in region:
        pixel_region = []
        for c, r in row:
            pixel_region.append(image[c][r])
        image_region.append(pixel_region)

    blurred_image = []

    for row in image_region:
        blurred_image.append(average(row))

    L = len(image[0])
    blur = [blurred_image[n:n + L] for n in range(0, len(blurred_image), L)]

    return blur