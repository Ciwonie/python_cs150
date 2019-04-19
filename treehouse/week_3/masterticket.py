SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# create the calculate price function. It takes numberOfTickets and returns price for the amount


def calculate_price(numberOfTickets):
    # create a new constant for the 2 dollar service charge
    # add the service charge to our result
    return (numberOfTickets * TICKET_PRICE) + SERVICE_CHARGE

# run this code continuously until all tickets are sold


while tickets_remaining:

    print("There are {} tickets remaining".format(tickets_remaining))
    userName = input("Please enter your name: ")
    numberOfTickets = input(
        "Hi {}, how many tickets would you like to order? ".format(userName))

    # Expect a ValueError to happen and handle it appropriately...
    try:
        numberOfTickets = int(numberOfTickets)
        # Raise a ValueError if the request is for more ticekts than are available
        if numberOfTickets > tickets_remaining:
            raise ValueError(
                "There are only {} tickets remaining".format(tickets_remaining))

    except ValueError as err:
        # Include the error text in the output
        print("Oh no, we ran into an issue. {}. Please try again".format(err))

    else:
        totalPrice = calculate_price(numberOfTickets)
        print("Total cost: ${}".format(totalPrice))
        proceed = input("Would you like to proceed (Y/N): ")

        if proceed.lower() == "y":
            # TODO: Gether credit card information and process it
            print("SOLD!")
            tickets_remaining -= numberOfTickets
        else:
            print("Thank you, {}".format(userName))

# Notify user that the tickets are sold out
print("Sorry, the tickets are sold out")
