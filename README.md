# Medication Reminder System

**Course:** Computer Science Engineering Project  
**Institution:** VIT Bhopal University  
**Professor:** Prof. Shahana Ghajala Qureshi  
**Student Name:** Aryan A.K Jha  
**Registration Number:** 25BAI10517  
**Date:** November 2025

---

## 📋 Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Requirements](#system-requirements)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Flowchart](#flowchart)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Medication Reminder System** is a Python-based console application designed to help users manage their medication schedules effectively. This system allows users to add, remove, list, and set reminders for their medications, ensuring timely medication intake and better health management.

This project demonstrates fundamental programming concepts including:
- Object-Oriented Programming (OOP)
- Data Structure Management (Lists and Dictionaries)
- User Input Validation
- Menu-Driven Interface Design
- Time-Based Reminder Logic

---

## ❗ Problem Statement

See [statement.md](statement.md) for detailed problem statement.

**Brief:** Many individuals, especially elderly patients and those with chronic conditions, struggle to remember their medication schedules. Missing doses can lead to serious health complications. This system provides a simple, accessible solution to track and remind users about their medication timings.

---

## ✨ Features

### Core Functionalities

1. **Add Medication**
   - Store medication name, dosage, and scheduled time
   - Intuitive input prompts
   - Confirmation messages

2. **Remove Medication**
   - Delete medications from the list by name
   - Error handling for non-existent medications

3. **List All Medications**
   - View all stored medications in a formatted table
   - Shows medication number, name, dosage, and time
   - Empty list handling

4. **Check Reminder**
   - Time-based reminder checks
   - Alerts user when it's time to take medication
   - Supports HH:MM format

5. **User-Friendly Interface**
   - Clean menu-driven navigation
   - Clear visual separators
   - Input validation

---

## 💻 Technologies Used

- **Programming Language:** Python 3.x
- **Development Environment:** Any Python IDE (VS Code, PyCharm, IDLE)
- **Data Structures:** Lists, Dictionaries
- **Paradigm:** Object-Oriented Programming (OOP)

---

## 🔧 System Requirements

### Hardware Requirements
- Processor: Intel Core i3 or equivalent
- RAM: 2 GB minimum
- Storage: 50 MB free space

### Software Requirements
- Operating System: Windows 10/11, macOS, or Linux
- Python Version: 3.6 or higher
- Terminal/Command Prompt access

---

## 📥 Installation & Setup

### Step 1: Install Python
Download and install Python from [python.org](https://www.python.org/downloads/)

Verify installation:
```bash
python --version
```

### Step 2: Download the Project
Clone or download the project files to your local machine.

### Step 3: Navigate to Project Directory
```bash
cd medication-reminder-system
```

### Step 4: Run the Application
```bash
python medication_reminder.py
```

---

## 📖 Usage Guide

### Starting the Application
Run the Python script:
```bash
python medication_reminder.py
```

### Menu Options

#### 1️⃣ Add Medication
```
Example:
Medication name: Aspirin
Dosage: 100mg
Time (HH:MM): 09:00
```

#### 2️⃣ Remove Medication
```
Example:
Medication name to remove: Aspirin
```

#### 3️⃣ List All Medications
Displays all stored medications in a formatted table.

#### 4️⃣ Check Reminder
```
Example:
Enter current time (HH:MM): 09:00
*REMINDER: Take your Aspirin (100mg) NOW!*
```

#### 5️⃣ Exit
Closes the application with a farewell message.

---

## 📁 Project Structure

```
medication-reminder-system/
│
├── medication_reminder.py      # Main application file
├── README.md                   # Project documentation (this file)
├── DOCUMENTATION.md            # Detailed technical documentation
├── statement.md                # Problem statement
├── screenshots/                # Application screenshots
│   ├── main_menu.png
│   ├── add_medication.png
│   ├── list_medications.png
│   └── reminder_alert.png
└── diagrams/
    ├── flowchart.png          # System flowchart
    └── workflow.png           # Application workflow
```

---

## 📸 Screenshots

### Main Menu Interface
![Main Menu](screenshots/main_menu.png)

### Adding Medication
![Add Medication](screenshots/add_medication.png)

### Medication List
![List Medications](screenshots/list_medications.png)

### Reminder Alert
![Reminder](screenshots/reminder_alert.png)

---

## 📊 Flowchart

![System Flowchart](diagrams/flowchart.png)

See [DOCUMENTATION.md](DOCUMENTATION.md) for detailed workflow diagrams and pseudocode.

---

## 🚀 Future Enhancements

1. **Database Integration**
   - Store medications persistently using SQLite or MySQL
   - User account management

2. **GUI Implementation**
   - Develop using Tkinter or PyQt
   - More intuitive visual interface

3. **Advanced Reminder System**
   - Real-time notifications using system alerts
   - Multiple reminders per day
   - Recurring medication schedules

4. **Mobile Application**
   - Android/iOS version
   - Push notifications

5. **Analytics Dashboard**
   - Medication adherence tracking
   - Visual reports and statistics
   - Export data to CSV/PDF

6. **Multi-User Support**
   - Caregiver access
   - Family member monitoring
   - Healthcare provider integration

7. **Voice Assistance**
   - Voice commands for adding medications
   - Audio reminders

---

## 🤝 Contributing

This is an academic project for VIT Bhopal. For suggestions or improvements:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## 📄 License

This project is submitted as part of the CSE curriculum at VIT Bhopal University.

**Academic Use Only** - Please consult with Prof. Shahana Ghajala Qureshi before any external use or distribution.

---

## 👤 Author

**Aryan A.K Jha**  
Registration Number: 25BAI10517  
VIT Bhopal University  
Email: [Your Email]  
GitHub: [Your GitHub Profile]

---

## 🙏 Acknowledgments

- **Prof. Shahana Ghajala Qureshi** - Course Instructor and Project Guide
- **VIT Bhopal University** - For providing the learning environment
- **Python Community** - For comprehensive documentation and resources

---

## 📞 Contact

For any queries regarding this project:
- **Email:** [Your VIT Email]
- **Phone:** [Your Contact Number]
- **Office Hours:** [Consultation Timings]

---

**Last Updated:** November 24, 2025

**Version:** 1.0.0

---

*"Taking care of your health, one reminder at a time."*