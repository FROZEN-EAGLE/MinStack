class UndergSys:
    def __init__(self):
        self.checks_ins = {}
        self.travel_time = {}

    def chek_in(self, passenger_id: int, station: str, time: int) -> None:
        if passenger_id in self.checks_ins:
            return
        self.checks_ins[passenger_id] = (station, time)

    def check_out(self, passenger_id: int, station: str, time: int) -> None:
        if passenger_id not in self.checks_ins:
            return

        start_stat, check_time = self.checks_ins.pop(passenger_id)
        route = (start_stat, station)
        duration = time - check_time

        if route not in self.travel_time:
            self.travel_time[route] = [0,0]

        self.travel_time[route][0] += duration
        self.travel_time[route][1] += 1

    def get_time(self, start_stat: str, end_stat: str) -> float:
        route = (start_stat, end_stat)
        if route not in self.travel_time:
            return None
        total, count = self.travel_time[route]
        return total / count