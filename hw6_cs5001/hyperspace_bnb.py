"""
Kangning Li
CS 5001 Spring 2024
hyperspace_bnb.py
"""

def load_travelers(travelers_file_name: str) -> list[list[str]]:
    """
    Function -- load_travelers
        This function load the .txt file by the input string file name
        return a list of string list (matrix) to store the data
    Parameter:
        travelers_file_name -- string indicate the .txt file
    Return a matrix to store the data
    """
    try:
        name, id, credit = [], [], []

        # read and construct the matrix to store travel info
        with open(travelers_file_name, 'r') as file:
            for line in file:
                name.append(line.rstrip().split('@')[0])
                id.append(line.rstrip().split('@')[1])
                credit.append(line.rstrip().split('@')[2])
        
        return [name, id, credit]

    except FileNotFoundError as e:
        print(f"Error: {e}")

def process_requests(travelers: list[list[str]], request_file_name: str):
    """
    Function -- process_requests
        This function request file contains a booking request according
        to the schedule in request_file_name, if booking successful
        it orchestrate the reservation for our alien and update a file
        named booking.txt, if already booked or short of credits,
        the file should not be modified.
    Parameter:
        travelers -- a matrix contains travelers data
        request_file_name -- file containing order details
    """
    try:
        with open(request_file_name, 'r') as file:
            booked_week = []

            for line in file:
                # import current line to handle
                booking_id = line.split()[0]
                requested_week = line.split()[1]
                traveler_idx = travelers[1].index(booking_id)
                remain_credit = int(travelers[2][traveler_idx])
                
                # make sure the request is valid
                if requested_week in booked_week:
                    continue
                if remain_credit < 500:
                    continue

                # take the request
                booked_week.append(requested_week)
                remain_credit -= 500
                travelers[2][traveler_idx] = str(remain_credit)
                
                # register for the request
                id = travelers[1][traveler_idx]
                name = travelers[0][traveler_idx]
                book_order(requested_week, id, name)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")

def book_order(week: str, id: str, name: str):
    """
    Function -- book_order
        This function write a new line in the bookings.txt
    Parameters:
        week -- target week to book
        id -- the id of the customer
        name -- the name of the customer
    """
    with open("bookings.txt", 'a') as file:
        new_line = week + " - " + id + " - " + name + "\n"
        file.write(new_line)

def main():
    process_requests(load_travelers("travelers.txt"), "requests.txt")

if __name__ == "__main__":
    main()
