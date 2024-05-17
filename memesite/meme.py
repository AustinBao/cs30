class Meme:
    def __init__(self, image_path, name, description, year, source):
        self.image_path = image_path
        self.name = name
        self.description = description
        self.year = year
        self.source = source

    def save_to_db(self, db_collection):
        meme_data = {
            'image_path': self.image_path,
            'name': self.name,
            'description': self.description,
            'year': self.year,
            'source': self.source
        }
        db_collection.insert_one(meme_data)