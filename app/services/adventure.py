
class Adventure:
    def __init__(self, client):
        self.client = client
        #should generate some starting story and decisions when initialized with start
        self.status = 0 #maybe add an additional "starting info" to let the ai generate a different type of start?
        # maybe change status to numbers? 0 is start, and the story progresses by numbers of "scenes" generated
        self.type = ""
        self.history = [] #need to decide how to define adventure history

        self.current_story_text = None #current story text we just got from the ai (send to USER)

        self.current_story_options = {} #current story options (send to USER)

    async def start_adventure(self, type: str = "fantasy"):
        self.type = type
        system_message = f"""
            You are an experienced storyteller, like a D&D game master. You will adjust your storytelling style based on the type of adventure. 
            This adventure's type is: "{type}".
            
         Every reply must be formatted like this:
            <text>
            Your adventure Narration here
            <text/>
            <option1>
            action the user may take
            <option1/>
            <option2>
            action the user may take
            <option2/>
            <option3>
            action the user may take
            <option3/>
            """
            
            
        user_message = "Start my adventure"
        return self.client.chat_with_ai(system_message, user_message)

    def advance_scene(self):
        self.history.append({
            "status":self.status
        })

    def get_adventure_info(self): #collect info from DB?
     
        return {
        "type": self.type,
        "status": self.status,
        "history": self.history,
        }


    def is_starting_scene(self): #will be used to generate starting scene from the AI in the api code 
        return self.status == 0

    
    


    