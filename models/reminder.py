
class Reminder:

    def __init__(self,personName,reminderNumber,frequency,startDate,onFreeze=False,frozenPeriod= None):
        self.personName = personName;
        self.reminderNumber =reminderNumber;
        self.frequency = frequency;
        self.startDate=startDate;
        self.onFreeze = onFreeze;
        self.frozenPeriod = frozenPeriod;
        self.reachingDate;
    def __repr__(self) -> str:
        return f"(PersonName:{self.personName},\nreminderNumber:{self.reminderNumber},\nFrequency:{self.frequency},\nStartDate:{self.startDate},\nOnFreeze:{self.onFreeze},\nFrozenPeriod:{self.frozenPeriod})"