POLICIES = {
    "lockdown": "In a lockdown, stay in your room, lock the door, and keep students away from windows.",
    "fire_drill": "During a fire drill, line up at the door and exit the building calmly.",
    "late_policy": "Students arriving more than 10 minutes late must check in at the office."
}

def answer(question: str) -> str:
    q = question.lower()

    if "lockdown" in q:
        return POLICIES["lockdown"]

    if "fire" in q:
        return POLICIES["fire_drill"]

    if "late" in q:
        return POLICIES["late_policy"]

    return "I don't know. Please check the school handbook."

