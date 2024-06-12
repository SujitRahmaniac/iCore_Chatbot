from flask import Flask, jsonify, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests


app = Flask(__name__)

def send_email(name, address, phone_number, service, option):
    # Email credentials
    sender_email = "enter sender's mail"  # Replace with your email
    sender_password = "enter your password"  # Replace with your email password
    receiver_email = "enter recievers mail"  # Replace with recipient's email

    # Email content
    subject = "Appointment Details"
    body = f"Name: {name}\nAddress: {address}\nPhone Number: {phone_number}\nService: {service}\nOption: {option}"

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



@app.route('/greet', methods=['GET'])
def greet():
    message = {
        "message": "Welcome to iCore Software Systems. How can we assist you today?",
        "options": {
            "1": "Work With Us",
            "2": "Schedule an Appointment",
            "3": "Our Works",
            "4": "Contact Us",
            "5": "Client reviews and Testimonials"
        }
    }
    return jsonify(message)



@app.route('/work_with_us', methods=['GET'])
def work_with_us():
    message = {
        "message": "What service are you interested in?",
        "options": {
            "1": "Web Application Development",
            "2": "Mobile Application Development",
            "3": "Niche Solutions",
            "4": "Digital Marketing"
        }
    }
    return jsonify(message)

@app.route('/web_app_dev', methods=['GET'])
def web_app_dev():
    message = {
        "message": "What platform are you targeting?",
        "options": {
            "1": "Custom Web Applications",
            "2": "CMS Web Applications",
            "3": "E-Commerce Web Applications"
        }
    }
    return jsonify(message)

@app.route('/custom_web_app', methods=['GET'])
def custom_web_app():
    message = {
        "message": "A custom web application is a tailor-made solution designed specifically for your business needs. "
                   "It provides unique features and functionalities to address your specific requirements."
    }
    return jsonify(message)

@app.route('/cms_dev', methods=['GET'])
def cms_dev():
    message = {
        "message": "CMS development involves creating a Content Management System for your website, "
                   "allowing you to easily manage and update your website's content without technical expertise."
    }
    return jsonify(message)

@app.route('/ecommerce_web_design', methods=['GET'])
def ecommerce_web_design():
    message = {
        "message": "E-commerce website design focuses on creating an online storefront that enables you to sell products or services online. "
                   "It includes features like product listings, shopping carts, and secure payment gateways."
    }
    return jsonify(message)

@app.route('/mobile_app_dev', methods=['GET'])
def mobile_app_dev():
    message = {
        "message": "What platform are you targeting?",
        "options": {
            "1": "IOS Applications",
            "2": "Android Applications",
            "3": "Hybrid Mobile Applications"
        }
    }
    return jsonify(message)

@app.route('/ios_apps', methods=['GET'])
def ios_apps():
    message = {
        "message": "Develop native iOS applications tailored to Apple devices for seamless user experiences."
    }
    return jsonify(message)

@app.route('/android_apps', methods=['GET'])
def android_apps():
    message = {
        "message": "Build native Android applications optimized for a wide range of Android devices and versions."
    }
    return jsonify(message)

@app.route('/hybrid_apps', methods=['GET'])
def hybrid_apps():
    message = {
        "message": "Create hybrid mobile applications using frameworks like React Native or Flutter, combining web technologies with native code for cross-platform compatibility."
    }
    return jsonify(message)

@app.route('/niche_solutions', methods=['GET'])
def niche_solutions():
    message = {
        "message": "Which niche solution are you interested in?",
        "options": {
            "1": "Augmented Reality / Virtual Reality Services",
            "2": "UI / UX",
            "3": "Artificial Intelligence",
            "4": "CRM Solutions"
        }
    }
    return jsonify(message)

@app.route('/vr_ar_apps', methods=['GET'])
def vr_ar_apps():
    message = {
        "message": "Explore immersive experiences and interactive solutions with AR/VR technologies, revolutionizing the way users interact with digital content."
    }
    return jsonify(message)

@app.route('/ui_ux', methods=['GET'])
def ui_ux():
    message = {
        "message": "Elevate user experiences with intuitive user interfaces and captivating user experiences, ensuring seamless navigation and engagement."
    }
    return jsonify(message)

@app.route('/ai', methods=['GET'])
def ai():
    message = {
        "message": "Leverage AI technologies such as machine learning and natural language processing to automate tasks, gain insights, and enhance decision-making processes."
    }
    return jsonify(message)

