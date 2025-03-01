from datetime import datetime, timedelta

class StartStopCalculator:
    def __init__(self):
        self.records = []
    
    def add_entry(self, start_time, stop_time):
        try:
            start = datetime.strptime(start_time, "%I:%M %p")
            stop = datetime.strptime(stop_time, "%I:%M %p")
            
            # Handle cases where medication duration crosses midnight
            if stop < start:
                stop += timedelta(days=1)
            
            duration = stop - start
            formatted_duration = f"{duration.seconds // 3600}:{(duration.seconds % 3600) // 60:02d}"
            
            entry = {
                "Start Time": start_time,
                "Stop Time": stop_time,
                "Total Duration (HH:MM)": formatted_duration
            }
            self.records.append(entry)
            return entry
        except ValueError:
            return "Invalid time format. Please use HH:MM AM/PM."
    
    def get_records(self):
        return self.records

# Integration with Injection & Infusion Tool
class InjectionInfusionTool:
    def __init__(self):
        self.cpt_codes = []
    
    def assign_cpt_code(self, route, medication_type, duration, concurrent=False):
        if route == "intravenous":
            if duration < 16:
                self.cpt_codes.append("96374 - IV Push, single drug")
            elif medication_type == "chemotherapy":
                if duration <= 90:
                    self.cpt_codes.append("96413 - Chemotherapy infusion, up to 1 hour")
                else:
                    self.cpt_codes.append("96415 - Chemotherapy infusion, each additional hour")
            elif medication_type == "hydration":
                if duration <= 30:
                    self.cpt_codes.append("96360 - Hydration infusion, initial 30 minutes")
                else:
                    self.cpt_codes.append("96361 - Hydration infusion, each additional 30 minutes")
            else:
                if duration <= 60:
                    self.cpt_codes.append("96365 - Intravenous infusion, up to 1 hour")
                else:
                    self.cpt_codes.append("96366 - Intravenous infusion, each additional hour")
            if concurrent:
                self.cpt_codes.append("96368 - Concurrent infusion of second or third drug")
        elif route in ["intramuscular", "subcutaneous"]:
            if medication_type == "vaccination":
                self.cpt_codes.append("90471 - Injection for immunization")
            else:
                self.cpt_codes.append("96372 - Therapeutic, prophylactic or diagnostic injection")
        return self.cpt_codes

# Example Usage:
# start_stop = StartStopCalculator()
# print(start_stop.add_entry("05:00 PM", "08:30 PM"))
# 
# infusion_tool = InjectionInfusionTool()
# print(infusion_tool.assign_cpt_code("intravenous", "hydration", 45))
