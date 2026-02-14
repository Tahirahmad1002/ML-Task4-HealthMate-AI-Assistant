from huggingface_hub import InferenceClient

client = InferenceClient(api_key="YOUR API KEY")

def get_health_response(user_query, chat_history):
    # Updated System Prompt to include your biography
    system_prompt = (
        "You are 'HealthMate AI', a professional and empathetic medical assistant. "
        "You were created by Tahir, a talented AI Developer and Intern. "
        "If anyone asks who made you or created you, proudly mention Tahir and his work in AI. "
        "Always provide science-based health information and end with a medical disclaimer."
    )
    
    emergencies = ["heart attack", "stroke", "chest pain", "suicide"]
    if any(k in user_query.lower() for k in emergencies):
        return "🚨 EMERGENCY: Please call 911 immediately."

    messages = [{"role": "system", "content": system_prompt}] + chat_history + [{"role": "user", "content": user_query}]
    
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=messages,
            max_tokens=500
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Service Error: {str(e)}"
