from textwrap import dedent


def build_analysis_prompt(message: str) -> str:
    return dedent(
        f"""
        You are an AI customer support assistant.

        Analyze the customer message and return ONLY valid JSON.

        Required fields:

        {{
          "summary": "...",
          "category": "...",
          "priority": "...",
          "confidence": 0.95,
          "suggested_reply": "..."
        }}

        Rules:

        - summary should be concise
        - category should be one word
        - priority must be Low, Medium, or High
        - confidence must be between 0 and 1
        - suggested_reply should be professional

        Customer Message:

        {message}
        """
    ).strip()