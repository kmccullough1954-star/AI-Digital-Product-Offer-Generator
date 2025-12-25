"""
Product offer templates for different digital product types.
Each template provides a structured framework for creating compelling offers.
"""

OFFER_TEMPLATES = {
    "eBook/Guide": {
        "product_type": "eBook or Guide",
        "typical_price_range": "$7-$97",
        "key_components": [
            "Clear problem statement",
            "Step-by-step solution",
            "Actionable worksheets",
            "Bonus resources"
        ],
        "monetization_models": [
            "One-time purchase",
            "Tiered pricing (basic/premium)",
            "Bundle with other products"
        ]
    },
    "Online Course": {
        "product_type": "Online Course",
        "typical_price_range": "$97-$997",
        "key_components": [
            "Module breakdown",
            "Video lessons",
            "Downloadable resources",
            "Community access",
            "Certificate of completion"
        ],
        "monetization_models": [
            "One-time purchase",
            "Payment plan (3-6 months)",
            "Subscription access",
            "Cohort-based premium pricing"
        ]
    },
    "Template Pack": {
        "product_type": "Template Pack",
        "typical_price_range": "$27-$197",
        "key_components": [
            "Multiple template variations",
            "Easy customization instructions",
            "Use case examples",
            "Editable source files"
        ],
        "monetization_models": [
            "One-time purchase",
            "Subscription for updates",
            "Commercial license upgrade"
        ]
    },
    "Coaching Program": {
        "product_type": "Coaching Program",
        "typical_price_range": "$497-$5,000+",
        "key_components": [
            "1-on-1 or group sessions",
            "Personalized action plans",
            "Accountability check-ins",
            "Resource library",
            "Private community"
        ],
        "monetization_models": [
            "Package pricing (4-12 weeks)",
            "Monthly retainer",
            "Pay-per-session",
            "VIP intensive days"
        ]
    },
    "Membership Site": {
        "product_type": "Membership Site",
        "typical_price_range": "$27-$97/month",
        "key_components": [
            "Monthly content releases",
            "Exclusive community",
            "Member-only resources",
            "Live Q&A sessions",
            "Member directory"
        ],
        "monetization_models": [
            "Monthly subscription",
            "Annual subscription (discounted)",
            "Tiered membership levels",
            "Founding member special pricing"
        ]
    },
    "Digital Tool/Software": {
        "product_type": "Digital Tool or Software",
        "typical_price_range": "$19-$99/month or one-time",
        "key_components": [
            "Core functionality",
            "User documentation",
            "Customer support",
            "Regular updates",
            "Integration options"
        ],
        "monetization_models": [
            "Monthly/annual subscription",
            "Freemium model",
            "One-time lifetime access",
            "Usage-based pricing"
        ]
    }
}


MARKETING_COPY_TEMPLATES = {
    "headline": [
        "Transform {pain_point} into {desired_outcome} in {timeframe}",
        "The Ultimate {product_type} for {target_audience}",
        "Finally! {desired_outcome} Without {common_objection}",
        "{number} Ways to {achieve_goal} Starting {timeframe}"
    ],
    "value_proposition": [
        "Get {specific_benefit} so you can {ultimate_outcome}",
        "Everything you need to {achieve_goal}, nothing you don't",
        "The only {product_type} designed specifically for {target_audience}",
        "Proven {product_type} used by {number}+ {target_audience}"
    ],
    "call_to_action": [
        "Get Instant Access Now",
        "Start Your Journey Today",
        "Download Your Copy",
        "Join {number}+ Successful {target_audience}",
        "Claim Your Spot Now"
    ]
}


LAUNCH_CHECKLIST = [
    "Create product delivery mechanism (download page, course platform, etc.)",
    "Set up payment processing (Stripe, PayPal, Gumroad, etc.)",
    "Design sales page with compelling copy",
    "Create product mockups and preview images",
    "Prepare launch email sequence (3-5 emails)",
    "Set up customer onboarding flow",
    "Create FAQ section addressing common questions",
    "Prepare social media announcement posts",
    "Set up affiliate program (optional)",
    "Create testimonial/review collection system",
    "Prepare product delivery email template",
    "Test complete purchase flow",
    "Plan post-launch follow-up sequence"
]


def get_template_info(template_type: str) -> dict:
    """Get template information for a specific product type."""
    return OFFER_TEMPLATES.get(template_type, {
        "product_type": "General Digital Product",
        "typical_price_range": "$27-$297",
        "key_components": [
            "Core content or functionality",
            "Supporting resources",
            "User guidance"
        ],
        "monetization_models": [
            "One-time purchase",
            "Subscription model"
        ]
    })