@app.route('/crm', methods=['GET'])
def crm():
    message = {
        "message": "Streamline customer relationship management processes with tailored CRM solutions, enabling efficient customer engagement, retention, and satisfaction."
    }
    return jsonify(message)

@app.route('/digital_marketing', methods=['GET'])
def digital_marketing():
    message = {
        "message": "What digital marketing service are you interested in?",
        "options": {
            "1": "Search Engine Optimization (SEO)",
            "2": "Search Engine Marketing / Google Adwords",
            "3": "Social Media Optimization (SMO) / Social Media Marketing (SMM)"
        }
    }
    return jsonify(message)

@app.route('/seo', methods=['GET'])
def seo():
    message = {
        "message": "Search Engine Optimization (SEO) - Improve your website's visibility on search engines organically, increase traffic, and enhance online presence through strategic optimization techniques."
    }
    return jsonify(message)

@app.route('/sem', methods=['GET'])
def sem():
    message = {
        "message": "Search Engine Marketing / Google Adwords - Reach targeted audiences effectively through paid advertising on search engines, drive website traffic, and maximize conversions with Google AdWords."
    }
    return jsonify(message)

@app.route('/smo', methods=['GET'])
def smo():
    message = {
        "message": "Social Media Optimization (SMO) / Social Media Marketing (SMM) - Boost brand awareness, engage with your audience, and drive website traffic through optimized social media presence and targeted social media advertising."
    }
    return jsonify(message)

@app.route('/schedule_appointment', methods=['GET', 'POST'])
def schedule_appointment():
    if request.method == 'GET':
        message = {
            "message": "Please provide your details to schedule an appointment.",
            "options": {
                "name": "Your Name",
                "address": "Your Address",
                "phone_number": "Your Phone Number",
                "option": "Your Choice"
            }
        }
        return jsonify(message)
    elif request.method == 'POST':
        data = request.json
        name = data.get('name')
        address = data.get('address')
        phone_number = data.get('phone_number')
        option = data.get('option')

        if name and address and phone_number and option:
            # Perform scheduling logic here, e.g., storing data in database
            return jsonify({"message": "Your appointment has been scheduled successfully!"})
        else:
            return jsonify({"error": "Incomplete data. Please provide all required fields."}), 400
    else:
        return jsonify({"error": "Method not allowed"}), 405


@app.route('/our_works', methods=['GET'])
def our_works():
    message = {
        "works": [
            "Iride - Taxi booking app",
            "Iportal - Resume storage and retrieval portal",
            "Itrack - Incident management tool",
            "Catalina augmented reality app - Remote issue resolution of Assets (Printers and PCs) issues",
            "Trintas - Admin module",
            "PKS - Persistent knowledge solutions - an interactive website",
            "Readygrass, UK - rectified a payment gateway issue.",
            "ORM (Online Reputation Management) plugin -  grab reviews and soliciting reviews",
            "Newfoil, UK - completely responsive website",
            "Agile Advantages, USA - website design and development",
            "Central Fans, UK - a fullstack project",
            "Payperfix.net - outsourcing market place"
        ]
    }
    return jsonify(message)

@app.route('/clients_and_reviews', methods=['GET'])
def clients_and_reviews():
    message = {
        "clients_and_reviews": [
            {
                "name": "Tim Adams",
                "designation": "Design Project Manager",
                "company": "Forte Trinity",
                "review": "We needed a fix to a .NET ecommerce project. The guys at iCore were very helpful and attentive. They fixed the issue rapidly and were very cost effective. I would highly recommend iCore to anyone looking for an affective developer. We will be working with them again on future projects."
            },
            {
                "name": "Michael Purvis",
                "designation": "Director",
                "company": "Scream Marketing",
                "review": "iCore software systems have recently started working on an SEO and website project for my client, I am very pleased with the results so far and they are a pleasure to work with and always easy to contact with any queries which is always one of the main things i find important when using a company. I would recommend using icore for SEO and Web Design."
            }
        ]
    }
    return jsonify(message)

@app.route('/contact_us', methods=['GET'])
def contact_us():
    contact_info = {
        "India": {
            "Mobile": "+91 73580 56001",
            "Phone": "+91 (044) 42059777",
            "Website": "https://www.icoresoftwaresystems.com",
            "Email": "contact@icoresoftwaresystems.com"
        },
        "USA": {
            "Phone": "+1 (469) 885-2249",
            "Website": "https://www.icoretek.com",
            "Email": "contact@icoretek.com"
        }
    }
    return jsonify(contact_info)

if __name__ == '__main__':
    app.run(debug=True)