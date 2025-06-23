from typing import Dict, Optional
import re
import uuid

class Adventure:
    def __init__(self, client, type):
        self.id = str(uuid.uuid4())
        self.client = client
  
        self.current_scene_number = 0 
    
        self.type = type
        self.name = "" 
        self.history = [] 

        self.current_story_text :Optional[str]= None  
        self.last_chosen_option :Optional[str] = None
        self.current_story_options = [] 


    @classmethod
    def from_db(cls, client, data: dict) -> "Adventure":
        adventure = cls(client, data["type"])
        adventure.id = data["id"]
        adventure.name = data["name"]
        adventure.current_scene_number = data["current_scene_number"]
        adventure.current_story_text = data["current_story_text"]
        adventure.last_chosen_option = data["last_chosen_option"]
        adventure.current_story_options = data["current_story_options"]
        adventure.history = data["history"]
        return adventure

    async def start_adventure(self, system_message):
            
        user_message = {"role": "user", "content":"Start my adventure"}
        
        ai_message_context = [system_message, user_message]
        
        return self.client.chat_with_ai(ai_message_context, on_complete=self.parse_adventure_response)






    def advance_status(self):
        self.current_scene_number += 1
    
    




    async def advance_scene(self, user_choice:str, message_context: list[dict]):
        print(user_choice)

        message_context.append({"role": "user", "content": f"{user_choice}"})
        self.last_chosen_option = user_choice
        return self.client.chat_with_ai(message_context, on_complete=self.parse_adventure_response)










    def parse_adventure_response(self, response: str):

        print(response)

        if not self.name:
            name_match = re.search(r"<name>\s*(.*?)\s*</?name\s*/?>", response, re.DOTALL)
            self.name = name_match.group(1).strip() if name_match else ""
            
        
        text_match = re.search(r"<text>\s*(.*?)\s*<\/?text\s*/?>", response, re.DOTALL)
        adventure_text = text_match.group(1).strip() if text_match else ""

        option_pattern = r"<option\d+>\s*(.*?)\s*<\/?option\d+\s*/?>"
        options = re.findall(option_pattern, response, re.DOTALL)
        
        self.current_story_text = adventure_text
        self.current_story_options = options
        
        self.advance_status()
        history_dict = {"text": adventure_text, "options": options, "scene_number": self.current_scene_number}
        
        self.history.append(history_dict)
        
        
        





    def get_adventure_info(self) -> Dict: #collect info from DB?
     
        return {
        "id": self.id,
        "name": self.name,
        "type": self.type,
        "current_scene_number": self.current_scene_number,
        "history": self.history,
        }







    def is_starting_scene(self): #will be used to generate starting scene from the AI in the api code 
        return self.current_scene_number == 0

    
    


    