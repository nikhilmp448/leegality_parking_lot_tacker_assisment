class ParkingLot:
    def __init__(self, levels):
        self.levels = {}
        self.level_to_slots = {}
        self.vehicle_to_spot = {}  
        slot_start = 1

        for level in levels:
            self.levels[level] = [False] * 20
            self.level_to_slots[level] = (slot_start, slot_start + 19)
            slot_start += 20

    def update_level_slots(self, level):
        if level not in self.levels:
            self.levels[level] = [False] * 20
            start_spot = max([end_spot for _,(_, end_spot) in self.level_to_slots.items()])
            end_spot = start_spot + 19
            self.level_to_slots[level] = (start_spot + 1, end_spot + 1)

    def assign_parking_space(self, vehicle_number):
        if vehicle_number in self.vehicle_to_spot:
            return False

        for level, slots in self.level_to_slots.items():
            start_spot, end_spot = slots

            for spot in range(start_spot, end_spot + 1):
                if not self.levels[level][spot - start_spot]:
                    self.vehicle_to_spot[vehicle_number] = (level, spot)
                    self.levels[level][spot - start_spot] = True
                    return {"level": level, "spot": spot}

        return "Parking is full"
    
    def retrieve_parking_spot(self, vehicle_number):
        if vehicle_number in self.vehicle_to_spot:
            level, spot = self.vehicle_to_spot[vehicle_number]
            del self.vehicle_to_spot[vehicle_number]  
            self.levels[level][spot - self.level_to_slots[level][0]] = False  
            return {"level": level, "spot": spot}
        else:
            return False

    def print_parking_status(self):
        for level, slots in self.level_to_slots.items():
            start_spot, end_spot = slots
            print(f'Level {level}:')
            for spot in range(start_spot, end_spot + 1):
                occupied = self.levels[level][spot - start_spot]
                status = 'Occupied' if occupied else 'Available'
                print(f'Spot {spot}: {status}')