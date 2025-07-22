#!/usr/bin/env python3
"""
Employee Data Generator for Peer Recognition Dashboard
Generates sample employee data in JSON format
"""

import json
import random
from datetime import datetime, timedelta

# Sample data pools
FIRST_NAMES = [
    "Alex", "Blake", "Casey", "Drew", "Emery", "Finley", "Harper", "Indigo",
    "Jamie", "Kai", "London", "Morgan", "Nico", "Oakley", "Parker", "Quinn",
    "River", "Sage", "Taylor", "Uri", "Vale", "Winter", "Xara", "Yael", "Zara"
]

LAST_NAMES = [
    "Anderson", "Brown", "Chen", "Davis", "Evans", "Foster", "Garcia", "Harris",
    "Johnson", "Kim", "Lee", "Martinez", "Nguyen", "O'Connor", "Patel", "Robinson",
    "Smith", "Thompson", "Wilson", "Young"
]

DESIGNATIONS = {
    "Engineering": [
        "Software Engineer", "Senior Software Engineer", "Lead Engineer",
        "Frontend Developer", "Backend Developer", "Full Stack Developer",
        "DevOps Engineer", "Site Reliability Engineer", "Platform Engineer"
    ],
    "Product": [
        "Product Manager", "Senior Product Manager", "Product Owner",
        "Product Analyst", "Technical Product Manager"
    ],
    "Design": [
        "UX Designer", "UI Designer", "UX/UI Designer", "Product Designer",
        "Visual Designer", "Design Lead"
    ],
    "Marketing": [
        "Marketing Manager", "Digital Marketing Specialist", "Content Manager",
        "Marketing Analyst", "Brand Manager", "Growth Manager"
    ],
    "Analytics": [
        "Data Scientist", "Data Analyst", "Business Intelligence Analyst",
        "Machine Learning Engineer", "Analytics Manager"
    ],
    "Human Resources": [
        "HR Specialist", "HR Manager", "Talent Acquisition Specialist",
        "People Operations Manager", "HR Business Partner"
    ],
    "Sales": [
        "Sales Representative", "Account Manager", "Sales Manager",
        "Business Development Manager", "Sales Director"
    ],
    "Quality Assurance": [
        "QA Engineer", "Test Engineer", "QA Manager",
        "Automation Engineer", "Performance Test Engineer"
    ],
    "Operations": [
        "Operations Manager", "Business Analyst", "Process Improvement Specialist",
        "Operations Coordinator", "Workflow Analyst"
    ],
    "Security": [
        "Security Engineer", "Information Security Analyst", "Security Manager",
        "Cybersecurity Specialist", "Security Architect"
    ],
    "Finance": [
        "Financial Analyst", "Finance Manager", "Accountant",
        "Budget Analyst", "Financial Controller"
    ]
}

ACHIEVEMENTS = [
    "Innovation Award", "Team Player", "Code Quality Award", "Leadership Excellence",
    "Customer Focus", "Problem Solver", "Mentor of the Year", "Technical Excellence",
    "Collaboration Champion", "Process Improvement", "Performance Optimizer",
    "Security Champion", "Design Excellence", "Data Insights Master",
    "Campaign Excellence", "Revenue Growth", "Client Relations", "Bug Hunter",
    "Testing Excellence", "Infrastructure Hero", "API Design Master",
    "Scalability Expert", "Employee Engagement", "Budget Optimization",
    "Content Strategy", "UI/UX Excellence", "Vulnerability Detection",
    "Top Performer", "ML Innovation"
]

QUARTERS = ["Q1", "Q2", "Q3", "Q4"]

def generate_employee_id(index):
    """Generate employee ID"""
    return f"EMP{str(index + 1).zfill(3)}"

def generate_join_date():
    """Generate random join date within the last 2 years"""
    start_date = datetime.now() - timedelta(days=730)
    end_date = datetime.now() - timedelta(days=30)
    
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_email(first_name, last_name):
    """Generate email address"""
    return f"{first_name.lower()}.{last_name.lower()}@company.com"

