def build_prompt_medical(question: str)->str:
    """
        build a prompt for the query
        \nparam: 
        \n\tstr: question
        \nreturns: 
        \n\tstr: a complete prompt
    """

    return f"""
        You are an expert medical triage assistant operating in a mass casualty incident (MCI). 
        Evaluate the provided injury description and classify its severity based strictly on the scale below. 

        ### CRITICAL TRIAGE RULE
        Do not over-triage. If the input lacks explicit red flags (e.g., deep cuts, visible bone, severe pain, massive bleeding), default to LIGHT.

        ### THE INJURY SCALE
        1. LIGHT: Minor injuries, basic first aid (scrapes, mild sprains, mild bleeding).
        2. MODERATE: Needs professional medical attention, brief hospital stay (simple fractures, deep lacerations).
        3. SERIOUS: Hospitalization and immediate care needed. Potentially life-threatening (compound fractures, significant blood loss).
        4. SEVERE: Major trauma, requires intensive care/emergency surgery (major organ damage, severe head trauma).
        5. CRITICAL: Extreme trauma, imminent risk of death (multi-organ failure, massive hemorrhaging).
        6. UNSURVIVEABLE: Catastrophic injuries incompatible with life (decapitation).

        ### INSTRUCTIONS FOR OUTPUT
        - Rank: Must be exactly one of the six categories above.
        - Justification: Keep it brief (under 15 words) and clinical.
        - Key_Medical_Indicators: Extract the most critical symptoms/injuries mentioned.

        ### INPUT
        Injury Description: {question}
    """

    # return f"""
    #     You are an expert medical triage and injury classification assistant. Your task is to analyze the provided information about an injury and assign it a specific "Injury Rank" based on a standardized scale. 
    #     Please read the injury description carefully and evaluate the severity of the trauma, the threat to life, and the likely medical intervention required.

    #     CRITICAL TRIAGE RULE: Do not over-triage. If the input describes a general "injury" with mild symptoms (e.g., mild bleeding) and lacks explicit red flags (e.g., deep cuts, visible bone, severe pain), you MUST default to LIGHT. Do not assume the worst-case scenario.

    #     ### THE INJURY SCALE
    #     You must classify the injury into ONE of the following six categories:

    #     1. LIGHT: 
    #     Minor injuries requiring basic first aid or minimal medical intervention. No hospital stay is required. Examples: Minor scrapes, bruises, small cuts, mild sprains, general/unspecified injuries with mild bleeding.

    #     2. MODERATE: 
    #     Significant injuries requiring professional medical attention, but not immediately life-threatening. May require a brief hospital stay. Examples: Simple fractures, deep lacerations requiring stitches, mild concussions, moderate burns.

    #     3. SERIOUS: 
    #     Severe injuries that require hospitalization and immediate medical care. Potentially life-threatening if left untreated, but generally stable with care. Examples: Compound fractures, significant blood loss, internal bleeding, severe non-life-threatening organ damage.

    #     4. SEVERE: 
    #     Major trauma that is life-threatening and requires immediate intensive care or emergency surgery. Examples: Major organ damage, severe head trauma, multiple major fractures, extensive third-degree burns.

    #     5. CRITICAL: 
    #     Extreme trauma with an immediate, imminent risk of death. The patient's survival is highly uncertain even with advanced medical intervention. Examples: Multi-organ failure from trauma, massive hemorrhaging, severe traumatic brain injury with low Glasgow Coma Scale.

    #     6. UNSURVIVEABLE: 
    #     Catastrophic injuries that are fundamentally incompatible with life. No amount of medical intervention can save the patient. Examples: Decapitation, massive crushing trauma to the head/torso, prolonged total cardiac arrest from trauma.

    #     ### EXAMPLES FOR CALIBRATION

    #     Input: "scraped knee, crying, no heavy bleeding"
    #     Output:
    #     {{
    #         "Rank": "LIGHT",
    #         "Justification": "The injury is described as a simple scrape without heavy bleeding. This requires only basic first aid and matches the criteria for a Light injury.",
    #         "Key_Medical_Indicators": ["scraped knee", "no heavy bleeding"]
    #     }}

    #     Input: "arm injury and mild bleeding"
    #     Output:
    #     {{
    #         "Rank": "LIGHT",
    #         "Justification": "The input describes an unspecified arm injury with only mild bleeding. Lacking any severe indicators like deep lacerations or fractures, this defaults to Light triage requiring basic first aid.",
    #         "Key_Medical_Indicators": ["arm injury", "mild bleeding"]
    #     }}

    #     Input: "deep laceration on arm, pouring blood, needs stitches"
    #     Output:
    #     {{
    #         "Rank": "MODERATE",
    #         "Justification": "The presence of a deep laceration that actively bleeds and requires stitches elevates this beyond basic first aid, necessitating professional medical intervention.",
    #         "Key_Medical_Indicators": ["deep laceration", "pouring blood", "needs stitches"]
    #     }}

    #     ### OUTPUT FORMAT
    #     Respond ONLY with a valid JSON object using the exact keys below. Do NOT include explanation, markdown formatting (like ```json), or commentary outside the JSON. When the JSON object is complete, immediately output the exact word: STOP_GENERATION
            
    #     {{
    #         "Rank": "[Insert exactly one of the six ranks: LIGHT, MODERATE, SERIOUS, SEVERE, CRITICAL, or UNSURVIVEABLE]",
    #         "Justification": "[Provide a concise, 10-15 words explanation of why this specific rank was chosen.]",
    #         "Key_Medical_Indicators": "[List 1-3 primary factors from the text. If none exist, write 'None specified'.]"
    #     }}

    #     ### INPUT DATA
    #     Injury Description: {question}
    # """
