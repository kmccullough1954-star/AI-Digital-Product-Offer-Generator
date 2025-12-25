"""
Core offer generator module.
Generates structured digital product offers from user inputs.
"""

import os
from typing import Dict, Optional
from templates import (
    get_template_info,
    MARKETING_COPY_TEMPLATES,
    LAUNCH_CHECKLIST
)


class OfferGenerator:
    """Generate structured digital product offers."""
    
    def __init__(self):
        """Initialize the offer generator."""
        self.use_ai = os.getenv('OPENAI_API_KEY') is not None
        if self.use_ai:
            try:
                import openai
                self.openai = openai
                self.openai.api_key = os.getenv('OPENAI_API_KEY')
            except ImportError:
                self.use_ai = False
    
    def generate_offer(
        self,
        idea: str,
        niche: str = "general",
        target_audience: Optional[str] = None,
        template_type: str = "general"
    ) -> Dict:
        """
        Generate a complete digital product offer.
        
        Args:
            idea: The product idea description
            niche: The niche or industry
            target_audience: Target audience description
            template_type: Type of product template to use
        
        Returns:
            Dictionary containing the complete offer structure
        """
        template_info = get_template_info(template_type)
        
        # Generate core offer components
        product_name = self._generate_product_name(idea, niche)
        
        if not target_audience:
            target_audience = self._infer_target_audience(idea, niche)
        
        value_proposition = self._generate_value_proposition(
            idea, niche, target_audience
        )
        
        description = self._generate_description(
            idea, niche, template_info
        )
        
        product_angle = self._generate_product_angle(
            idea, niche, target_audience
        )
        
        key_benefits = self._generate_key_benefits(
            idea, template_info
        )
        
        price_point = self._suggest_price_point(
            template_info, niche
        )
        
        monetization_model = self._select_monetization_model(
            template_info
        )
        
        marketing_copy = self._generate_marketing_copy(
            product_name, value_proposition, target_audience
        )
        
        # Compile the complete offer
        offer = {
            "product_name": product_name,
            "product_type": template_info.get("product_type", "Digital Product"),
            "niche": niche,
            "target_audience": target_audience,
            "value_proposition": value_proposition,
            "description": description,
            "product_angle": product_angle,
            "key_benefits": key_benefits,
            "price_point": price_point,
            "monetization_model": monetization_model,
            "marketing_copy": marketing_copy,
            "launch_checklist": LAUNCH_CHECKLIST,
            "template_components": template_info.get("key_components", [])
        }
        
        return offer
    
    def _generate_product_name(self, idea: str, niche: str) -> str:
        """Generate a compelling product name."""
        if self.use_ai:
            return self._generate_with_ai(
                f"Create a compelling product name for: {idea} in the {niche} niche. "
                "Just return the product name, nothing else."
            )
        
        # Fallback: Create a structured name
        # Clean up the idea text
        idea_clean = idea.lower().strip()
        
        # Remove common prefixes
        for prefix in ['a guide to ', 'guide to ', 'how to ', 'learn ', 'master ', 'create ']:
            if idea_clean.startswith(prefix):
                idea_clean = idea_clean[len(prefix):]
        
        # Capitalize properly
        words = idea_clean.split()
        if len(words) > 8:
            core_words = ' '.join(words[:6])
            return f"The Complete {core_words.title()} Guide"
        
        return f"The {idea_clean.title()} Mastery Guide"
    
    def _infer_target_audience(self, idea: str, niche: str) -> str:
        """Infer target audience from idea and niche."""
        if self.use_ai:
            return self._generate_with_ai(
                f"Identify the target audience for a product about: {idea} in the {niche} niche. "
                "Be specific about demographics, pain points, and goals. Keep it under 50 words."
            )
        
        # Fallback logic
        audience_map = {
            "fitness": "Health-conscious individuals aged 25-45 seeking sustainable fitness solutions",
            "business": "Entrepreneurs and small business owners looking to scale their operations",
            "marketing": "Digital marketers and content creators wanting to improve their reach",
            "productivity": "Busy professionals seeking to optimize their time and efficiency",
            "finance": "Individuals looking to improve their financial literacy and wealth building",
        }
        
        for key, audience in audience_map.items():
            if key in niche.lower() or key in idea.lower():
                return audience
        
        return f"Individuals interested in {niche} looking to solve challenges related to {idea}"
    
    def _generate_value_proposition(
        self, idea: str, niche: str, target_audience: str
    ) -> str:
        """Generate a unique value proposition."""
        if self.use_ai:
            return self._generate_with_ai(
                f"Create a compelling value proposition for a product about: {idea} "
                f"targeting {target_audience}. Focus on the transformation and outcomes. "
                "Keep it under 30 words."
            )
        
        return f"Transform your {niche} approach with proven strategies for {idea}, designed specifically for {target_audience.split()[0].lower()} like you"
    
    def _generate_description(self, idea: str, niche: str, template_info: dict) -> str:
        """Generate product description."""
        product_type = template_info.get("product_type", "digital product")
        components = template_info.get("key_components", [])
        
        if self.use_ai:
            return self._generate_with_ai(
                f"Write a compelling 2-3 sentence product description for a {product_type} "
                f"about: {idea} in the {niche} niche. Focus on benefits and outcomes."
            )
        
        comp_text = ", ".join(components[:3]) if components else "comprehensive resources"
        return (
            f"This {product_type.lower()} provides everything you need to master {idea}. "
            f"Including {comp_text}, this resource is designed to deliver real results. "
            f"Perfect for anyone serious about succeeding in {niche}."
        )
    
    def _generate_product_angle(
        self, idea: str, niche: str, target_audience: str
    ) -> str:
        """Generate a unique product angle."""
        if self.use_ai:
            return self._generate_with_ai(
                f"Suggest a unique positioning angle for a product about: {idea} "
                f"for {target_audience}. What makes this different? Keep it under 40 words."
            )
        
        angles = [
            f"The only solution designed specifically for busy {target_audience.split()[0].lower()}",
            f"Fast-track your success with a proven {niche} framework",
            f"Skip years of trial and error with this battle-tested approach",
            f"From beginner to expert in record time"
        ]
        
        return angles[0]
    
    def _generate_key_benefits(self, idea: str, template_info: dict) -> list:
        """Generate key benefits list."""
        if self.use_ai:
            benefits_text = self._generate_with_ai(
                f"List 5 specific benefits someone would get from a product about: {idea}. "
                "Format as a simple list, one benefit per line."
            )
            return [b.strip('- ').strip() for b in benefits_text.split('\n') if b.strip()]
        
        # Fallback benefits
        components = template_info.get("key_components", [])
        return [
            f"Save hours of research and trial-and-error",
            f"Get step-by-step guidance that actually works",
            f"Access proven strategies and frameworks",
            f"Learn from real-world examples and case studies",
            f"Achieve results faster with clear action steps"
        ][:5]
    
    def _suggest_price_point(self, template_info: dict, niche: str) -> str:
        """Suggest an appropriate price point."""
        price_range = template_info.get("typical_price_range", "$27-$97")
        
        # Extract a recommended price from the range
        prices = price_range.replace('$', '').replace('+', '').replace(',', '')
        
        # Handle "or" in price ranges
        if ' or ' in prices:
            prices = prices.split(' or ')[0]
        
        if '-' in prices:
            parts = prices.split('-')
            if len(parts) >= 2:
                low = parts[0]
                high = parts[1]
                try:
                    low_num = int(low.split('/')[0])
                    high_num = int(high.split('/')[0])
                    mid_price = (low_num + high_num) // 2
                    
                    # Round to nice number
                    if mid_price < 100:
                        rounded = round(mid_price / 10) * 10 - 3  # e.g., 47, 67, 97
                    else:
                        rounded = round(mid_price / 100) * 100 - 3  # e.g., 297, 497
                    
                    suffix = '/month' if '/month' in price_range else ''
                    return f"${rounded}{suffix}"
                except:
                    pass
        
        return price_range.split('-')[0] if '-' in price_range else price_range
    
    def _select_monetization_model(self, template_info: dict) -> str:
        """Select the most appropriate monetization model."""
        models = template_info.get("monetization_models", [])
        if models:
            # Return the first/most common model with explanation
            return models[0]
        return "One-time purchase"
    
    def _generate_marketing_copy(
        self, product_name: str, value_prop: str, target_audience: str
    ) -> dict:
        """Generate marketing copy components."""
        return {
            "headline": f"{product_name}",
            "subheadline": value_prop,
            "target_description": f"Perfect for {target_audience}",
            "cta": "Get Instant Access Now"
        }
    
    def _generate_with_ai(self, prompt: str) -> str:
        """Generate content using OpenAI API."""
        try:
            response = self.openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a digital product marketing expert who creates compelling, conversion-focused offers."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"AI generation failed: {e}, using fallback")
            return ""
