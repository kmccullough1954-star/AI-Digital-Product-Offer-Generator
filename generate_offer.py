#!/usr/bin/env python3
"""
AI Digital Product Offer Generator
Main entry point for generating structured, sellable digital product offers.
"""

import sys
import json
from typing import Dict, Optional
from offer_generator import OfferGenerator
from templates import OFFER_TEMPLATES
from config import (
    APP_NAME,
    APP_TAGLINE,
    PREMIUM_URL,
    DEFAULT_NICHE,
    DEFAULT_SAVE_FILENAME,
    BANNER_WIDTH,
    SECTION_WIDTH
)


def print_banner():
    """Print the application banner."""
    print("\n" + "="*BANNER_WIDTH)
    print(f"   {APP_NAME.upper()}")
    print(f"   {APP_TAGLINE}")
    print("="*BANNER_WIDTH + "\n")


def get_user_input(prompt: str, default: Optional[str] = None) -> str:
    """Get input from user with optional default value."""
    if default:
        prompt = f"{prompt} (default: {default}): "
    else:
        prompt = f"{prompt}: "
    
    user_input = input(prompt).strip()
    return user_input if user_input else (default or "")


def select_template() -> str:
    """Allow user to select a product template."""
    print("\nAvailable Product Templates:")
    templates = list(OFFER_TEMPLATES.keys())
    for i, template in enumerate(templates, 1):
        print(f"  {i}. {template}")
    
    while True:
        try:
            choice = input("\nSelect a template (1-{}), or press Enter to skip: ".format(len(templates)))
            if not choice:
                return "general"
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(templates):
                return templates[choice_num - 1]
            else:
                print(f"Please enter a number between 1 and {len(templates)}")
        except ValueError:
            print("Please enter a valid number")


def display_offer(offer: Dict):
    """Display the generated offer in a formatted way."""
    print("\n" + "="*SECTION_WIDTH)
    print("   YOUR DIGITAL PRODUCT OFFER")
    print("="*SECTION_WIDTH + "\n")
    
    sections = [
        ("Product Name", "product_name"),
        ("Target Audience", "target_audience"),
        ("Value Proposition", "value_proposition"),
        ("Product Description", "description"),
        ("Product Angle", "product_angle"),
        ("Key Benefits", "key_benefits"),
        ("Price Point", "price_point"),
        ("Monetization Model", "monetization_model"),
        ("Marketing Copy", "marketing_copy"),
        ("Launch Checklist", "launch_checklist")
    ]
    
    for section_name, key in sections:
        if key in offer and offer[key]:
            print(f"\n{section_name}:")
            print("-" * SECTION_WIDTH)
            value = offer[key]
            if isinstance(value, list):
                for item in value:
                    print(f"  • {item}")
            elif isinstance(value, dict):
                for k, v in value.items():
                    print(f"  {k.replace('_', ' ').title()}: {v}")
            else:
                print(f"  {value}")
    
    print("\n" + "="*SECTION_WIDTH + "\n")


def save_offer(offer: Dict, filename: str = "generated_offer.json"):
    """Save the generated offer to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(offer, f, indent=2)
        print(f"\n✓ Offer saved to: {filename}")
    except Exception as e:
        print(f"\n✗ Error saving offer: {e}")


def main():
    """Main application flow."""
    print_banner()
    
    # Gather user inputs
    print("Let's create your digital product offer!\n")
    
    idea = get_user_input("What's your product idea?")
    if not idea:
        print("Product idea is required. Exiting.")
        sys.exit(1)
    
    niche = get_user_input("What's your niche or industry?", DEFAULT_NICHE)
    target_audience = get_user_input("Who is your target audience? (optional)")
    template_type = select_template()
    
    # Generate the offer
    print("\n⏳ Generating your digital product offer...\n")
    
    generator = OfferGenerator()
    offer = generator.generate_offer(
        idea=idea,
        niche=niche,
        target_audience=target_audience,
        template_type=template_type
    )
    
    # Display the results
    display_offer(offer)
    
    # Ask if user wants to save
    save_choice = get_user_input("Would you like to save this offer? (y/n)", "y").lower()
    if save_choice in ['y', 'yes']:
        filename = get_user_input("Enter filename", DEFAULT_SAVE_FILENAME)
        if not filename.endswith('.json'):
            filename += '.json'
        save_offer(offer, filename)
    
    print(f"\n✨ Thank you for using {APP_NAME}!")
    print("For unlimited generations and premium features, visit:")
    print(f"{PREMIUM_URL}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ An error occurred: {e}")
        sys.exit(1)
