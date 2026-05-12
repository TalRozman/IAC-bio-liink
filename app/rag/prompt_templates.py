def build_prompt_medical(question: str) -> str:
    """
    Optimized for 1B models using Ollama JSON Schema. 
    Uses plain-text examples to teach logic without confusing the JSON parser.
    """
    return f"""You are an AI medical triage system. Read the patient's injuries and classify the severity.

        ### INJURY SCALE
        1. LIGHT: Minor injuries.
        2. MODERATE: Needs professional attention.
        3. SERIOUS: Hospitalization needed.
        4. SEVERE: Major trauma.
        5. CRITICAL: Extreme trauma, imminent risk of death.
        6. UNSURVIVEABLE: Catastrophic injuries (or explicitly labeled unsurviveable).

        ### STRICT RULES
        1. If ANY injury contains the word "unsurviveable", the Rank MUST exactly be UNSURVIVEABLE.
        2. Extract the FULL phrase of the injury (e.g., "unsurviveable chest injury"). Do not split it into single words.
        3. Identify the single worst injury as the Primary_Severe_Injury.

        ### EXAMPLES

        Input: The patient has been diagnosed with light head injury, unsurviveable left-hand injury.
        Primary_Severe_Injury: unsurviveable left-hand injury
        Rank: UNSURVIVEABLE
        Justification: The unsurviveable left-hand injury dictates the maximum rank.
        Key_Medical_Indicators: ["light head injury", "unsurviveable left-hand injury"]

        Input: The patient has been diagnosed with moderate right-thigh injury, severe abdomen injury.
        Primary_Severe_Injury: severe abdomen injury
        Rank: SEVERE
        Justification: The severe abdomen injury is the most critical trauma present.
        Key_Medical_Indicators: ["moderate right-thigh injury", "severe abdomen injury"]

        ### PATIENT INPUT
        {question}
    """