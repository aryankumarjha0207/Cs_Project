Class MedicationReminder:

Initialize medications as empty list

Method add\_medication(name, dosage, time):

Create dict for med with name, dosage, time

Append med to medications list

Print confirmation

Method remove\_medications(name):

For each med in medications:

If med's name matches:

Remove med and print confirmation

Return

If not found, print not found message

Method list\_medications():

If medications list is empty:

Print no meds message

Else:

Print formatted list of meds

Method check\_reminder(current\_time):

For each med in medications:

If med's time matches current\_time:

Print reminder

Function main():

Create MedicationReminder object

While True:

Display menu

Get user choice

Based on choice, call appropriate method (add, remove, list, check, exit)
