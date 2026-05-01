from tools.llm import call_llm

def analyze_ads(ads):
    insights = []
    for ad in ads[:5]:
        prompt = f"""
        Analyze this ad:
        {ad}

        Extract:
        - Pain point
        - Hook
        - Emotional trigger
        - CTA
        """
        result = call_llm(prompt)
        insights.append(result)

    with open("outputs/insights.txt", "w") as f:
        f.write("\n\n".join(insights))

    return insights
