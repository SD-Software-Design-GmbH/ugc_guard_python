from ugc_guard_python.ugc_guard_python import GuardClient
from ugc_guard_python.wrapper.content_wrapper import (
    ContentWrapper, ReportContent, ReportPerson, Body, TextBody, MultiMediaBody, MultiMultiMediaBody, ContentType
)

# Initialize the GuardClient
guard_client = GuardClient(
    organization_id="d3cc59a5-de38-4148-988d-e77c45b38d60",
    base_url="http://localhost:8099/"
)
print("🚀 ~ guard_client:", guard_client)

# Define module ID, secret, and type ID
mid = "8f430b83-25ca-4218-a1a2-bfc1dfc5c924"
sec = "9CuLBQA6NjL9_Y9baW8-nGOZ00g"
type_id = "64a40e7b-d224-4199-b1a3-459082298611"

# Create a MultiMediaBody from a file path
body = MultiMediaBody(
    bytes_=open("./GPT image-2025-05-20-13_14_04.png", "rb").read(),
    filename="GPT image-2025-05-20-13_14_04.png",
    mime_type="image/png"
)
print("🚀 ~ body:", body)

# Create main content
main_content = ContentWrapper(
    content=ReportContent(
        unique_partner_id="3332323",
        body=body
    ),
    creator=ReportPerson(
        unique_partner_id="1",
        name="John Doe",
        email="as@software-design.de"
    )
)

# Create context content
context = [
    ContentWrapper(
        content=ReportContent(
            unique_partner_id="3",
            body=TextBody(text="Test")
        ),
        creator=ReportPerson(
            unique_partner_id="3",
            name="Jeff",
            email="as@software-design.de"
        )
    ),
    ContentWrapper(
        content=ReportContent(
            unique_partner_id="4",
            body=TextBody(text="katze")
        ),
        creator=ReportPerson(
            unique_partner_id="4",
            name="Sarah",
            email="as@software-design.de"
        )
    ),
    ContentWrapper(
        content=ReportContent(
            unique_partner_id="4",
            body=TextBody(text="ist toll")
        ),
        creator=ReportPerson(
            unique_partner_id="4",
            name="Sarah",
            email="as@software-design.de"
        )
    )
]

# Create reporter
reporter = ReportPerson(
    unique_partner_id="2",
    name="Jane Doe",
    email="as@software-design.de"
)

# Report content
guard_client.report(
    module_id=mid,
    module_secret=sec,
    type_id=type_id,
    main_content=main_content,
    reporter=reporter,
    options={
        "description": "HALLOOOOOO Ich bin nicht Simon",
        "reportCategory": "other",
        "userMessage": "",
        "context": context,
        "channels": []
    }
)
print("GuardClient initialized:", guard_client)

# Print class references
print("🚀 ~ ContentType:", ContentType)
print("🚀 ~ MultiMultiMediaBody:", MultiMultiMediaBody)
print("🚀 ~ MultiMediaBody:", MultiMediaBody)
print("🚀 ~ TextBody:", TextBody)
print("🚀 ~ Body:", Body)
print("🚀 ~ ContentWrapper:", ContentWrapper)
print("🚀 ~ ReportPerson:", ReportPerson)
print("🚀 ~ ReportContent:", ReportContent)