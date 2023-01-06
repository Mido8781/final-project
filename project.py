buses = {
    'Bus1': 'New York',
    'Bus2': 'Boston',
    'Bus3': 'Washington DC',
    'Bus4': 'Philadelphia'
}

seats = [True, True, False, True, False, True]  

 
def check_availability(seats): 


    for seat in seats: 

        
        if seat == True: 

            
            print('Seat is available') 

        else: 

            
            print('Seat is not available')  

    
def book_seat(seats):  

    
    for i in range(len(seats)):  

          
        if seats[i] == True:  

            
            seats[i] = False  

            
            print('Seat booked successfully. Your seat number is {}'.format(i))  

            break    

        else:    

            print('All seats are booked!')    

                           
if seats == 'main':     

    print('Welcome to Bus Reservation System')     

    while True:     

        print('\nPlease select an option below')     

        print('1. Check Availability \n2. Book Seat \n3. Exit')     

        choice = int(input())     

        if choice == 1:     

            check_availability(seats)     

        elif choice == 2:     

            book_seat(seats)  
        elif choice == 3:  
           break