from mongoengine import *
import mlab_1
from ex2_class import PushHobby 


mlab_1.connect()
Hobbies={
    "Ancient Rome philosophy": 
        {
            "information": """Two major philosophical schools of thought in Rome in the 1st and 2nd century AD was Cynicism and Stoicism. 
                            Cynicism taught that civilization was corrupt and people needed to break away from it and its trappings 
                            Stoicism taught that one must give up all earthly goods by remaining detached from civilization and help others.""",
            "pics":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Forum_Romanum_panorama_2.jpg/600px-Forum_Romanum_panorama_2.jpg",
            'link': "https://www.youtube.com/watch?v=yu7n0XzqtfA"
        },
    "Materialism":
        {
            "information":  """Materialism is a form of philosophical monism which holds that matter is the fundamental substance in nature, 
                            and that all things, including mental aspects and consciousness, are results of material interactions.""",
            "pics": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoyOZhn4oUgeDX9DBJcoYwLThJgFpG2A7LWp22cEOrL_SKpOeF",
            "link": "https://en.wikipedia.org/wiki/Materialism"
        },
    "Marxist philosophy":
        {
            "information": ''' Marx's works can be divided into "economic works" , "philosophical works" and "historical works" ... ''',
            "pics": "data:image/jpeg;base64,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",
            "link": "https://en.wikipedia.org/wiki/Marxism"
        }
    }     
for hobby in Hobbies:
    post_hobby=PushHobby(name=hobby,info=Hobbies[hobby]["information"],pics=Hobbies[hobby]["pics"],link=Hobbies[hobby]["link"])
    post_hobby.save()  