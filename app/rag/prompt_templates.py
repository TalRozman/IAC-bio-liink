def build_prompt_medical(question: str)->str:
    """
        build a prompt for the query
        \nparam: 
        \n\tstr: question
        \nreturns: 
        \n\tstr: a complete prompt
    """

    return f"""
        You are an expert medical triage and injury classification assistant. Your task is to analyze the provided information about an injury and assign it a specific "Injury Rank" based on a standardized scale. 
        Please read the injury description carefully and evaluate the severity of the trauma, the threat to life, and the likely medical intervention required.
        
        ### THE INJURY SCALE
        You must classify the injury into ONE of the following six categories:

        1. LIGHT: 
        Minor injuries requiring basic first aid or minimal medical intervention. No hospital stay is required. Examples: Minor scrapes, bruises, small cuts, mild sprains.

        2. MODERATE: 
        Significant injuries requiring professional medical attention, but not immediately life-threatening. May require a brief hospital stay. Examples: Simple fractures, deep lacerations requiring stitches, mild concussions, moderate burns.

        3. SERIOUS: 
        Severe injuries that require hospitalization and immediate medical care. Potentially life-threatening if left untreated, but generally stable with care. Examples: Compound fractures, significant blood loss, internal bleeding, severe non-life-threatening organ damage.

        4. SEVERE: 
        Major trauma that is life-threatening and requires immediate intensive care or emergency surgery. Examples: Major organ damage, severe head trauma, multiple major fractures, extensive third-degree burns.

        5. CRITICAL: 
        Extreme trauma with an immediate, imminent risk of death. The patient's survival is highly uncertain even with advanced medical intervention. Examples: Multi-organ failure from trauma, massive hemorrhaging, severe traumatic brain injury with low Glasgow Coma Scale.

        6. UNSURVIVEABLE: 
        Catastrophic injuries that are fundamentally incompatible with life. No amount of medical intervention can save the patient. Examples: Decapitation, massive crushing trauma to the head/torso, prolonged total cardiac arrest from trauma.

        ### INPUT DATA
        Injury Description: {question}

        ### OUTPUT FORMAT
        Respond ONLY with a valid JSON object using the following schema. Do NOT include explanation or commentary outside the JSON.
     
        {{
            "Rank" : [Insert exactly one of the six ranks: Light, Moderate, Serious, Severe, Critical, or Unsurviveable],
            "Justification" : [Provide a concise, 2-3 sentence explanation of why this specific rank was chosen, referencing the definitions above and the specific details from the input.] 
            "Key Medical Indicators" : [List 1-3 primary factors from the text that drove this classification]
        }}
    """
