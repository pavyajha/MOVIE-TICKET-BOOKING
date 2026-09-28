
print("MOVIE TICKET BOOKING SYSTEM")


print("\nAvailable Movies:")
print("1. DHURANDHAR")
print("2. SPIDERMAN")
print("3. GODZILLA")

movie_choice =int (input("\nEnter your movie choice: "))

if movie_choice == 1:
    movie = "DHURANDHAR"
elif movie_choice == 2:
    movie = "SPIDERMAN"
elif movie_choice == 3:
    movie = "GODZILLA"
else:
    print("SORRY, THIS MOVIE IS NOT AVAILABLE")
    exit()

print("\nAVAILABLE SHOW TIMINGS:")
print("1. 11:30 AM")
print("2. 4:00 PM")
print("3. 10:00 PM")

time_choice = int(input("\nEnter your show choice: "))

if time_choice == 1:
    show_time = "11:30 AM"
elif time_choice == 2:
    show_time = "4:00 PM"
elif time_choice == 3:
    show_time = "10:30 PM"
else:
    print("Sorry, there are no shows available for this time.")
    exit()

tickets = int(input("\nEnter number of tickets: "))

price = 250
total = tickets*price

print("\n========== BOOKING SUMMARY ==========")
print("Movie:", movie)
print("Show Time:", show_time)
print("Number of Tickets:", tickets)
print("Ticket Price: Rs.", price)
print("Total Amount: Rs.", total)

print("\nBooking confirmed!")
print("""Thank you for using Movie Ticket Booking System!
                         HAVE A NICE DAY!!!""")
