import smtplib
import random

# Function to send verification code
def send_verification_code(email):
    code = random.randint(100000, 999999)
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("your_email@gmail.com", "your_password")
            message = f"Subject: Verification Code\n\nYour verification code is: {code}"
            server.sendmail("your_email@gmail.com", email, message)
        return code
    except Exception as e:
        print(f"Failed to send email: {e}")
        return None

# Function to verify the code
def verify_code(input_code, actual_code):
    return input_code == actual_code

# Example usage
if __name__ == "__main__":
    email = input("Enter your email: ")
    sent_code = send_verification_code(email)
    if sent_code:
        user_code = int(input("Enter the verification code sent to your email: "))
        if verify_code(user_code, sent_code):
            print("Verification successful!")
        else:
            print("Invalid verification code.")
    else:
        print("Failed to send verification code.")