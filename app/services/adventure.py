class Adventure:
    def __init__(self, type : str = "fantasy"):
        #should generate some starting story and decisions when initialized with start
        self.status = 0 #maybe add an additional "starting info" to let the ai generate a different type of start?
        # maybe change status to numbers? 0 is start, and the story progresses by numbers of "scenes" generated

        self.type = type # type of the adventure (slice of life, fantasy, etc..)

        self.history = [] #need to decide how to define adventure history

        self.current_story_text = None #current story text we just got from the ai (send to USER)

        self.current_story_options = {} #current story options (send to USER)

    def get_adventure_info(self): #collect info from DB?
        return {
        "type": self.type,
        "status": self.status,
        "history": self.history,
        }


    def is_starting_scene(self): #will be used to generate starting scene from the AI in the api code 
        return self.status == 0

    
    


    