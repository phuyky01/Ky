from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class DownlinkCommandType:
    SET_UPLOAD_TIME_24H = "SET_UPLOAD_TIME_24H"
    SET_UPLOAD_CLOCK = "SET_UPLOAD_CLOCK"
    SET_CLOCK_BY_DATE = "SET_CLOCK_BY_DATE"
    SET_FULL_ALARM_THRESHOLD = "SET_FULL_ALARM_THRESHOLD"
    SET_FIRE_ALARM_THRESHOLD = "SET_FIRE_ALARM_THRESHOLD"
    SET_FALL_ALARM_THRESHOLD = "SET_FALL_ALARM_THRESHOLD"
    SET_BATTERY_ALARM_THRESHOLD = "SET_BATTERY_ALARM_THRESHOLD"
    SET_SERVER_ADDRESS = "SET_SERVER_ADDRESS"
    SELECT_SERVER = "SELECT_SERVER"
    SET_CYCLE_DETECTION_TIME = "SET_CYCLE_DETECTION_TIME"
    SET_APN = "SET_APN"
    SET_BAND = "SET_BAND"
    SET_ACC_XYZ_ENABLE = "SET_ACC_XYZ_ENABLE"
    SET_LIFT_UP_DOWN_ALARM_THRESHOLD = "SET_LIFT_UP_DOWN_ALARM_THRESHOLD"
    SWITCH_FUNCTION = "SWITCH_FUNCTION"


class SensorCommandSetting(BaseModel):
    name: Optional[str] = Field(default=None)
    command_json: Dict[str, Any] = Field(default=None)
    packet_head: str = "80"
    command_type: str = "02"
    command_code: str = Field(default=None)
    payload_header: str = "9999"
    payload_command_code: str = Field(default=None)
    payload_content: str = Field(default=None)
    payload_tail: str = "81"
    command_json: Dict[str, Any] = Field(default_factory=dict)

    def return_command(self):
        print("packet_head:", self.packet_head)
        print("command_type:", self.command_type)
        print("payload_header:", self.payload_header)
        print("command_code:", self.command_code)
        print("payload_content:", self.payload_content)
        print("payload_tail:", self.payload_tail)
        print("payload_header: ", self.payload_header + " command_code: ", self.command_code + " payload_content: ", self.payload_content + " payload_tail:", self.payload_tail)
        return f"{self.packet_head}{self.command_type}{self.payload_header}{self.command_code}{self.payload_content}{self.payload_tail}"

    def return_command_json(self):
        return self.command_json

    def decimal_to_hex(self, decimal: int, length=2):
        return hex(decimal)[2:].rjust(length, "0").upper()

    def convert_time_to_decimal(self, time: str) -> int:
        time_parts = time.split(":")
        return int(time_parts[0]) * 60 + int(time_parts[1])

class SetClockByDate(SensorCommandSetting):
    name: str = DownlinkCommandType.SET_CLOCK_BY_DATE
    command_code: str = "0F"

    week_day_to_hex_map: Optional[Dict[str, str]] = Field(default={
        "Sunday": "00",
        "Monday": "01",
        "Tuesday": "02",
        "Wednesday": "03",
        "Thursday": "04",
        "Friday": "05",
        "Saturday": "06"
    })

    def translate_payload_content(self, content) -> str:
        weekday_index_map = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
        weekday_index = weekday_index_map[content.get("weekday")]
        base_offset_minutes = weekday_index * 1440

        # ACC value must be 2 bytes (e.g., 100 -> 0064)
        hex_ACC_value_threshold = self.decimal_to_hex(int(content.get("acc_value_threshold", 100)), 4)

        hex_report_clocks = []
        for report_clock in content.get("report_clocks", []):
            minutes = self.convert_time_to_decimal(report_clock)
            absolute_minutes = base_offset_minutes + minutes
            hex_report_clocks.append(self.decimal_to_hex(absolute_minutes, 4))

        # Ensure the list has exactly 6 elements, padding with "FFFF" if necessary
        while len(hex_report_clocks) < 6:
            hex_report_clocks.append("FFFF")
        hex_report_clocks_format = "".join(hex_report_clocks)

        weekday_hex = self.week_day_to_hex_map[content.get("weekday")]

        # Duration byte is intentionally omitted from payload per latest requirement
        self.payload_content = f"{hex_ACC_value_threshold}{weekday_hex}{hex_report_clocks_format}"
    

if __name__ == "__main__":
    schedules = (
        ("Monday", ["01:00", "05:00", "09:00", "13:00", "17:00"]),
        ("Tuesday", ["01:00", "05:00", "09:00", "13:00", "17:00"]),
        ("Wednesday", ["01:00", "05:00", "09:00", "13:00", "17:00"]),
        ("Thursday", ["01:00", "05:00", "09:00", "13:00", "17:00"]),
        ("Friday", ["01:00", "05:00", "09:00", "11:00"]),
        ("Saturday", ["18:00", "20:00"]),
        ("Sunday", ["01:00", "05:00", "09:00", "13:00", "17:00"]),
    )
   
    for i, (weekday, clocks) in enumerate(schedules):
        parser = SetClockByDate()
        parser.translate_payload_content({"weekday": weekday, "report_clocks": clocks})
        print("Weekday:", weekday)
        print("Command combined:", parser.return_command())
        print("--------------------------------")
