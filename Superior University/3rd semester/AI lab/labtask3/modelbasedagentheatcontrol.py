class HomeTemperatureController:
    def __init__(self, target_temperature):
        self.target_temperature = target_temperature
        self.room_temperatures = {}

    def sense(self, room, temperature):
        self.room_temperatures[room] = temperature

    def decide_action(self, room):
        if room in self.room_temperatures:  
            if self.room_temperatures[room] > self.target_temperature:
                return f"Reduce heating in the {room}"
            else:
                return f"Increase heating in the {room}"
        return "Room not found"

controller = HomeTemperatureController(22)


room_data = {
    "Living Room": 28,
    "Bedroom": 18,
    "Kitchen": 32
}


for room, temp in room_data.items():
    controller.sense(room, temp)
    action = controller.decide_action(room)
    print(f"{room}: {temp}°C ==> Action: {action}")
