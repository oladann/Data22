class Location:

    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return f"(latitude={self.latitude}, longitude={self.longitude})"

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude



bham_academy = location(52.488647, -1.887249)
print(f"The coordinates for the birmingham accademy are: {bham_academy}")
