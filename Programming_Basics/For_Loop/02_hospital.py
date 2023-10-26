period = int(input())
doctors = 7
cured_patients = 0
uncured_patients = 0

for i in range(period):
    patients = int(input())
    if (i + 1) % 3 == 0 and uncured_patients > cured_patients:
        doctors += 1

    if patients <= doctors:
        cured_patients += patients
    else:
        cured_patients = cured_patients + doctors
        uncured_patients += patients - doctors

print(f"Treated patients: {cured_patients}.")
print(f"Untreated patients: {uncured_patients}.")
