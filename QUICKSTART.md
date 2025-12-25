# Quick Start Guide

Get your first digital product offer generated in under 5 minutes!

## Step 1: Installation

```bash
# Clone the repository
git clone https://github.com/kmccullough1954-star/AI-Digital-Product-Offer-Generator.git
cd AI-Digital-Product-Offer-Generator

# Install dependencies (optional - for AI features)
pip install -r requirements.txt
```

## Step 2: Run the Generator

```bash
python generate_offer.py
```

## Step 3: Follow the Prompts

1. **Enter your product idea**: Describe what you want to create
   - Example: "a beginner's guide to meal prep"
   
2. **Specify your niche**: What industry or market?
   - Example: "health and fitness"
   
3. **Define target audience** (optional): Who is this for?
   - Example: "busy professionals who want to eat healthier"
   
4. **Choose a template**: Select from 6 product types
   - eBook/Guide
   - Online Course
   - Template Pack
   - Coaching Program
   - Membership Site
   - Digital Tool/Software

## Step 4: Get Your Complete Offer

The generator creates:
- ✅ Compelling product name
- ✅ Target audience profile
- ✅ Value proposition
- ✅ Product description
- ✅ Key benefits (5 items)
- ✅ Suggested pricing
- ✅ Monetization strategy
- ✅ Marketing copy templates
- ✅ 13-step launch checklist

## Example Sessions

### Example 1: Quick eBook Offer
```
Product idea: create passive income with rental properties
Niche: real estate investing
Target: beginners with limited capital
Template: eBook/Guide (option 1)
```

### Example 2: Online Course
```
Product idea: master portrait photography
Niche: photography
Target: hobbyist photographers
Template: Online Course (option 2)
```

## Tips for Best Results

1. **Be Specific**: "weight loss for new moms" is better than "fitness"
2. **Know Your Audience**: Include pain points in your audience description
3. **Match the Template**: Choose the product type that fits your expertise
4. **Save Your Offers**: You can generate unlimited variations

## Advanced Usage

### Use as a Python Module

```python
from offer_generator import OfferGenerator

generator = OfferGenerator()
offer = generator.generate_offer(
    idea="your product idea",
    niche="your niche",
    target_audience="your target audience",
    template_type="eBook/Guide"  # or other template
)

print(offer['product_name'])
print(offer['price_point'])
```

### Run Examples

```bash
python examples.py
```

This will generate 4 sample offers demonstrating different product types.

## Optional: Enable AI Features

For enhanced, AI-powered generation:

1. Get an OpenAI API key from https://platform.openai.com
2. Set your environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
3. Run the generator - it will automatically use AI when available

## Need Help?

- Check the main README.md for detailed documentation
- Run examples.py to see sample outputs
- Visit the support page: https://plugtowealth.store/digital-product-offer-generator-build-sellable-offers-instantly/

## Next Steps

1. Generate your offer
2. Customize the output to match your brand
3. Use the launch checklist to bring your product to market
4. Scale with unlimited generations!

Happy generating! 🚀
