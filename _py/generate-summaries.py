import random
import yaml
import os

# Original base paragraphs
base_para1 = (
    "With over {years} years of experience specializing in API integration, particularly with technologies like MuleSoft, "
    "I have {verb1} strong skills in software development. Along the way, I've earned industry-recognized certifications, "
    "including those in MuleSoft Development and Anypoint Platform Architecture. While MuleSoft has been central to my career, "
    "my experience extends beyond it. In my current organization, I am also an \"Elevated Wings1 Certified - Full-Stack JavaScript Developer (MERN),\" "
    "a program that deepened my expertise in integration patterns using JavaScript."
)

base_para2 = (
    "Automation has {verb2} to my success, especially in testing—be it {test_type} testing. "
    "I'm well-versed in various architectural patterns, including {patterns}. {connect_phrase}"
)

# Variants to inject randomness
verbs_para1 = ["developed", "refined", "honed", "strengthened", "built"]
verbs_para2 = ["been crucial", "played a vital role", "contributed significantly", "been instrumental", "helped drive"]
test_types = ["unit and integration", "automated", "integration and regression", "performance and functional", "unit, integration, and system"]
patterns = ["ETL, event-driven, and message queue", "ETL, real-time, and async Pub/Sub", "batch and real-time streaming", "ETL and microservices", "Pub/Sub and streaming pipelines"]
connect_phrases = ["I'd be happy to connect!", "Let’s get in touch!", "Please feel free to reach out!", "Open to new opportunities—feel free to connect!", "Happy to discuss potential projects!"]

# Generate 100 summaries
summaries = []
for _ in range(100):
    para1 = base_para1.format(
        years="{years}",
        verb1=random.choice(verbs_para1)
    )

    para2 = base_para2.format(
        verb2=random.choice(verbs_para2),
        test_type=random.choice(test_types),
        patterns=random.choice(patterns),
        connect_phrase=random.choice(connect_phrases)
    )

    summaries.append(f"- >\n  {para1}\n  \n  {para2}")

# Ensure output folder exists
os.makedirs("_data", exist_ok=True)

# Write to YAML file
with open("_data/summaries.yml", "w") as f:
    f.write("summaries:\n")
    for summary in summaries:
        f.write(summary + "\n")

print("Generated 100 CV summaries with dynamic {years} tag and saved to _data/summaries.yml")