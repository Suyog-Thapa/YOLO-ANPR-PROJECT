def get_car(license_plate, vehicle_track_ids):
    """
    Retrieve the vehicle coordinates and ID based on the
    license plate coordinates.

    Args:
        license_plate (tuple):
            (x1, y1, x2, y2, score, class_id)

        vehicle_track_ids (list):
            List of tracked vehicles:
            [xcar1, ycar1, xcar2, ycar2, car_id]

    Returns:
        tuple:
            (xcar1, ycar1, xcar2, ycar2, car_id)
            or (0, 0, 0, 0, -1) if no matching car is found.
    """

    x1, y1, x2, y2, score, class_id = license_plate

    found = False
    for j in range(len(vehicle_track_ids)):
        xcar1, ycar1, xcar2, ycar2, car_id = vehicle_track_ids[j]

        # Check if the license plate is inside the vehicle bounding box
        if (x1 > xcar1 and
            y1 > ycar1 and
            x2 < xcar2 and
            y2 < ycar2):

            car_indx = j
            found = True
            break

    if found:
        return vehicle_track_ids[car_indx]

    return 0, 0, 0, 0, -1
    