class AdventureSnapshot:
    def __init__(self, adventure_id: str, type: str, scene_number: int, history ):
        self.id = adventure_id
        self.type = type
        self.scene_number = scene_number
        self.history = history