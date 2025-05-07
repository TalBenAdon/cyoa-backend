from typing import Tuple, List
import re
import uuid
class Adventure:
    def __init__(self, client):
        self.id = str(uuid.uuid4())
        self.client = client
        #should generate some starting story and decisions when initialized with start
        self.scene_num = 0 #maybe add an additional "starting info" to let the ai generate a different type of start?
        # maybe change status to numbers? 0 is start, and the story progresses by numbers of "scenes" generated
        self.type = ""
        self.history = [] #need to decide how to define adventure history

        self.current_story_text = None #current story text we just got from the ai (send to USER)

        self.current_story_options = [] #current story options (send to USER)







    async def start_adventure(self, type: str = "fantasy"):
        self.type = type
        system_message = {
            "role": "system",
            "content":f"""
            You are an experienced storyteller, like a D&D game master. You will adjust your storytelling style based on the type of adventure. 
            This adventure's type is: "{type}".
            
         Every reply must be formatted like this:
            <text>
            Your adventure Narration here
            </text>
            <option1>
            action the user may take
            </option1>
            <option2>
            action the user may take
            </option2>
            <option3>
            action the user may take
            </option3>
            """
            }
            
        
        user_message = {"role": "user", "content":"Start my adventure"}
        
        self.ai_message_context = [system_message, user_message]
        
        return self.client.chat_with_ai(self.ai_message_context, on_complete=self.parse_adventure_response)






    def advance_status(self):
        self.scene_num += 1
    
    




    async def advance_scene(self, user_choice):
        print(user_choice)
        user_message = {"role": "user", "content": f"{user_choice}"}
        self.ai_message_context.append(user_message)
        
        return self.client.chat_with_ai(self.ai_message_context, on_complete=self.parse_adventure_response)










    def parse_adventure_response(self, response: str) -> Tuple[str, List[str]]:
        # Extract content inside <text>...</text/>
        print(response)
        self.ai_message_context.append({"role": "assistant", "content": f"{response}"})
        
        text_match = re.search(r"<text>\s*(.*?)\s*<\/?text\s*/?>", response, re.DOTALL)
        # text_match = re.search(r"<text>\s*(.*?)\s*<text/>", response, re.DOTALL)
        adventure_text = text_match.group(1).strip() if text_match else ""
        # Extract all <optionX>...</optionX/> entries
        # option_pattern = r"<option\d+>\s*(.*?)\s*<option\d+/>"
        option_pattern = r"<option\d+>\s*(.*?)\s*<\/?option\d+\s*/?>"
        options = re.findall(option_pattern, response, re.DOTALL)
        
        # print(adventure_text)
        # print(options)
        
        self.current_story_text = adventure_text
        self.current_story_options = options
        
        self.advance_status()
        history_dict = {"text": adventure_text, "options": options, "status": self.scene_num}
        
        self.history.append(history_dict)
        
        
        # print(self.ai_message_context)
        # print(self.history)
        





    def get_adventure_info(self): #collect info from DB?
     
        return {
            "id": self.id,
        "type": self.type,
        "scene_number": self.scene_num,
        "history": self.history,
        }







    def is_starting_scene(self): #will be used to generate starting scene from the AI in the api code 
        return self.scene_num == 0

    
    


    