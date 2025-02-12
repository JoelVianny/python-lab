import re

class Length:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    @classmethod
    def from_string(cls, text):
        """Transforme une chaîne comme '5'8"' en objet Length."""
        pattern = r"^\s*(\d+)'\s*(\d+)\"\s*$"  # Regex pour vérifier le format
        match = re.match(pattern, text)
        
        if not match:
            raise ValueError("Format invalide. Utilisez par exemple 5'8\".")

        feet, inches = map(int, match.groups())

        if inches >= 12:
            raise ValueError("Les pouces doivent être inférieurs à 12.")

        return cls(feet, inches)

    def __str__(self):
        return f"{self.feet}'{self.inches}\""

# --- Tests ---
try:
    length1 = Length.from_string("5'8\"")
    print(length1)  # ✅ 5'8"
    
    length2 = Length.from_string(" 10' 11\" ")  
    print(length2)  # ✅ 10'11"

    length3 = Length.from_string("7'12\"")  
    print(length3)

except ValueError as e:
    print("Erreur :", e)

try:
    length4 = Length.from_string("abc")  
    print(length4)
except ValueError as e:
    print("Erreur :", e)
