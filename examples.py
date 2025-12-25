"""
Example usage of the AI Digital Product Offer Generator
"""

from offer_generator import OfferGenerator
import json


def example_1_ebook():
    """Example: Generate an eBook offer"""
    print("\n=== Example 1: eBook Offer ===\n")
    
    generator = OfferGenerator()
    offer = generator.generate_offer(
        idea="a guide to starting a profitable side hustle",
        niche="entrepreneurship",
        target_audience="9-5 employees wanting to earn extra income",
        template_type="eBook/Guide"
    )
    
    print(f"Product Name: {offer['product_name']}")
    print(f"Price: {offer['price_point']}")
    print(f"Value Prop: {offer['value_proposition']}")
    print(f"\nKey Benefits:")
    for benefit in offer['key_benefits']:
        print(f"  • {benefit}")


def example_2_course():
    """Example: Generate an online course offer"""
    print("\n=== Example 2: Online Course Offer ===\n")
    
    generator = OfferGenerator()
    offer = generator.generate_offer(
        idea="mastering social media marketing for small businesses",
        niche="digital marketing",
        target_audience="small business owners with limited marketing budgets",
        template_type="Online Course"
    )
    
    print(f"Product Name: {offer['product_name']}")
    print(f"Price: {offer['price_point']}")
    print(f"Value Prop: {offer['value_proposition']}")
    print(f"Product Angle: {offer['product_angle']}")


def example_3_template_pack():
    """Example: Generate a template pack offer"""
    print("\n=== Example 3: Template Pack Offer ===\n")
    
    generator = OfferGenerator()
    offer = generator.generate_offer(
        idea="professional email templates for freelancers",
        niche="freelancing",
        template_type="Template Pack"
    )
    
    print(f"Product Name: {offer['product_name']}")
    print(f"Target Audience: {offer['target_audience']}")
    print(f"Price: {offer['price_point']}")
    print(f"Monetization: {offer['monetization_model']}")


def example_4_save_to_file():
    """Example: Generate and save offer to JSON file"""
    print("\n=== Example 4: Save Offer to File ===\n")
    
    generator = OfferGenerator()
    offer = generator.generate_offer(
        idea="a productivity system for remote workers",
        niche="productivity",
        target_audience="remote professionals struggling with work-life balance",
        template_type="Template Pack"
    )
    
    filename = "example_productivity_offer.json"
    with open(filename, 'w') as f:
        json.dump(offer, f, indent=2)
    
    print(f"✓ Offer saved to: {filename}")
    print(f"Product: {offer['product_name']}")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("   AI DIGITAL PRODUCT OFFER GENERATOR - EXAMPLES")
    print("="*70)
    
    example_1_ebook()
    example_2_course()
    example_3_template_pack()
    example_4_save_to_file()
    
    print("\n" + "="*70)
    print("\nRun 'python generate_offer.py' for interactive generation!")
    print("="*70 + "\n")
