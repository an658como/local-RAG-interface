import SLM
from langchain.prompts import PromptTemplate

# Initialize the local LLM
llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

# Create the email template
email_template = PromptTemplate.from_template(
    "Create an invitation email to the recipient that is {recipient_name} "
    "for an event that is {event_type} in a language that is {language}. "
    "Mention the event location that is {event_location} "
    "and event date that is {event_date}. "
    "Also write a few sentences about the event description that is {event_description} "
    "in a style that is {style}."
)

# Format the message using the template
message = email_template.format(
    style="enthusiastic tone",
    language="American English",
    recipient_name="John",
    event_type="product launch",
    event_date="January 15, 2024",
    event_location="Grand Ballroom, City Center Hotel",
    event_description="an exciting unveiling of our latest innovations"
)

# Invoke the local model
response = llm.invoke(message)
print(response)

'''
Here's an invitation email to John:

Subject: You're Invited: Our Latest Innovations Launch Event!

Dear John,

We are thrilled to invite you to a very special event, marking the launch of our latest innovations! On January 15, 2024, we will be unveiling our exciting new products at the stunning Grand Ballroom, located in the heart of City Center Hotel.

Get ready for an unforgettable experience as we bring together industry experts, influencers, and enthusiasts to witness the unveiling of our cutting-edge technology. Our team has worked tirelessly to create something truly groundbreaking, and we can't wait to share it with you!

Join us for an evening of inspiration, excitement, and discovery as we launch our latest innovations. The event promises to be a night to remember, with plenty of opportunities to network, learn, and get up close and personal with the latest advancements.

Date: January 15, 2024
Time: [Insert time]
Location: Grand Ballroom, City Center Hotel

We look forward to seeing you there! If you have any questions or require more information, please don't hesitate to reach out.

Best regards,
[Your Name]
'''