# College Mobile Usage Tracker 📱

students = int(input("Enter number of students: "))
mobile_users = int(input("Enter number of students using mobiles: "))

if mobile_users <= students:
    percentage = (mobile_users / students) * 100

    print("\n📱 College Mobile Usage Report")
    print("------------------------------")
    print("Total students:", students)
    print("Mobile users:", mobile_users)
    print("Usage percentage:", round(percentage, 2), "%")

    if percentage > 70:
        print("⚠️ High mobile usage in college.")
    elif percentage >= 40:
        print("🟡 Moderate mobile usage.")
    else:
        print("🟢 Low mobile usage.")
else:
    print("❌ Mobile users cannot be greater than total students.")
