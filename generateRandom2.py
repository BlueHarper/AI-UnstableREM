import random
import json


def get_random_element(json_list):
    """
    Returns a random element from a list of JSON objects.

    Args:
        json_list: A list of dictionaries (JSON objects)

    Returns:
        A randomly selected dictionary from the list, or None if list is empty
    """
    if not json_list:
        return None

    return random.choice(json_list)


data = [
    {
        "mood": "un憋住一条 Creek",
        "seed_hint": "sunshine_and_light_breeze",
        "steps": [
            {"action": "setSkybox", "args": {"skyBoxType": "EveningSky"}},
            {"action": "setBackgroundSong", "args": {"songType": "Classy"}},
            {
                "action": "setLightingSimple",
                "args": {
                    "ambientR": 125,
                    "ambientG": 150,
                    "ambientB": 190,
                    "outdoorR": 90,
                    "outdoorG": 105,
                    "outdoorB": 128,
                    "brightness": 1.8,
                    "clockTime": 20,
                    "fogStart": 50,
                    "fogEnd": 10000,
                    "fogR": 100,
                    "fogG": 115,
                    "fogB": 160,
                },
            },
            {
                "action": "fillTerrainBlock",
                "args": {
                    "posX": 0,
                    "posY": 0,
                    "posZ": 0,
                    "sizeX": 128,
                    "sizeY": 5,
                    "sizeZ": 128,
                    "material": "Grass",
                },
            },
            {
                "action": "addParticles",
                "args": {
                    "posX": 0,
                    "posY": 20,
                    "posZ": 0,
                    "texture": "rbxasset://textures/particles/smoke_main.dds",
                    "rate": 50,
                    "lifetime": 6,
                    "size": 1.2,
                },
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "LightOrb",
                    "posX": 10,
                    "posY": 50,
                    "posZ": 10,
                    "sizeX": 2,
                    "sizeY": 4,
                    "sizeZ": 2,
                    "colorR": 255,
                    "colorG": 210,
                    "colorB": 80,
                    "anchored": "true",
                    "material": "Glass",
                },
            },
            {
                "action": "spawnCluster",
                "args": {
                    "partType": "Crystal",
                    "centerposX": 16,
                    "centerposY": 10,
                    "centerposZ": 16,
                    "count": 8,
                    "radius": 4,
                },
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "Crystal",
                    "posX": 32,
                    "posY": 80,
                    "posZ": 32,
                    "sizeX": 8,
                    "sizeY": 16,
                    "sizeZ": 8,
                    "colorR": 239,
                    "colorG": 41,
                    "colorB": 41,
                    "anchored": "true",
                    "material": "DiamondPlate",
                },
            },
            {
                "action": "floatPart",
                "args": {
                    "partType": "LightOrb",
                    "posX": -16,
                    "posY": 50,
                    "posZ": -16,
                    "sizeX": 2,
                    "sizeY": 4,
                    "sizeZ": 2,
                    "colorR": 255,
                    "colorG": 210,
                    "colorB": 80,
                    "anchored": "true",
                    "material": "Glass",
                    "amplitude": 1.8,
                    "speed": 0.8,
                },
            },
            {
                "action": "spawnCluster",
                "args": {
                    "partType": "Normal",
                    "centerposX": -32,
                    "centerposY": 10,
                    "centerposZ": -32,
                    "count": 12,
                    "radius": 6,
                },
            },
            {
                "action": "addDialogueCharacter",
                "args": {
                    "tone": "Friendly",
                    "posX": 0,
                    "posY": 30,
                    "posZ": 0,
                    "initialdialogue": "Welcome, traveler! What brings you to the edge of the Creek?",
                    "dialogue1": "I'm looking for help.",
                    "dialogue1response": "Ah, you've come at the right time. Tell me what you need.",
                    "dialogue2": "Is this place safe?",
                    "dialogue2response": "Only if you keep your eyes open.",
                },
            },
            {
                "action": "addAssetProps",
                "args": {"prop": "Sign_01", "posX": 20, "posY": 26, "posZ": 0},
            },
            {
                "action": "addBrainRot",
                "args": {"rot": "a9", "posX": 8, "posY": 0, "posZ": 0},
            },
            {
                "action": "spawnCluster",
                "args": {
                    "partType": "CapitalOneSign",
                    "centerposX": 56,
                    "centerposY": 10,
                    "centerposZ": 56,
                    "count": 6,
                    "radius": 5,
                },
            },
        ],
    },
    {
        "mood": "Ethereal and nostalgic",
        "seed_hint": "Clockwork dreams in bleeding midnight light",
        "steps": [
            {"action": "setSkybox", "args": {"skyBoxType": "EveningSky"}},
            {
                "action": "setLightingSimple",
                "args": {
                    "ambientR": 25,
                    "ambientG": 20,
                    "ambientB": 25,
                    "outdoorR": 120,
                    "outdoorG": 100,
                    "outdoorB": 210,
                    "brightness": 1,
                    "clockTime": 22.5,
                    "fogStart": 100,
                    "fogEnd": 3000,
                    "fogR": 25,
                    "fogG": 20,
                    "fogB": 25,
                },
            },
            {"action": "setBackgroundSong", "args": {"songType": "Dream"}},
            {
                "action": "fillTerrainBlock",
                "args": {
                    "posX": 0,
                    "posY": 0,
                    "posZ": 0,
                    "sizeX": 128,
                    "sizeY": 128,
                    "sizeZ": 20,
                    "material": "Neon",
                },
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": 16,
                    "posY": 10,
                    "posZ": 0,
                    "sizeX": 64,
                    "sizeY": 15,
                    "sizeZ": 32,
                    "colorR": 135,
                    "colorG": 206,
                    "colorB": 235,
                    "anchored": "true",
                    "material": "CrackedLava",
                },
            },
            {
                "action": "spawnCluster",
                "args": {
                    "partType": "LightOrb",
                    "centerposX": 32,
                    "centerposY": 10,
                    "centerposZ": 0,
                    "count": 8,
                    "radius": 10,
                },
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": 16,
                    "posY": 8,
                    "posZ": 16,
                    "sizeX": 32,
                    "sizeY": 5,
                    "sizeZ": 16,
                    "colorR": 173,
                    "colorG": 216,
                    "colorB": 230,
                    "anchored": "true",
                    "material": "Poisson",
                },
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": 80,
                    "posY": 10,
                    "posZ": 0,
                    "sizeX": 64,
                    "sizeY": 15,
                    "sizeZ": 32,
                    "colorR": 0,
                    "colorG": 255,
                    "colorB": 170,
                    "anchored": "true",
                    "material": "Ice",
                },
            },
            {
                "action": "addDialogueCharacter",
                "args": {
                    "tone": "Friendly",
                    "posX": 24,
                    "posY": 5,
                    "posZ": 0,
                    "initialdialogue": "ءﺎﺘەﺮىە سەﺰىپ نۇقۇسىدا ءۇچۇڭ, ئەرجىڭە ئەپەتى ھەنزۇدان ئۇچۇرۇپ ئەپەتى باسۇۋاتىدۇ.",
                    "dialogue1": "ۋە ئۇنىڭلارنىڭ نەۋە تەپىدىغان ئىگىلىكى ئەپەتى بۇلۇپ باسۇۋاتىدۇ.",
                    "dialogue1response": "ئۇ چېنە ھەققىدى. ئۇ بۇلۇپ ئىگىلىكىڭىزنىڭ ھەypressىنىڭ چەڭىنىڭنى ئەپەتى @%##*",
                    "dialogue2": "ۋە ئۇنىڭلارنىڭ نەۋە تەپىدىغان ئىگىلىكى ئەپەتى بۇلۇپ باسۇۋاتىدۇ.",
                    "dialogue2response": "ئۇ چېنە ھەققىدى. ئۇ بۇلۇپ ئىگىلىكىڭىزنىڭ ھەypressىنىڭ چەڭىنىڭنى ئەپەتى @%##*",
                },
            },
            {
                "action": "addAssetProps",
                "args": {"prop": "Cart_01", "posX": 48, "posY": 6, "posZ": 0},
            },
            {
                "action": "addBrainRot",
                "args": {"rot": "a1", "posX": 72, "posY": 22, "posZ": 0},
            },
            {
                "action": "addDialogueCharacter",
                "args": {
                    "tone": "Enemy",
                    "posX": 96,
                    "posY": 3,
                    "posZ": 0,
                    "initialdialogue": "There's no escape from this reality, not with those cursed abominations.",
                    "dialogue1": "Why do you even bother haunting these islands?",
                    "dialogue1response": "And why do you keep trespassing? Proceed at your own risk.",
                    "dialogue2": "Will you never learn to leave?",
                    "dialogue2response": "Your words carry weight, but my curse remains absolute.",
                },
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": 88,
                    "posY": 10,
                    "posZ": 0,
                    "sizeX": 32,
                    "sizeY": 15,
                    "sizeZ": 16,
                    "colorR": 255,
                    "colorG": 216,
                    "colorB": 170,
                    "anchored": "true",
                    "material": "ForceField",
                },
            },
            {
                "action": "addParticles",
                "args": {
                    "posX": 0,
                    "posY": 3,
                    "posZ": 0,
                    "texture": "rbxasset://textures/particles/smoke_main.dds",
                    "rate": 80,
                    "lifetime": 2,
                    "size": 4,
                },
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": 72,
                    "posY": 7,
                    "posZ": 0,
                    "sizeX": 16,
                    "sizeY": 20,
                    "sizeZ": 8,
                    "colorR": 30,
                    "colorG": 90,
                    "colorB": 160,
                    "anchored": "true",
                    "material": "Rock",
                },
            },
            {
                "action": "addAssetProps",
                "args": {"prop": "Flag_01", "posX": 80, "posY": 9, "posZ": 0},
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "LightOrb",
                    "posX": 40,
                    "posY": 10,
                    "posZ": 0,
                    "sizeX": 6,
                    "sizeY": 10,
                    "sizeZ": 6,
                    "colorR": 225,
                    "colorG": 160,
                    "colorB": 80,
                    "anchored": "true",
                    "material": "Glass",
                },
            },
            {
                "action": "addBrainRot",
                "args": {"rot": "b1", "posX": 56, "posY": 8, "posZ": 0},
            },
            {
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": 16,
                    "posY": 12,
                    "posZ": 5,
                    "sizeX": 28,
                    "sizeY": 10,
                    "sizeZ": 14,
                    "colorR": 73,
                    "colorG": 170,
                    "colorB": 180,
                    "anchored": "true",
                    "material": "Pneumatic",
                },
            },
            {
                "action": "spawnCluster",
                "args": {
                    "partType": "Crystal",
                    "centerposX": 92,
                    "centerposY": 8,
                    "centerposZ": 0,
                    "count": 3,
                    "radius": 6,
                },
            },
        ],
    },
    {
        "mood": "CosmicMemories",
        "seed_hint": "gossamer memory threads",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "OrangeSky" }
            },
            {
            "action": "BackgroundSong",
            "args": { "songType": "Dream" }
            },
            {
            "action": "floatPart",
            "args": { "partType": "LightOrb", "posX": 0, "posY": 20, "posZ": 0, "sizeX": 3, "sizeY": 5, "sizeZ": 3, "colorR": 255, "colorG": 192, "colorB": 203, "anchored": "true", "material": "Metal", "amplitude": 5, "speed": 1 }
            },
            {
            "action": "floatPart",
            "args": { "partType": "Crystal", "posX": 20, "posY": 20, "posZ": 0, "sizeX": 3, "sizeY": 5, "sizeZ": 3, "colorR": 255, "colorG": 165, "colorB": 0, "anchored": "true", "material": "Metal", "amplitude": 2, "speed": 0.5 }
            },
            {
            "action": "fillTerrainBlock",
            "args": { "posX": 0, "posY": 64, "posZ": 0, "sizeX": 128, "sizeY": 64, "sizeZ": 0, "material": "SmokyGrass" }
            },
            {
            "action": "spawnCluster",
            "args": { "partType": "Fence_01", "centerposX": 128, "centerposY": 2, "centerposZ": 128, "count": 12, "radius": 10 }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Tent_01", "posX": 30, "posY": 6, "posZ": 30 }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Crate_01", "posX": 50, "posY": 6, "posZ": 50 }
            },
            {
            "action": "addParticles",
            "args": { "posX": 10, "posY": 24, "posZ": 10, "texture": "rbxasset://textures/particles/smoke01.dds", "rate": 8, "lifetime": 4, "size": 2 }
            },
            {
            "action": "floatPart",
            "args": { "partType": "TextBlock", "posX": -8, "posY": 22, "posZ": -8, "sizeX": 10, "sizeY": 5, "sizeZ": 10, "colorR": 0, "colorG": 255, "colorB": 0, "anchored": "true", "material": "Plastic", "amplitude": 4, "speed": 0.2, "text": "Welcome, Lost One." }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly",
                "posX": 20, "posY": 3, "posZ": 20,
                "initialdialogue": "Have you come to remember the forgotten dreams?",
                "dialogue1": "What are you looking for?",
                "dialogue1response": "Maybe a reply from the one I lost.",
                "dialogue2": "Will you help me rebuild where I fell?",
                "dialogue2response": "Nothing lost is truly gone, just misplaced for a while. Let's search together."
            }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Enemy",
                "posX": 80, "posY": 3, "posZ": 80,
                "initialdialogue": "Not everyone seeks paradise in memories.",
                "dialogue1": "Why destroy what you can't recreate?",
                "dialogue1response": "I never destroyed—just unlaid who I was meant to be. Leave, or witness the next awakening.",
                "dialogue2": "Will you stay?",
                "dialogue2response": "The past won't stay, no matter how much we ask. Try to leave with grace."
            }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "a1", "posX": 64, "posY": 2, "posZ": 64 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 100, "posY": 50, "posZ": 100, "sizeX": 6, "sizeY": 4, "sizeZ": 6, "colorR": 128, "colorG": 192, "colorB": 255, "anchored": "true", "material": "ForceField" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 250, "posY": 50, "posZ": 250, "sizeX": 12, "sizeY": 6, "sizeZ": 12, "colorR": 255, "colorG": 255, "colorB": 255, "anchored": "true", "material": "WoodPlanks" }
            },
            {
            "action": "floatPart",
            "args": { "partType": "Crystal", "posX": 70, "posY": 24, "posZ": 70, "sizeX": 4, "sizeY": 5, "sizeZ": 4, "colorR": 0, "colorG": 0, "colorB": 255, "anchored": "true", "material": "Metal" }
            },
            {
            "action": "floatPart",
            "args": { "partType": "Crystal", "posX": -30, "posY": 24, "posZ": -30, "sizeX": 3, "sizeY": 5, "sizeZ": 3, "colorR": 255, "colorG": 165, "colorB": 0, "anchored": "true", "material": "Metal" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "LightOrb", "posX": 90, "posY": 20, "posZ": 90, "sizeX": 3, "sizeY": 5, "sizeZ": 3, "colorR": 255, "colorG": 0, "colorB": 255, "anchored": "true", "material": "Metal" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 255, "ambientG": 204, "ambientB": 0, "outdoorR": 255, "outdoorG": 102, "outdoorB": 255, "brightness": 2, "clockTime": 12, "fogStart": 500, "fogEnd": 2000, "fogR": 255, "fogG": 204, "fogB": 255 }
            }
        ]
    },
    {
        "mood": " nostalgic intrigue",
        "seed_hint": "Memory shimmers on cracked pavements",  
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "EveningSky" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 165, "ambientG": 75, "ambientB": 150, "outdoorR": 200, "outdoorG": 130, "outdoorB": 170, "brightness": 2, "clockTime": 19.3, "fogStart": 500, "fogEnd": 100000, "fogR": 70, "fogG": 45, "fogB": 90 }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "Dream" }
            },
            {
            "action": "fillTerrainBlock",
            "args": { "posX": 64, "posY": 0, "posZ": 64, "sizeX": 128, "sizeY": 128, "sizeZ": 128, "material": "smoothplastic" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 111, "posZ": 64, "sizeX": 32, "sizeY": 6, "sizeZ": 32, "colorR": 172, "colorG": 111, "colorB": 172, "anchored": "true", "material": "brick" }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Crash_Cart_01", "posX": 20, "posY": 62, "posZ": 0, "anchored": "true" }
            },
            {
            "action": "addParticle",
            "args": { "posX": 64, "posY": 85, "posZ": 64, "texture": "rbxasset://textures/particles/smoke01.dds", "rate": 60, "lifetime": 2.5, "size": 20 }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly", "posX": 18, "posY": 60, "posZ": 0, "initialdialogue": "Welcome to the Emigrant Terminal, have you forgotten why you are here?", "dialogue1": "No, I know exactly why...", "dialogue1response": "Then why will you not move forward?", "dialogue2": "I wish to stay.", "dialogue2response": "You are living in memories. What do you wish to remember?" }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "b1", "posX": 80, "posY": 60, "posZ": 0, "anchored": "true" }
            },
            {
            "action": "spawnCluster",
            "args": { "partType": "Normal", "centerposX": 12, "centerposY": 62, "centerposZ": 12, "count": 5, "radius": 4, "colorR": 137, "colorG": 99, "colorB": 176, "material": "Wood" }
            },
            {
            "action": "floatPart",
            "args": { "partType": "LightOrb", "posX": 100, "posY": 62, "posZ": 100, "sizeX": 2, "sizeY": 2, "sizeZ": 2, "colorR": 255, "colorG": 175, "colorB": 255, "anchored": "false", "material": "Glass", "amplitude": 0.8, "speed": 0.5 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 90, "posY": 60, "posZ": 90, "sizeX": 8, "sizeY": 2, "sizeZ": 8, "colorR": 150, "colorG": 60, "colorB": 115, "anchored":"true", "material": "Pavement" }
            },
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "EveningSky" }
            },
            {
            "action": "addParticle",
            "args": { "posX": 0, "posY": 0, "posZ": 0, "texture": "rbxasset://textures/particles/smoke_main.dds", "rate": 30, "lifetime": 3, "size": 4 }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Torch_01", "posX": 55, "posY": 62, "posZ": 61, "anchored": "true" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 0, "posY": 0, "posZ": 0, "sizeX": 2, "sizeY": 2, "sizeZ": 1, "colorR": 115, "colorG": 45, "colorB": 70, "anchored": "true", "material": "Brick" }
            }
        ]
    },
    {
        "mood": "fleeting serenity with creeping melancholy", 
        "seed_hint": "melody in fractured glass",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "Hills" }
            },
            {
            "action": "setLightingSimple",
            "args": {
                "ambientR": 200,
                "ambientG": 180,
                "ambientB": 230,
                "outdoorR": 150,
                "outdoorG": 200,
                "outdoorB": 190,
                "brightness": 2,
                "clockTime": 8,
                "fogStart": 7000,
                "fogEnd": 11000,
                "fogR": 150,
                "fogG": 180,
                "fogB": 190
            }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "SadMemory" }
            },
            {
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": 0, "posY": 0, "posZ": 0,
                "sizeX": 130, "sizeY": 30, "sizeZ": 130,        
                "colorR": 200, "colorG": 230, "colorB": 255,    
                "anchored": "true",
                "material": "Glass"
            }
            },
            {
            "action": "floatPart",
            "args": {
                "partType": "Normal",
                "posX": 0, "posY": 30, "posZ": 0,
                "sizeX": 128, "sizeY": 4, "sizeZ": 128,
                "colorR": 240, "colorG": 240, "colorB": 255,    
                "anchored": "true",
                "material": "ForceField",
                "amplitude": 2,
                "speed": 0.2
            }
            },
            {
            "action": "addParticles",
            "args": {
                "posX": 0,
                "posY": 28,
                "posZ": 50,
                "texture": "rbxasset://textures/particles/smoke02.dds",
                "rate": 20,
                "lifetime": 4,
                "size": 1
            }
            },
            {
            "action": "addParticles",
            "args": {
                "posX": 50,
                "posY": 28,
                "posZ": 0,
                "texture": "rbxasset://textures/particles/fire_main.dds",
                "rate": 10,
                "lifetime": 2,
                "size": 0.7
            }
            },
            {
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": 20, "posY": 11, "posZ": 20,
                "sizeX": 10, "sizeY": 20, "sizeZ": 10,
                "colorR": 204, "colorG": 125, "colorB": 51,     
                "anchored": "true",
                "material": "LavaCrate"
            }
            },
            {
            "action": "addAssetProps",
            "args": {
                "prop": "Grave_01",
                "posX": 42, "posY": 32, "posZ": 15,
                "anchored": "true"
            }
            },
            {
            "action": "addAssetProps",
            "args": {
                "prop": "Lantern_01",
                "posX": 55, "posY": 34, "posZ": 16,
                "anchored": "true"
            }
            },
            {
            "action": "addAssetProps",
            "args": {
                "prop": "Well_02",
                "posX": 70, "posY": 43, "posZ": 17,
                "anchored": "true"
            }
            },
            {
            "action": "addDialogueCharacter",
            "args": {
                "tone": "Friendly",
                "posX": 23, "posY": 25, "posZ": 0,
                "initialdialogue": "Welcome, traveler. Did you bring flowers?",
                "dialogue1": "Have you been here before?",      
                "dialogue1response": "Sometimes I dream here. Fragile glass mends only in the hush of the night.",      
                "dialogue2": "What if I don't belong here?",    
                "dialogue2response": "Then let your words become a melody for these rare clouds."
            }
            },
            {
            "action": "addBrainRot",
            "args": {
                "rot": "a0",
                "posX": 39, "posY": 23, "posZ": 17,
                "anchored": "true",
                "tone": "Enemy",
                "initialdialogue": "Intruder! This place is meant to remember forgotten fears.",
                "dialogue1": "Why haunt childhood places?",     
                "dialogue1response": "It is all I recognize, after the world fell silent.",
                "dialogue2": "I will run.",
                "dialogue2response": "You may. But shadows remember."
            }
            },
            {
            "action": "spawnPart",
            "args": {
                "partType": "Flower",
                "posX": 15, "posY": 8, "posZ": 40,
                "sizeX": 20, "sizeY": 4, "sizeZ": 20,
                "colorR": 255, "colorG": 200, "colorB": 210,    
                "anchored": "true",
                "material": "Fabric"
            }
            },
            {
            "action": "spawnCluster",
            "args": {
                "partType": "Normal",
                "centerposX": 65, "centerposY": 210, "centerposZ": 55,
                "count": 20,
                "radius": 15,
                "material": "Glass"
            }
            },
            {
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": 80, "posY": 220, "posZ": 60,
                "sizeX": 30, "sizeY": 20, "sizeZ": 20,
                "colorR": 180, "colorG": 160, "colorB": 240,    
                "anchored": "true",
                "material": "Pavement"
            }
            },
            {
            "action": "spawnCluster",
            "args": {
                "partType": "Normal",
                "centerposX": 35, "centerposY": 320, "centerposZ": 40,
                "count": 15,
                "radius": 7,
                "material": "Cobblestone"
            }
            },
            {
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": 58, "posY": 333, "posZ": 30,
                "sizeX": 36, "sizeY": 10, "sizeZ": 5,
                "colorR": 204, "colorG": 218, "colorB": 230,    
                "anchored": "true",
                "material": "Ice"
            }
            },
            {
            "action": "addAssetProps",
            "args": {
                "prop": "Flag_02",
                "posX": 62, "posY": 43, "posZ": 26,
                "anchored": "true"
            }
            },
            {
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": 16, "posY": 2, "posZ": -1,
                "sizeX": 12, "sizeY": 2, "sizeZ": 60,
                "colorR": 180, "colorG": 210, "colorB": 255,    
                "anchored": "true",
                "material": "Cobblestone"
            }
            }
        ]
    },
    {
        "mood": "whimsical serenity",
        "seed_hint": "clockwork meadows fluttering",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "EveningSky" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 100, "ambientG": 80, "ambientB": 120, "outdoorR": 160, "outdoorG": 180, "outdoorB": 200, "brightness": 1.8, "clockTime": 19.5, "fogStart": 80, "fogEnd": 1000, "fogR": 100, "fogG": 80, "fogB": 100 }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "Dream" }
            },
            {
            "action": " spawnCluster",
            "args": { " partType": "Snow", "centerPosX": 64, "centerPosY": 0, "centerPosZ": 64, "count": 100, "radius": 32 }
            },
            {
            "action": " spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 1, "posZ": 64, "sizeX": 128, "sizeY": 24, "sizeZ": 128, "colorR": 255, "colorG": 77, "colorB": 139, "anchored": "true", "material": "Grass" }   
            },
            {
            "action": " spawnPart",
            "args": { "partType": "Normal", "posX": 0, "posY": 1, "posZ": 0, "sizeX": 32, "sizeY": 24, "sizeZ": 32, "colorR": 139, "colorG": 68, "colorB": 123, "anchored": "true", "material": "Snow" }        
            },
            {
            "action": " spawnPart",
            "args": { "partType": "Normal", "posX": 128, "posY": 1, "posZ": 128, "sizeX": 32, "sizeY": 24, "sizeZ": 32, "colorR": 255, "colorG": 204, "colorB": 0, "anchored": "true", "material": "Sandstone" }
            },
            {
            "action": " addAssetProps",
            "args": { "prop": "Well_02", "posX": 64, "posY": 2, "posZ": 64 }
            },
            {
            "action": " addAssetProps",
            "args": { "prop": "Cart_01", "posX": -16, "posY": 2, "posZ": -16 }
            },
            {
            "action": " spawnPart",
            "args": { " partType": "Normal", "PosX": 256, "PosY": 2, "PosZ": 0, "SizeX": 40, "SizeY": 2, "SizeZ": 40, "ColorR": 204, "ColorG": 233, "ColorB": 102, "Anchored": "true", "Material": "WoodPlanks" }
            },
            {
            "action": " addDialogueCharacter",
            "args": { "tone": "Friendly", " posX": 0, " posY": 20, " posZ": 0, " initialDialogue": "Welcome to Shimmer Fields. Looking for something?", " dialogue1": "Can you tell me about this place?", " dialogue1response": "This place is alive with dreams and gentle magic. Each path tells a story.", " dialogue2": "Do you like music here?", " dialogue2response": "Music weaves through the winds—try listening to the sky song above." }
            },
            {
            "action": " addBrainRot",
            "args": { "rot": "a9", " posX": 25, " posY": 5, " posZ": -15 }
            },
            {
            "action": " floatPart",
            "args": { " partType": "LightOrb", " posX": 10, " posY": 11, " posZ": 10, " sizeX": 2, " sizeY": 2, " sizeZ": 2, " colorR": 255, " colorG": 245, " colorB": 160, " anchored": "true", " material": "Brick", " amplitude": 1.5, " speed": 0.3 }
            },
            {
            "action": " spawnPart",
            "args": { " partType": "Crystal", " posX": 22, " posY": 10, " posZ": 0, " sizeX": 4, " sizeY": 2, " sizeZ": 2, " colorR": 220, " colorG": 255, " colorB": 255, " anchored": "true", " material": "Glass" }
            },
            {
            "action": " addParticles",
            "args": { " posX": 50, " posY": 0, " posZ": 50, " texture": "rbxasset://textures/particles/fire_main.dds", " rate": 2, " lifetime": 3, " size": 0.8 }
            },
            {
            "action": " addAssetProps",
            "args": { " prop": "Lantern_01", " posX": -128, " posY": 3, " posZ": 64 }
            },
            {
            "action": " addDialogueCharacter",
            "args": { "tone": "Enemy", " posX": 2048, " posY": 8, " posZ": -2048, " initialDialogue": "You trespass on land sacred to dreams. Surrender or face the waiters.", " dialogue1": "Waiters?", " dialogue1response": "Silence is ritual. Our guests must rest.", " dialogue2": "Why should I surrender?", " dialogue2response": "Our shadows watch, violation earns silence forever." }
            },
            {
            "action": " fillTerrainBlock",
            "args": { " posX": 64, " posY": 2, " posZ": 64, " sizeX": 128, " sizeY": 10, " sizeZ": 128, " material": "WoodPlanks" }
            }
        ]
    },
    {
        "mood": "Serenely dreamlike and mysterious",
        "seed_hint": "shimmering clocktower over enchanted meadow",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "EveningSky" }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "Angel" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 204, "ambientG": 153, "ambientB": 204, "outdoorR": 255, "outdoorG": 193, "outdoorB": 255, "brightness": 1.1, "clockTime": 20, "fogStart": 50, "fogEnd": 2000, "fogR": 255, "fogG": 153, "fogB": 204 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 0, "posY": 0, "posZ": 0, "sizeX": 256, "sizeY": 64, "sizeZ": 256, "colorR": 255, "colorG": 255, "colorB": 255, "anchored": "true", "material": "Pavement" }   
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 0, "posY": 8, "posZ": 0, "sizeX": 128, "sizeY": 32, "sizeZ": 128, "colorR": 65, "colorG": 105, "colorB": 225, "anchored": "true", "material": "Grass" }       
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 0, "posZ": 0, "sizeX": 64, "sizeY": 32, "sizeZ": 64, "colorR": 255, "colorG": 0, "colorB": 0, "anchored": "true", "material": "DiamondPlate" }    
            },
            {
            "action": "spawnPart",
            "args": { "partType": "LightOrb", "posX": 50, "posY": 32, "posZ": 0, "sizeX": 6, "sizeY": 8, "sizeZ": 6, "colorR": 255, "colorG": 255, "colorB": 255, "anchored": "true", "material": "Glass" }       
            },
            {
            "action": "spawnCluster",
            "args": { "partType": "Crystal", "centerposX": 25, "centerposY": 24, "centerposZ": 24, "count": 25, "radius": 5 }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly", "posX": 30, "posY": 32, "posZ": 32, "initialdialogue": "Welcome, traveler. The clock has voices, and secrets are written in the ground.", "dialogue1": "What lies beneath the tower?", "dialogue1response": "Some call it the시간文书库, a memory archive, watched over by the silent clock.", "dialogue2": "Is anyone here after me?", "dialogue2response": "Not my voice. Most who enter go to hear the stories that living urns have kept for centuries." }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Torch_01", "posX": 20, "posY": 40, "posZ": 0 }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "b1", "posX": 16, "posY": 41, "posZ": 0 }
            },
            {
            "action": "floatPart",
            "args": { "partType": "LightOrb", "posX": 40, "posY": 36, "posZ": 0, "sizeX": 3, "sizeY": 5, "sizeZ": 3, "colorR": 255, "colorG": 255, "colorB": 255, "anchored": "true", "material": "Glass", "amplitude": 4, "speed": 0.5 }
            },
            {
            "action": "floatPart",
            "args": { "partType": "Crystal", "posX": 52, "posY": 34, "posZ": -2, "sizeX": 2, "sizeY": 2, "sizeZ": 2, "colorR": 225, "colorG": 204, "colorB": 255, "anchored": "true", "material": "Glass", "amplitude": 2, "speed": 1.1 }
            },
            {
            "action": "addParticles",
            "args": { "posX": 40, "posY": 36, "posZ": 0, "texture": "rbxasset://textures/particles/smoke02.dds", "rate": 20, "lifetime": 1.5, "size": 0.6 }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Cart_01", "posX": 70, "posY": 34, "posZ": 0 }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Tent_02", "posX": 80, "posY": 38, "posZ": 0 }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "a10", "posX": 90, "posY": 28, "posZ": 0 }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Enemy", "posX": 95, "posY": 30, "posZ": 0, "initialdialogue": "You seek knowledge? Only those who remember the sound of the bell may claim it.", "dialogue1": "What sound was it?", "dialogue1response": "A hollow appellation, like two fingers tapping stillness.", "dialogue2": "Will you challenge me?", "dialogue2response": "Every knee that bows remembers the bell. Its echo is not for the naive." }
            },
            {
            "action": "addParticles",
            "args": { "posX": 60, "posY": 42, "posZ": 0, "texture": "rbxasset://textures/particles/soft_smoke.dds", "rate": 100, "lifetime": 1.2, "size": 0.4 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 15, "posY": 50, "posZ": 30, "sizeX": 10, "sizeY": 10, "sizeZ": 20, "colorR": 153, "colorG": 204, "colorB": 102, "anchored": "true", "material": "WoodPlanks" }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Grave_01", "posX": 48, "posY": 50, "posZ": 30 }
            }
        ]
    },
    {
        "mood": "OTHERRUM",
        "seed_hint": "llc2c34y",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "EveningSky" }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "Soul" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 0, "ambientG": 150, "ambientB": 100, "outdoorR": 45, "outdoorG": 50, "outdoorB": 160, "brightness": 1.5, "clockTime": 16, "fogStart": 80, "fogEnd": 1000, "fogR": 0, "fogG": 0, "fogB": 0 }
            },
            {
            "action": "fillTerrainBlock",
            "args": { "posX": 0, "posY": 0, "posZ": 0, "sizeX": 128, "sizeY": 4, "sizeZ": 128, "material": "Grass" }
            },
            {
            "action": "addParticles",
            "args": { "posX": 0, "posY": 0, "posZ": 0, "texture": "rbxasset://textures/particles/smokemain.dds", "rate": 12, "lifetime": 6, "size": 0.8 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": -32, "posY": 16, "posZ": -32, "sizeX": 64, "sizeY": 6, "sizeZ": 64, "colorR": 50, "colorG": 190, "colorB": 50, "anchored": "true", "material": "Fabric" }     
            },
            {
            "action": "floatPart",
            "args": { "partType": "LightOrb", "posX": 96, "posY": 73, "posZ": 96, "sizeX": 8, "sizeY": 8, "sizeZ": 8, "colorR": 255, "colorG": 128, "colorB": 51, "anchored": "true", "material": "Neon", "amplitude": 4, "speed": 0.65 }
            },
            {
            "action": "spawnCluster",
            "args": { "partType": "Crystal", "centerposX": 92, "centerposY": 94, "centerposZ": 67, "count": 35, "radius": 12 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 30, "posY": 146, "posZ": 30, "sizeX": 4, "sizeY": 10, "sizeZ": 4, "colorR": 120, "colorG": 200, "colorB": 100, "anchored": "true", "material": "Glass" }      
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "b2", "posX": 0, "posY": 78, "posZ": 0 }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly", "posX": -100, "posY": 60, "posZ": 72, "initialdialogue": "Welcome to the fabric world, traveler.", "dialogue1": "Is there anyone else around?", "dialogue1response": "No, it's just us for now.", "dialogue2": "What is this place?", "dialogue2response": "It's called Oddities Grove—made from threads and echoes." }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Fence_01", "posX": 53, "posY": 51, "posZ": -27 }
            },
            {
            "action": "addParticles",
            "args": { "posX": 64, "posY": 88, "posZ": 64, "texture": "rbxasset://textures/particles/cloud_main.dds", "rate": 6, "lifetime": 18, "size": 1.2 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 30, "posY": 0.1, "posZ": -40, "sizeX": 80, "sizeY": 16, "sizeZ": 26, "colorR": 75, "colorG": 30, "colorB": 100, "anchored": "true", "material": "CrackedLava" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": -67, "posY": 16, "posZ": 67, "sizeX": 10, "sizeY": 4, "sizeZ": 10, "colorR": 45, "colorG": 200, "colorB": 230, "anchored": "true", "material": "Salt" }       
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Tent_01", "posX": 43, "posY": 151, "posZ": 43 }
            },
            {
            "action": "floatPart",
            "args": { "partType": "Crystal", "posX": 18, "posY": 42, "posZ": 85, "sizeX": 6, "sizeY": 6, "sizeZ": 6, "colorR": 169, "colorG": 210, "colorB": 255, "anchored": "true", "material": "ForceField", "amplitude": 2.5, "speed": 0.38 }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "c10", "posX": 18, "posY": 89, "posZ": 18 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 77, "posY": 1, "posZ": 77, "sizeX": 32, "sizeY": 2, "sizeZ": 32, "colorR": 135, "colorG": 210, "colorB": 245, "anchored": "true", "material": "Plastic" }     
            },
            {
            "action": "fillTerrainBlock",
            "args": { "posX": -36, "posY": 99, "posZ": -36, "sizeX": 72, "sizeY": 3, "sizeZ": 72, "material": "Snow" }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly", "posX": -90, "posY": 40, "posZ": 23, "initialdialogue": "This grove feels strange... almost alive with emotions.", "dialogue1": "How do you know this place is alive?", "dialogue1response": "The way everything moves quietly and in patterns, even I can feel it.", "dialogue2": "Why are you here at night?", "dialogue2response": "I search for hidden truths about this world and its forgotten spirits." }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Well_02", "posX": 91, "posY": 162, "posZ": 91 }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "b9", "posX": 0, "posY": 35, "posZ": 0 }
            }
        ]
    },
    {
        "mood": "melancholy思念之乡",
        "seed_hint": "记忆里的雾",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "Snow" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 150, "ambientG": 150, "ambientB": 200, "outdoorR": 100, "outdoorG": 80, "outdoorB": 120, "brightness": 0.75, "clockTime": 10, "fogStart": 5, "fogEnd": 40, "fogR": 220, "fogG": 220, "fogB": 240 }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "Reflection" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 0, "posY": 5, "posZ": 0, "sizeX": 128, "sizeY": 30, "sizeZ": 128, "colorR": 40, "colorG": 40, "colorB": 60, "anchored": "true", "material": "Glacier" }     
            },
            {
            "action": "floatPart",
            "args": { "partType": "Crystal", "posX": 32, "posY": 25, "posZ": 64, "sizeX": 8, "sizeY": 8, "sizeZ": 8, "colorR": 255, "colorG": 255, "colorB": 255, "anchored": "true", "material": "Glass", "amplitude": 8, "speed": 0.4 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 40, "posY": 15, "posZ": 32, "sizeX": 32, "sizeY": 8, "sizeZ": 64, "colorR": 200, "colorG": 0, "colorB": 0, "anchored": "true", "material": "Brick" }        
            },
            {
            "action": "floatPart",
            "args": { "partType": "Normal", "posX": -64, "posY": -2, "posZ": -80, "sizeX": 64, "sizeY": 64, "sizeZ": 64, "colorR": 215, "colorG": 225, "colorB": 200, "anchored": "true", "material": "Mud" }   
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Flag_01", "posX": 64, "posY": 3, "posZ": 1, "anchored": "true" }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Sign_01", "posX": 112, "posY": 3.5, "posZ": 5, "anchored": "true" }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly", "posX": 96, "posY": 25, "posZ": 0, "initialdialogue": "欢迎来到记忆迷宫的一角。你想寻找什么？", "dialogue1": "你能告诉我这条路通向哪里吗？", "dialogue1response": "这 条路会带你回到你最重要的人的梦境里，但你要小心路上的记忆锁。", "dialogue2": "我很害怕迷路！", "dialogue2response": "没关系，我能当你的向导。只要跟我来就可以了。" }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "b6", "posX": 25, "posY": 5, "posZ": 35, "anchored": "true" }
            }
        ]
    },
    {
        "mood": "dreamlike serenity",
        "seed_hint": "foggy midnight playground",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "eveningsky" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 10, "ambientG": 15, "ambientB": 20, "outdoorR": 10, "outdoorG": 15, "outdoorB": 20, "brightness": 0.3, "clockTime": 22, "fogStart": 20, "fogEnd": 250, "fogR": 5, "fogG": 5, "fogB": 5 }
            },
            {
            "action": "fillTerrainBlock",
            "args": { "posX": 64, "posY": 0, "posZ": 64, "sizeX": 128, "sizeY": 64, "sizeZ": 128, "material": "Grass" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 1, "posZ": 64, "sizeX": 2, "sizeY": 16, "sizeZ": 2, "colorR": 135, "colorG": 206, "colorB": 235, "anchored": "true", "material": "Pavement" }     
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 80, "posY": 1, "posZ": 80, "sizeX": 2, "sizeY": 16, "sizeZ": 2, "colorR": 255, "colorG": 140, "colorB": 0, "anchored": "true", "material": "Sandstone" }      
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 0, "posY": 1, "posZ": 0, "sizeX": 2, "sizeY": 16, "sizeZ": 2, "colorR": 128, "colorG": 0, "colorB": 128, "anchored": "true", "material": "Snow" }
            },
            {
            "action": "spawnCluster",
            "args": { "partType": "Crystal", "centerposX": 0, "centerposY": 1, "centerposZ": 0, "count": 10, "radius": 5 }
            },
            {
            "action": "addParticles",
            "args": { "posX": 0, "posY": 0, "posZ": 0, "texture": "rbxasset://textures/particles/soft_smoke.dds", "rate": 2, "lifetime": 5, "size": 1 }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "Dream" }
            },
            {
            "action": "addDialogueCharacter",
            "args": {
                "tone": "Friendly",
                "posX": 45, "posY": 21, "posZ": 45,
                "initialdialogue": "Greetings wanderer… Why do you seek the endless field?",
                "dialogue1": "What lies after the horizon, do you think?",
                "dialogue1response": "Everything begins still… until it isn't.",
                "dialogue2": "Will this place always feel as hushed as the night?",
                "dialogue2response": "The world always shifts, youth. Tonight settles, slowly."
            }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Torch_01", "posX": 80, "posY": 1, "posZ": 80 }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "a1", "posX": 95, "posY": 1, "posZ": 0 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 49, "posY": 22, "posZ": 71, "sizeX": 4, "sizeY": 12, "sizeZ": 4, "colorR": 210, "colorG": 250, "colorB": 180, "anchored": "true", "material": "Cloth" }       
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 83, "posY": 1, "posZ": 83, "sizeX": 2, "sizeY": 16, "sizeZ": 2, "colorR": 50, "colorG": 150, "colorB": 200, "anchored": "true", "material": "WoodPlanks" }    
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": -20, "posY": 1, "posZ": -20, "sizeX": 2, "sizeY": 16, "sizeZ": 2, "colorR": 91, "colorG": 155, "colorB": 203, "anchored": "true", "material": "Rock" }        
            }
        ]
    },
    {
        "mood": "古怪而温馨",
        "seed_hint": "迷梦蛋糕",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "RedSky" }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "Soul" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 150, "ambientG": 0, "ambientB": 50, "outdoorR": 150, "outdoorG": 20, "outdoorB": 60, "brightness": 1.5, "clockTime": 21, "fogStart": 50, "fogEnd": 10000, "fogR": 255, "fogG": 255, "fogB": 255 }
            },
            {
            "action": "fillTerrainBlock",
            "args": { "posX": 0, "posY": 0, "posZ": 0, "sizeX": 128, "sizeY": 40, "sizeZ": 128, "material": "Sandstone" }   
            },
            {
            "action": "addParticles",
            "args": { "posX": 0, "posY": 15, "posZ": 0, "texture": "rbxasset://textures/particles/smoke01.dds", "rate": 150, "lifetime": 5, "size": 2 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 0, "posY": 25, "posZ": 0, "sizeX": 10, "sizeY": 10, "sizeZ": 10, "colorR": 220, "colorG": 220, "colorB": 200, "anchored": "true", "material": "Pavement" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 25, "posY": 0, "posZ": 25, "sizeX": 5, "sizeY": 15, "sizeZ": 5, "colorR": 0, "colorG": 150, "colorB": 0, "anchored": "true", "material": "Grass" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 75, "posY": 0, "posZ": 75, "sizeX": 5, "sizeY": 15, "sizeZ": 5, "colorR": 255, "colorG": 150, "colorB": 0, "anchored": "true", "material": "Pavement" }
            },
            {
            "action": "_spawnCluster",
            "args": { "partType": "Crystal", "centerposX": 0, "centerposY": 10, "centerposZ": 0, "count": 100, "radius": 8 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 50, "posY": 20, "posZ": 50, "sizeX": 30, "sizeY": 5, "sizeZ": 30, "colorR": 250, "colorG": 210, "colorB": 130, "anchored": "true", "material": "Fabric" }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Well_01", "posX": 80, "posY": 10, "posZ": 80 }
            },
            {
            "action": "addDialogueCharacter",
            "args": {
                "tone": "Friendly",
                "posX": 50, "posY": 30, "posZ": 50,
                "initialdialogue": "你好啊，这里是迷梦蛋糕！有什么可以帮你吗？",
                "dialogue1": "这地方看起来很奇怪啊...",
                "dialogue1response": "是呀，有时候梦里的地方确实不一样哦。",
                "dialogue2": "你知道怎么出去吗？",
                "dialogue2response": "暂时还不知道哦，也许你 discoveries 会给我们一个线索吧！"
            }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "a4", "posX": 30, "posY": 30, "posZ": 30 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 90, "posY": 10, "posZ": 90, "sizeX": 10, "sizeY": 20, "sizeZ": 10, "colorR": 150, "colorG": 230, "colorB": 180, "anchored": "true", "material": "Brick" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 60, "posY": 19, "posZ": 60, "sizeX": 50, "sizeY": 5, "sizeZ": 50, "colorR": 255, "colorG": 210, "colorB": 0, "anchored": "true", "material": "WoodPlanks" }
            }
        ]
    },
    {
        "mood": "melancholy longing",
        "seed_hint": "echoes of forgotten chains",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "EveningSky" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 150, "ambientG": 80, "ambientB": 100, "outdoorR": 110, "outdoorG": 110, "outdoorB": 60, "brightness": 1.5, "clockTime": 18, "fogStart": 30, "fogEnd": 200, "fogR": 70, "fogG": 30, "fogB": 20 }
            },
            {
            "action": "fillTerrainBlock",
            "args": { "posX": 64, "posY": 0, "posZ": 64, "sizeX": 128, "sizeY": 64, "sizeZ": 128, "material": "Coal" }      
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 128, "posZ": 64, "sizeX": 128, "sizeY": 3, "sizeZ": 128, "colorR": 140, "colorG": 150, "colorB": 130, "anchored": "true", "material": "Grass" }
            },
            {
            "action": "spawnCluster",
            "args": { "partType": "LightOrb", "centerposX": 64, "centerposY": 128, "centerposZ": 64, "count": 15, "radius": 8 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": -1, "posZ": 64, "sizeX": 128, "sizeY": 3, "sizeZ": 128, "colorR": 210, "colorG": 90, "colorB": 50, "anchored": "true", "material": "Coal" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 30, "posY": -1, "posZ": 30, "sizeX": 12, "sizeY": 24, "sizeZ": 12, "colorR": 60, "colorG": 0, "colorB": 0, "anchored": "true", "material": "Iron" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 69, "posY": -1, "posZ": 30, "sizeX": 12, "sizeY": 24, "sizeZ": 12, "colorR": 255, "colorG": 200, "colorB": 0, "anchored": "true", "material": "Iron" }
            },
            {
            "action": "addParticles",
            "args": { "posX": 64, "posY": 128, "posZ": 64, "texture": "rbxasset://textures/particles/smoke02.dds", "rate": 15, "lifetime": 4, "size": 3 }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "Reflection" }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly", "posX": 64, "posY": 128, "posZ": 64, "initialdialogue": "Hello traveler. The chains here run deep.", "dialogue1": "Can you help me break these?", "dialogue1response": "Of course, if you can find the key at the end of the maze.", "dialogue2": "Why are you trapped here?", "dialogue2response": "I was wrong and others punished me. Now I yearn for freedom." }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "a1", "posX": 50, "posY": 128, "posZ": 50 }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Well_01", "posX": 80, "posY": 138, "posZ": 80 }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 130, "posZ": 80, "sizeX": 15, "sizeY": 7, "sizeZ": 15, "colorR": 169, "colorG": 210, "colorB": 255, "anchored": "true", "material": "Metal" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 130, "posZ": 95, "sizeX": 20, "sizeY": 3, "sizeZ": 20, "colorR": 153, "colorG": 50, "colorB": 50, "anchored": "true", "material": "Iron" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 130, "posZ": 75, "sizeX": 25, "sizeY": 2, "sizeZ": 25, "colorR": 230, "colorG": 40, "colorB": 15, "anchored": "true", "material": "Brick" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 64, "posY": 130, "posZ": 60, "sizeX": 18, "sizeY": 3, "sizeZ": 18, "colorR": 80, "colorG": 0, "colorB": 100, "anchored": "true", "material": "Metal" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 750, "posY": 128, "posZ": 64, "sizeX": 128, "sizeY": 3, "sizeZ": 128, "colorR": 200, "colorG": 60, "colorB": 10, "anchored": "true", "material": "Grass" }
            }
        ]
    },
    {
        "mood": "Eerie and mysterious, with a sense of longing",
        "seed_hint": "whispers on a forgotten island",
        "steps": [
            {
            "action": "setSkybox",
            "args": { "skyBoxType": "DarkForest" }
            },
            {
            "action": "setLightingSimple",
            "args": { "ambientR": 15, "ambientG": 5, "ambientB": 5, "outdoorR": 60, "outdoorG": 10, "outdoorB": 10, "brightness": 1.5, "clockTime": 20.0, "fogStart": 15, "fogEnd": 100, "fogR": 15, "fogG": 0, "fogB": 0 }
            },
            {
            "action": "setBackgroundSong",
            "args": { "songType": "SadMemory" }
            },
            {
            "action": "fillTerrainBlock",
            "args": { "posX": 0, "posY": 0, "posZ": 0, "sizeX": 128, "sizeY": 15, "sizeZ": 128, "material": "Pebble" }      
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 56, "posY": 14, "posZ": 64, "sizeX": 16, "sizeY": 4, "sizeZ": 16, "colorR": 105, "colorG": 10, "colorB": 0, "anchored": "true", "material": "Sand" }
            },
            {
            "action": "spawnCluster",
            "args": { "partType": "Normal", "centerposX": 56, "centerposY": 14, "centerposZ": 64, "count": 40, "radius": 8, "material": "Rock" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 16, "posY": 14, "posZ": 64, "sizeX": 32, "sizeY": 2, "sizeZ": 16, "colorR": 87, "colorG": 60, "colorB": 20, "anchored": "true", "material": "Mud" }
            },
            {
            "action": "spawnPart",
            "args": { "partType": "Normal", "posX": 84, "posY": 14, "posZ": 64, "sizeX": 32, "sizeY": 2, "sizeZ": 16, "colorR": 50, "colorG": 80, "colorB": 0, "anchored": "true", "material": "LimeStone" }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Tent_01", "posX": 48, "posY": 14, "posZ": 64, "anchored": "true" }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly", "posX": 48, "posY": 14, "posZ": 64, "initialdialogue": "You find yourself on a forgotten island... Welcome.", "dialogue1": "Hello, stranger.", "dialogue1response": "Thank you. I've been lost for a while.", "dialogue2": "Do you see the old maps on the table?", "dialogue2response": "Yes, and they seem to tell stories long forgotten." }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Cart_01", "posX": 16, "posY": 16, "posZ": 64, "anchored": "true" }
            },
            {
            "action": "addAssetProps",
            "args": { "prop": "Well_01", "posX": 84, "posY": 16, "posZ": 64, "anchored": "true" }
            },
            {
            "action": "addparticles",
            "args": { "posX": 0, "posY": 15, "posZ": 0, "texture": "rbxasset://textures/particles/smoke_main.dds", "rate": 12, "lifetime": 4, "size": 1 }
            },
            {
            "action": "addparticles",
            "args": { "posX": 128, "posY": 15, "posZ": 0, "texture": "rbxasset://textures/particles/smoke02.dds", "rate": 10, "lifetime": 6, "size": 1 }
            },
            {
            "action": "addBrainRot",
            "args": { "rot": "a1", "posX": 48, "posY": 16, "posZ": 64 }
            },
            {
            "action": "addDialogueCharacter",
            "args": { "tone": "Friendly", "posX": 48, "posY": 18, "posZ": 64, "initialdialogue": "Lost? You are not the first.", "dialogue1": "What happened to this place?", "dialogue1response": "Time forgotten, treasures hidden.", "dialogue2": "Have you heard of the forgotten ones?", "dialogue2response": "Once they roamed these lands, now but shadows." }   
            },
            {
            "action": "addparticles",
            "args": { "posX": 48, "posY": 15, "posZ": 128, "texture": "rbxasset://textures/particles/smoke_main.dds", "rate": 20, "lifetime": 8, "size": 2 }
            }
        ]
    },
    
]

def generate_terrain():
    random_area = get_random_element(data)
    return random_area