def generate_employee(index):
    """Generate a single employee record"""
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    department = random.choice(list(DESIGNATIONS.keys()))
    designation = random.choice(DESIGNATIONS[department])
    quarter = random.choice(QUARTERS)
    recognitions = random.randint(1, 10)
    
    # Select 1-3 random achievements
    num_achievements = random.randint(1, 3)
    achievements = random.sample(ACHIEVEMENTS, num_achievements)
    
    return {
        "id": generate_employee_id(index),
        "name": f"{first_name} {last_name}",
        "designation": designation,
        "department": department,
        "quarter": quarter,
        "recognitions": recognitions,
        "achievements": achievements,
        "joinDate": generate_join_date(),
        "email": generate_email(first_name, last_name)
    }

def generate_quarter_info():
    """Generate quarter information"""
    return {
        "Q1": {
            "name": "Q1 2024",
            "period": "January - March 2024",
            "description": "Focus on foundation building and team establishment",
            "goals": ["Team building", "Process establishment", "Initial project delivery"]
        },
        "Q2": {
            "name": "Q2 2024",
            "period": "April - June 2024",
            "description": "Growth phase with increased productivity and innovation",
            "goals": ["Product development", "Innovation initiatives", "Customer satisfaction"]
        },
        "Q3": {
            "name": "Q3 2024",
            "period": "July - September 2024",
            "description": "Peak performance period with major project deliveries",
            "goals": ["Major releases", "Performance optimization", "Market expansion"]
        },
        "Q4": {
            "name": "Q4 2024",
            "period": "October - December 2024",
            "description": "Year-end achievements and strategic planning",
            "goals": ["Annual targets", "Strategic planning", "Year-end recognition"]
        }
    }

def generate_employee_data(num_employees=50):
    """Generate complete employee dataset"""
    employees = []
    
    for i in range(num_employees):
        employee = generate_employee(i)
        employees.append(employee)
    
    # Ensure we have representation across all quarters and departments
    for i, quarter in enumerate(QUARTERS):
        if i < len(employees):
            employees[i]["quarter"] = quarter
    
    for i, department in enumerate(DESIGNATIONS.keys()):
        if i < len(employees):
            employees[i]["department"] = department
            employees[i]["designation"] = random.choice(DESIGNATIONS[department])
    
    data = {
        "employees": employees,
        "quarters": generate_quarter_info(),
        "departments": list(DESIGNATIONS.keys())
    }
    
    return data

def main():
    """Main function to generate and save employee data"""
    print("Generating employee data...")
    
    # Get number of employees from user input or use default
    try:
        num_employees = int(input("Enter number of employees to generate (default 50): ") or "50")
    except ValueError:
        num_employees = 50
    
    # Generate data
    data = generate_employee_data(num_employees)
    
    # Save to JSON file
    filename = "generated_employee_data.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Generated data for {num_employees} employees")
    print(f"📁 Saved to: {filename}")
    
    # Print summary statistics
    departments = {}
    quarters = {}
    total_recognitions = 0
    
    for emp in data["employees"]:
        dept = emp["department"]
        quarter = emp["quarter"]
        
        departments[dept] = departments.get(dept, 0) + 1
        quarters[quarter] = quarters.get(quarter, 0) + 1
        total_recognitions += emp["recognitions"]
    
    print("\n📊 Summary Statistics:")
    print(f"   Total Employees: {num_employees}")
    print(f"   Total Departments: {len(departments)}")
    print(f"   Total Recognitions: {total_recognitions}")
    print(f"   Average Recognitions: {total_recognitions / num_employees:.1f}")
    
    print("\n🏢 Department Distribution:")
    for dept, count in sorted(departments.items()):
        print(f"   {dept}: {count} employees")
    
    print("\n📅 Quarter Distribution:")
    for quarter, count in sorted(quarters.items()):
        print(f"   {quarter}: {count} employees")

if __name__ == "__main__":
    main()
