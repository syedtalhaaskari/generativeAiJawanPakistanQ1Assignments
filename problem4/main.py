"""
Problem 4:
Design a hotel room managment system

Requirement:
1. I should be able to add hotel info i.e name and address
2. I should be able to add new room info i.e name, num_of_beds, fare_per_day
3. I should be able to book a room for a user/person/account for today and future dates (ignore timezone)
4. I should be able to view the few stats i.e total rooms, total room occupied today, total rooms available today
5. I should be able to check if room is available on future date

Design a good model. Its a simple requirment there will no need to use inheritance
"""

from datetime import date

class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        
    def add_room(self, room_name, num_of_beds, fare_per_day):
        room = {
            "room_name": room_name,
            "num_of_beds": num_of_beds,
            "fare_per_day": fare_per_day,
            "client_name": '',
            "is_booked": False,
            "check_in_date": None,
            "check_out_date": None
        }
        self.rooms.append(room)
    
    def book_room(self, room_name, user_name, check_in_date, check_out_date):
        print()
        for room in self.rooms:
            if room['room_name'] == room_name:
                if self.is_room_available(room_name, check_in_date, check_out_date):
                    check_in_date = date.fromisoformat(check_in_date)   
                    check_out_date = date.fromisoformat(check_out_date)
                    room['client_name'] = user_name
                    room['is_booked'] = True
                    room['check_in_date'] = check_in_date
                    room['check_out_date'] = check_out_date
                    print(f"{user_name} has successfully booked {room_name} from {check_in_date} to {check_out_date}")
                    print(f"Fare/Day of this room: {room['fare_per_day']}")
                    print(f"Total Cost: {room['fare_per_day'] * (check_out_date - check_in_date).days}")
                    return True
                else:
                    print(f"Sorry, {room_name} is not available from {room['check_in_date']} to {room['check_out_date']}")
                    return False
        print("Invalid Room Name")
                
    def is_room_available(self, room_name, check_in_date, check_out_date):
        check_in_date = date.fromisoformat(check_in_date)   
        check_out_date = date.fromisoformat(check_out_date)
        for room in self.rooms:
            if room['room_name'] == room_name:
                if room['is_booked'] == False:
                    print("Room is available")
                    return True
                elif room['check_in_date'] <= check_in_date <= room['check_out_date'] or room['check_in_date'] <= check_out_date <= room['check_out_date']:
                    print("Room is booked")
                    return False
                print("Room is available")
                return True
        return False
    
    def get_stats(self):
        total_rooms = len(self.rooms)
        total_rooms_occupied = sum(1 for room in self.rooms if room['is_booked'])
        total_rooms_available = total_rooms - total_rooms_occupied
        print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        print(f"Total Rooms: {total_rooms}")
        print(f"Total Room(s) Occupied Today: {total_rooms_occupied}")
        print(f"Total Rooms Available Today: {total_rooms_available}")
        print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        
hotel = Hotel("STA", "XYZ")

hotel.add_room('5 star',5, 500)
hotel.add_room('4 star',4, 400)
hotel.add_room('3 star',3, 300)
hotel.add_room('2 star',2, 200)
hotel.add_room('1 star',1, 100)

hotel.book_room('5 star', 'Talha', '2017-10-01', '2017-10-10')
hotel.book_room('5 star', 'Talha', '2017-10-02', '2017-10-08')
hotel.book_room('5 star', 'Talha', '2017-10-02', '2017-10-15')
hotel.book_room('5 star', 'Talha', '2017-10-11', '2017-10-15')
hotel.book_room('4 star', 'Talha', '2017-10-01', '2017-10-10')
hotel.get_stats()