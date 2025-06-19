from app.utils.get_system_message import get_system_message
def create_ai_context_from_db(history_rows): #TODO Complete it
    ai_context = [get_system_message()]
    for row in history_rows:
        
        assistant_content = row["scene_text"]
        user_content = row.get("chosen_option")
        
        assistant_message = {
            "role": "assistant",
            "content": assistant_content
        }
        
        user_message = {
            "role": "user",
            "content": user_content
        }
        
        ai_context.append(assistant_message)
        if user_content == None:
            break
        ai_context.append(user_message)
        
    return ai_context
        
    
    
    print(f"{history_rows}")
    