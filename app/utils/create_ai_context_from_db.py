from app.utils.get_system_message import get_system_message
def create_ai_context_from_db(type, history_rows):
    ai_context = [get_system_message(type)]
    for row in history_rows:
        
        assistant_content = row["scene_text"]
        user_content = row.get("chosen_option")
        
        ai_context.append({
            "role": "assistant",
            "content": assistant_content
        })
        
        
       
        if user_content is None:
            break
        
        
        ai_context.append(user_message = {
            "role": "user",
            "content": user_content
        })
        
   
    return ai_context
        
    
    
    
    