import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

def send_email(name, address, phone_number, service, option):
    try:
        # Email credentials
        sender_email = "sujitprojecticore@gmail.com"  # Replace with your email
        sender_password = "rsek qbvp sydw yskt"  # Replace with your email password
        receiver_email = "soundsarojapubg@gmail.com"  # Replace with recipient's email

        # Email content
        subject = "Appointment Details"
        body = f"Name: {name}\nAddress: {address}\nPhone Number: {phone_number}\nService required: {option}"

        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


def get_response(route):
    base_url = "http://127.0.0.1:5000"  # Change the URL accordingly if not running locally
    response = requests.get(base_url + route)
    return response.json()

def schedule_appointment():
    response = get_response('/schedule_appointment')
    print(response['message'])
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    option = input("Enter the required service: ")

    appointment_data = {
        "name": name,
        "address": address,
        "phone_number": phone_number,
        "option": option
    }

    response = requests.post('http://127.0.0.1:5000/schedule_appointment', json=appointment_data)

    if response.status_code == 200:
        print("Your appointment has been scheduled successfully!")
        send_email(name, address, phone_number, "Schedule Appointment", option)
    else:
        print("Failed to schedule appointment. Please try again.")



def main():
    base_url = "http://127.0.0.1:5000"  # Change the URL accordingly if not running locally

    def get_response(route):
        response = requests.get(base_url + route)
        return response.json()

    def greet():
        response = get_response('/greet')
        print(response['message'])
        print(response['options'])
        return response['options']

    def work_with_us():
        response = get_response('/work_with_us')
        print(response['message'])
        return response['options']
    
    def web_app_dev():
        response = get_response('/web_app_dev')
        print(response['message'])
        return response['options']

    def custom_web_app():
        response = get_response('/custom_web_app')
        print(response['message'])

    def cms_dev():
        response = get_response('/cms_dev')
        print(response['message'])

    def ecommerce_web_design():
        response = get_response('/ecommerce_web_design')
        print(response['message'])

    def mobile_app_dev():
        response = get_response('/mobile_app_dev')
        print(response['message'])
        return response['options']

    def ios_apps():
        response = get_response('/ios_apps')
        print(response['message'])

    def android_apps():
        response = get_response('/android_apps')
        print(response['message'])

    def hybrid_apps():
        response = get_response('/hybrid_apps')
        print(response['message'])

    def niche_solutions():
        response = get_response('/niche_solutions')
        print(response['message'])
        return response['options']

    def vr_ar_apps():
        response = get_response('/vr_ar_apps')
        print(response['message'])

    def ui_ux():
        response = get_response('/ui_ux')
        print(response['message'])

    def ai():
        response = get_response('/ai')
        print(response['message'])

    def crm():
        response = get_response('/crm')
        print(response['message'])

    def digital_marketing():
        response = get_response('/digital_marketing')
        print(response['message'])
        return response['options']

    def seo():
        response = get_response('/seo')
        print(response['message'])

    def sem():
        response = get_response('/sem')
        print(response['message'])

    def smo():
        response = get_response('/smo')
        print(response['message'])

    def our_works():
        response = get_response('/our_works')
        print("Here are some of our works...")
        for work in response['works']:
            print(work)

    def clients_and_reviews():
        response = get_response('/clients_and_reviews')
        print("Client Reviews and Testimonials:")
        for review in response['clients_and_reviews']:
            print(f"Name: {review['name']}")
            print(f"Designation: {review['designation']}")
            print(f"Company: {review['company']}")
            print(f"Review: {review['review']}")
            print()

    def contact_us():
        response = get_response('/contact_us')
        print("Contact Information:")
        for country, info in response.items():
            print(country)
            for key, value in info.items():
                print(f"{key}: {value}")
            print()

           

    options = greet()
    choice = input("Enter your choice: ")

    if choice in options:
        if choice == '1':
            work_with_us_options = work_with_us()
            print("Options:")
            for key, value in work_with_us_options.items():
                print(f"{key}: {value}")
            service_choice = input("Enter your choice: ")
            if service_choice in work_with_us_options:
                if service_choice == '1':
                    web_app_dev_options = web_app_dev()
                    print("Options:")
                    for key, value in web_app_dev_options.items():
                        print(f"{key}: {value}")
                    web_choice = input("Enter your choice: ")
                    if web_choice in web_app_dev_options:
                        if web_choice == '1':
                            custom_web_app()
                        elif web_choice == '2':
                            cms_dev()
                        elif web_choice == '3':
                            ecommerce_web_design()
                        else:
                            print("Invalid option selected.")
                    else:
                        print("Invalid option selected.")
                elif service_choice == '2':
                    mobile_app_dev_options = mobile_app_dev()
                    print("Options:")
                    for key, value in mobile_app_dev_options.items():
                        print(f"{key}: {value}")
                    mobile_choice = input("Enter your choice: ")
                    if mobile_choice in mobile_app_dev_options:
                        if mobile_choice == '1':
                            ios_apps()
                        elif mobile_choice == '2':
                            android_apps()
                        elif mobile_choice == '3':
                            hybrid_apps()
                        else:
                            print("Invalid option selected.")
                    else:
                        print("Invalid option selected.")
                elif service_choice == '3':
                    niche_solutions_options = niche_solutions()
                    print("Options:")
                    for key, value in niche_solutions_options.items():
                        print(f"{key}: {value}")
                    niche_choice = input("Enter your choice: ")
                    if niche_choice in niche_solutions_options:
                        if niche_choice == '1':
                            vr_ar_apps()
                        elif niche_choice == '2':
                            ui_ux()
                        elif niche_choice == '3':
                            ai()
                        elif niche_choice == '4':
                            crm()
                        else:
                            print("Invalid option selected.")
                    else:
                        print("Invalid option selected.")
                elif service_choice == '4':
                    digital_marketing_options = digital_marketing()
                    print("Options:")
                    for key, value in digital_marketing_options.items():
                        print(f"{key}: {value}")
                    marketing_choice = input("Enter your choice: ")
                    if marketing_choice in digital_marketing_options:
                        if marketing_choice == '1':
                            seo()
                        elif marketing_choice == '2':
                            sem()
                        elif marketing_choice == '3':
                            smo()
                        else:
                            print("Invalid option selected.")
                    else:
                        print("Invalid option selected.")
                else:
                    print("Invalid option selected.")
            else:
                print("Invalid option selected.")
        elif choice == '2':
            schedule_appointment()
            
        elif choice == '3':
            our_works()
        elif choice == '4':
            contact_us()
        elif choice == '5':
            clients_and_reviews()
        else:
            print("Invalid option selected.")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()

