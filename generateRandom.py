import random
import json
import math

def generate_random_scene():
    """ULTIMATE WORLD GENERATOR - Following all rules strictly"""
    print("GENERATING ULTIMATE WORLD WITH MAXIMUM DETAIL")
    
    center_x, center_y, center_z = 2.25, 8.625, 1
    steps = []
    
    # === ULTIMATE THEME COLLECTION - 21 Unique Worlds ===
    themes = [
        {
            "name": "Ethereal Crystal Cathedral",
            "sky": "EveningSky",
            "song": "Reflection",
            "terrain_material": "Ice",
            "accent_material": "Glass",
            "structure_material": "Neon",
            "terrain_layers": 4,
            "main_part": "Crystal",
            "structure_type": "cathedral",
            "lighting": {
                "ambient": (0.3, 0.5, 0.8), 
                "outdoor": (0.4, 0.6, 0.9), 
                "brightness": 1.8, 
                "time": 19.5, 
                "fog": (0.2, 0.3, 0.6)
            },
            "colors": [(150, 200, 255), (100, 180, 255), (180, 220, 255)],
        },
        {
            "name": "Molten Obsidian Fortress",
            "sky": "RedSky",
            "song": "Groovy",
            "terrain_material": "CrackedLava",
            "accent_material": "Basalt",
            "structure_material": "CorrodedMetal",
            "terrain_layers": 3,
            "main_part": "LightOrb",
            "structure_type": "fortress",
            "lighting": {
                "ambient": (0.9, 0.3, 0.1), 
                "outdoor": (1, 0.4, 0.15), 
                "brightness": 2.2, 
                "time": 20, 
                "fog": (0.9, 0.3, 0.1)
            },
            "colors": [(255, 100, 50), (200, 80, 40), (255, 150, 80)],
        },
        {
            "name": "Arctic Monastery",
            "sky": "Snow",
            "song": "SadMemory",
            "terrain_material": "Glacier",
            "accent_material": "Snow",
            "structure_material": "Marble",
            "terrain_layers": 5,
            "main_part": "Normal",
            "structure_type": "monastery",
            "lighting": {
                "ambient": (0.85, 0.9, 0.95), 
                "outdoor": (0.9, 0.95, 1), 
                "brightness": 2, 
                "time": 11, 
                "fog": (0.95, 0.97, 1)
            },
            "colors": [(240, 245, 255), (220, 230, 245), (200, 215, 235)],
        },
        {
            "name": "Golden Desert Oasis",
            "sky": "Desert",
            "song": "Space",
            "terrain_material": "Sand",
            "accent_material": "Sandstone",
            "structure_material": "Wood",
            "terrain_layers": 3,
            "main_part": "LightOrb",
            "structure_type": "oasis",
            "lighting": {
                "ambient": (1, 0.9, 0.6), 
                "outdoor": (1, 0.95, 0.7), 
                "brightness": 2.8, 
                "time": 13, 
                "fog": (1, 0.95, 0.8)
            },
            "colors": [(255, 220, 150), (240, 200, 130), (255, 235, 180)],
        },
        {
            "name": "Cyber Neon Gardens",
            "sky": "OrangeSky",
            "song": "Focus",
            "terrain_material": "Neon",
            "accent_material": "Glass",
            "structure_material": "DiamondPlate",
            "terrain_layers": 2,
            "main_part": "Crystal",
            "structure_type": "garden",
            "lighting": {
                "ambient": (0.5, 0.2, 0.7), 
                "outdoor": (0.7, 0.3, 0.9), 
                "brightness": 1.4, 
                "time": 1, 
                "fog": (0.4, 0.2, 0.6)
            },
            "colors": [(180, 100, 255), (200, 50, 255), (150, 80, 220)],
        },
        {
            "name": "Ancient Marble Sanctuary",
            "sky": "CloudSky",
            "song": "Classy",
            "terrain_material": "Marble",
            "accent_material": "Granite",
            "structure_material": "Limestone",
            "terrain_layers": 4,
            "main_part": "Normal",
            "structure_type": "sanctuary",
            "lighting": {
                "ambient": (0.9, 0.85, 0.75), 
                "outdoor": (0.95, 0.9, 0.8), 
                "brightness": 1.9, 
                "time": 9, 
                "fog": (0.98, 0.96, 0.92)
            },
            "colors": [(250, 240, 220), (240, 230, 210), (230, 220, 200)],
        },
        {
            "name": "Steampunk Sky Platform",
            "sky": "Hills",
            "song": "Dream",
            "terrain_material": "DiamondPlate",
            "accent_material": "Metal",
            "structure_material": "CorrodedMetal",
            "terrain_layers": 3,
            "main_part": "LightOrb",
            "structure_type": "platform",
            "lighting": {
                "ambient": (0.6, 0.55, 0.5), 
                "outdoor": (0.7, 0.65, 0.6), 
                "brightness": 1.5, 
                "time": 15, 
                "fog": (0.7, 0.65, 0.6)
            },
            "colors": [(180, 160, 140), (160, 140, 120), (200, 180, 160)],
        },
        {
            "name": "Bioluminescent Reef",
            "sky": "DarkForest",
            "song": "Reflection",
            "terrain_material": "Slate",
            "accent_material": "Rock",
            "structure_material": "ForceField",
            "terrain_layers": 4,
            "main_part": "Crystal",
            "structure_type": "reef",
            "lighting": {
                "ambient": (0.1, 0.4, 0.5), 
                "outdoor": (0.2, 0.5, 0.6), 
                "brightness": 1.2, 
                "time": 23, 
                "fog": (0.1, 0.3, 0.4)
            },
            "colors": [(80, 200, 220), (60, 180, 200), (100, 220, 240)],
        },
        {
            "name": "Enchanted Forest Grove",
            "sky": "Hills",
            "song": "Dream",
            "terrain_material": "LeafyGrass",
            "accent_material": "Wood",
            "structure_material": "WoodPlanks",
            "terrain_layers": 3,
            "main_part": "LightOrb",
            "structure_type": "grove",
            "lighting": {
                "ambient": (0.4, 0.7, 0.3), 
                "outdoor": (0.5, 0.8, 0.4), 
                "brightness": 1.6, 
                "time": 10, 
                "fog": (0.6, 0.8, 0.5)
            },
            "colors": [(120, 200, 100), (100, 180, 80), (140, 220, 120)],
        },
        {
            "name": "Twilight Zen Garden",
            "sky": "EveningSky",
            "song": "SadMemory",
            "terrain_material": "Pebble",
            "accent_material": "Slate",
            "structure_material": "Wood",
            "terrain_layers": 2,
            "main_part": "Normal",
            "structure_type": "zen",
            "lighting": {
                "ambient": (0.6, 0.5, 0.7), 
                "outdoor": (0.7, 0.6, 0.8), 
                "brightness": 1.3, 
                "time": 18.5, 
                "fog": (0.5, 0.4, 0.6)
            },
            "colors": [(180, 160, 200), (160, 140, 180), (200, 180, 220)],
        },
        {
            "name": "Celestial Observatory",
            "sky": "CloudSky",
            "song": "Space",
            "terrain_material": "Marble",
            "accent_material": "Glass",
            "structure_material": "Neon",
            "terrain_layers": 3,
            "main_part": "Crystal",
            "structure_type": "observatory",
            "lighting": {
                "ambient": (0.1, 0.1, 0.3), 
                "outdoor": (0.15, 0.15, 0.4), 
                "brightness": 1.0, 
                "time": 0, 
                "fog": (0.05, 0.05, 0.2)
            },
            "colors": [(100, 100, 200), (80, 80, 180), (120, 120, 220)],
        },
        {
            "name": "Jade Bamboo Palace",
            "sky": "Hills",
            "song": "Classy",
            "terrain_material": "LeafyGrass",
            "accent_material": "Wood",
            "structure_material": "Marble",
            "terrain_layers": 4,
            "main_part": "Normal",
            "structure_type": "palace",
            "lighting": {
                "ambient": (0.5, 0.8, 0.5), 
                "outdoor": (0.6, 0.85, 0.6), 
                "brightness": 1.7, 
                "time": 12, 
                "fog": (0.7, 0.9, 0.7)
            },
            "colors": [(100, 200, 100), (80, 180, 80), (120, 220, 120)],
        },
        {
            "name": "Rainbow Prism Nexus",
            "sky": "CloudSky",
            "song": "Focus",
            "terrain_material": "Glass",
            "accent_material": "Neon",
            "structure_material": "ForceField",
            "terrain_layers": 2,
            "main_part": "Crystal",
            "structure_type": "nexus",
            "lighting": {
                "ambient": (0.7, 0.7, 0.7), 
                "outdoor": (0.9, 0.9, 0.9), 
                "brightness": 2.5, 
                "time": 13, 
                "fog": (0.95, 0.95, 0.95)
            },
            "colors": [(255, 100, 150), (100, 255, 150), (150, 100, 255)],
        },
        {
            "name": "Volcanic Temple of Fire",
            "sky": "RedSky",
            "song": "Groovy",
            "terrain_material": "CrackedLava",
            "accent_material": "Basalt",
            "structure_material": "Rock",
            "terrain_layers": 4,
            "main_part": "LightOrb",
            "structure_type": "temple",
            "lighting": {
                "ambient": (1, 0.4, 0.1), 
                "outdoor": (1, 0.5, 0.2), 
                "brightness": 2.0, 
                "time": 19, 
                "fog": (0.8, 0.3, 0.1)
            },
            "colors": [(255, 120, 50), (255, 80, 30), (255, 150, 70)],
        },
        {
            "name": "Frozen Aurora Spire",
            "sky": "Snow",
            "song": "Reflection",
            "terrain_material": "Glacier",
            "accent_material": "Ice",
            "structure_material": "ForceField",
            "terrain_layers": 5,
            "main_part": "Crystal",
            "structure_type": "spire",
            "lighting": {
                "ambient": (0.4, 0.7, 0.9), 
                "outdoor": (0.5, 0.8, 1), 
                "brightness": 1.9, 
                "time": 3, 
                "fog": (0.6, 0.8, 0.95)
            },
            "colors": [(150, 220, 255), (100, 200, 255), (180, 230, 255)],
        },
        {
            "name": "Sakura Dream Pavilion",
            "sky": "EveningSky",
            "song": "SadMemory",
            "terrain_material": "LeafyGrass",
            "accent_material": "Wood",
            "structure_material": "WoodPlanks",
            "terrain_layers": 3,
            "main_part": "Normal",
            "structure_type": "pavilion",
            "lighting": {
                "ambient": (1, 0.85, 0.9), 
                "outdoor": (1, 0.9, 0.95), 
                "brightness": 1.6, 
                "time": 18, 
                "fog": (1, 0.95, 0.98)
            },
            "colors": [(255, 180, 200), (255, 200, 220), (255, 160, 190)],
        },
        {
            "name": "Mechanical Clock Tower",
            "sky": "CloudSky",
            "song": "Dream",
            "terrain_material": "DiamondPlate",
            "accent_material": "CorrodedMetal",
            "structure_material": "Metal",
            "terrain_layers": 3,
            "main_part": "LightOrb",
            "structure_type": "clocktower",
            "lighting": {
                "ambient": (0.7, 0.6, 0.5), 
                "outdoor": (0.8, 0.7, 0.6), 
                "brightness": 1.7, 
                "time": 14, 
                "fog": (0.85, 0.8, 0.75)
            },
            "colors": [(150, 120, 90), (170, 140, 110), (130, 100, 70)],
        },
        {
            "name": "Aquamarine Lagoon Shrine",
            "sky": "CloudSky",
            "song": "Reflection",
            "terrain_material": "Sand",
            "accent_material": "Pebble",
            "structure_material": "Glass",
            "terrain_layers": 2,
            "main_part": "Crystal",
            "structure_type": "shrine",
            "lighting": {
                "ambient": (0.4, 0.8, 0.9), 
                "outdoor": (0.5, 0.85, 0.95), 
                "brightness": 2.1, 
                "time": 11, 
                "fog": (0.6, 0.9, 1)
            },
            "colors": [(100, 220, 240), (80, 200, 230), (120, 240, 255)],
        },
        {
            "name": "Mystic Moon Gardens",
            "sky": "CloudSky",
            "song": "SadMemory",
            "terrain_material": "Slate",
            "accent_material": "Marble",
            "structure_material": "Neon",
            "terrain_layers": 3,
            "main_part": "LightOrb",
            "structure_type": "moongarden",
            "lighting": {
                "ambient": (0.3, 0.3, 0.5), 
                "outdoor": (0.4, 0.4, 0.6), 
                "brightness": 1.1, 
                "time": 1, 
                "fog": (0.2, 0.2, 0.4)
            },
            "colors": [(200, 200, 255), (180, 180, 240), (220, 220, 255)],
        },
        {
            "name": "Emerald Rainforest Canopy",
            "sky": "Hills",
            "song": "Dream",
            "terrain_material": "LeafyGrass",
            "accent_material": "Wood",
            "structure_material": "Fabric",
            "terrain_layers": 4,
            "main_part": "Normal",
            "structure_type": "canopy",
            "lighting": {
                "ambient": (0.3, 0.6, 0.3), 
                "outdoor": (0.4, 0.7, 0.4), 
                "brightness": 1.4, 
                "time": 10, 
                "fog": (0.5, 0.75, 0.5)
            },
            "colors": [(80, 180, 80), (60, 160, 60), (100, 200, 100)],
        },
        {
            "name": "Amethyst Geode Sanctuary",
            "sky": "DarkForest",
            "song": "Reflection",
            "terrain_material": "Rock",
            "accent_material": "Slate",
            "structure_material": "ForceField",
            "terrain_layers": 5,
            "main_part": "Crystal",
            "structure_type": "geode",
            "lighting": {
                "ambient": (0.5, 0.2, 0.6), 
                "outdoor": (0.6, 0.3, 0.7), 
                "brightness": 1.3, 
                "time": 23, 
                "fog": (0.4, 0.2, 0.5)
            },
            "colors": [(180, 80, 220), (200, 100, 240), (160, 60, 200)],
        },
    ]
    
    theme = random.choice(themes)
    
    # === SKY AND AUDIO (REQUIRED) ===
    steps.append({
        "action": "setSkybox",
        "args": {"skyBoxType": theme["sky"]}
    })
    
    steps.append({
        "action": "setBackgroundSong",
        "args": {"songType": theme["song"]}
    })
    
    # === THEMED LIGHTING (REQUIRED) ===
    lit = theme["lighting"]
    steps.append({
        "action": "setLightingSimple",
        "args": {
            "ambientR": lit["ambient"][0],
            "ambientG": lit["ambient"][1],
            "ambientB": lit["ambient"][2],
            "outdoorR": lit["outdoor"][0],
            "outdoorG": lit["outdoor"][1],
            "outdoorB": lit["outdoor"][2],
            "brightness": lit["brightness"],
            "clockTime": lit["time"],
            "fogStart": random.randint(80, 200),
            "fogEnd": random.randint(400, 1200),
            "fogR": lit["fog"][0],
            "fogG": lit["fog"][1],
            "fogB": lit["fog"][2]
        }
    })
    
    # === LARGE CENTRAL TERRAIN (REQUIRED: at least 128x128) ===
    steps.append({
        "action": "fillTerrainBlock",
        "args": {
            "posX": center_x,
            "posY": center_y - 10,
            "posZ": center_z,
            "sizeX": 128,
            "sizeY": 20,
            "sizeZ": 128,
            "material": theme["terrain_material"]
        }
    })
    
    # === ADDITIONAL TERRAIN LAYERS ===
    for i in range(1, theme["terrain_layers"]):
        layer_offset_y = i * random.randint(-12, -5)
        layer_size_x = random.randint(90, 120) - (i * 12)
        layer_size_z = random.randint(90, 120) - (i * 12)
        
        offset_x = random.randint(-8, 8)
        offset_z = random.randint(-8, 8)
        
        material = theme["accent_material"] if i % 2 == 1 else theme["terrain_material"]
        
        steps.append({
            "action": "fillTerrainBlock",
            "args": {
                "posX": center_x + offset_x,
                "posY": center_y + layer_offset_y,
                "posZ": center_z + offset_z,
                "sizeX": layer_size_x,
                "sizeY": random.randint(15, 35),
                "sizeZ": layer_size_z,
                "material": material
            }
        })
    
    # === UNIQUE STRUCTURE GENERATION FOR EACH THEME ===
    structure_type = theme["structure_type"]
    colors = theme["colors"]
    
    if structure_type == "cathedral":
        # Main hall
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 15,
                "posZ": center_z,
                "sizeX": 30,
                "sizeY": 25,
                "sizeZ": 50,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Corner spires
        for dx, dz in [(-12, -20), (12, -20), (-12, 20), (12, 20)]:
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Crystal",
                    "posX": center_x + dx,
                    "posY": center_y + 35,
                    "posZ": center_z + dz,
                    "sizeX": 5,
                    "sizeY": 40,
                    "sizeZ": 5,
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": "Neon"
                }
            })
        
        # Central spire
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Crystal",
                "posX": center_x,
                "posY": center_y + 45,
                "posZ": center_z,
                "sizeX": 8,
                "sizeY": 50,
                "sizeZ": 8,
                "colorR": colors[2][0],
                "colorG": colors[2][1],
                "colorB": colors[2][2],
                "anchored": True,
                "material": "Glass"
            }
        })
    
    elif structure_type == "fortress":
        # Central keep
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 20,
                "posZ": center_z,
                "sizeX": 25,
                "sizeY": 35,
                "sizeZ": 25,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Corner towers
        for dx, dz in [(-20, -20), (20, -20), (-20, 20), (20, 20)]:
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x + dx,
                    "posY": center_y + 25,
                    "posZ": center_z + dz,
                    "sizeX": 10,
                    "sizeY": 45,
                    "sizeZ": 10,
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": theme["accent_material"]
                }
            })
        
        # Walls
        for dx, dz, sx, sz in [(-20, 0, 5, 40), (20, 0, 5, 40), (0, -20, 40, 5), (0, 20, 40, 5)]:
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x + dx,
                    "posY": center_y + 12,
                    "posZ": center_z + dz,
                    "sizeX": sx,
                    "sizeY": 18,
                    "sizeZ": sz,
                    "colorR": colors[2][0],
                    "colorG": colors[2][1],
                    "colorB": colors[2][2],
                    "anchored": True,
                    "material": theme["structure_material"]
                }
            })
    
    elif structure_type == "monastery":
        # Main temple
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 12,
                "posZ": center_z,
                "sizeX": 35,
                "sizeY": 20,
                "sizeZ": 35,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Prayer bells in circle
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 25
            z = center_z + math.sin(rad) * 25
            
            steps.append({
                "action": "floatPart",
                "args": {
                    "partType": "LightOrb",
                    "posX": x,
                    "posY": center_y + 18,
                    "posZ": z,
                    "sizeX": 3,
                    "sizeY": 3,
                    "sizeZ": 3,
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": "Neon",
                    "amplitude": 2,
                    "speed": 0.5
                }
            })
    
    elif structure_type == "oasis":
        # Water pool
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 2,
                "posZ": center_z,
                "sizeX": 40,
                "sizeY": 3,
                "sizeZ": 40,
                "colorR": 100,
                "colorG": 180,
                "colorB": 255,
                "anchored": True,
                "material": "Glass"
            }
        })
        
        # Palm trees
        for angle in range(0, 360, 60):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 22
            z = center_z + math.sin(rad) * 22
            
            # Trunk
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 12,
                    "posZ": z,
                    "sizeX": 3,
                    "sizeY": 20,
                    "sizeZ": 3,
                    "colorR": 139,
                    "colorG": 90,
                    "colorB": 43,
                    "anchored": True,
                    "material": "Wood"
                }
            })
            
            # Leaves
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 24,
                    "posZ": z,
                    "sizeX": 12,
                    "sizeY": 1,
                    "sizeZ": 12,
                    "colorR": 50,
                    "colorG": 150,
                    "colorB": 50,
                    "anchored": True,
                    "material": "Fabric"
                }
            })
    
    elif structure_type == "garden":
        # Tiered platforms
        for level in range(3):
            size = 35 - (level * 8)
            y_offset = level * 12
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x,
                    "posY": center_y + 8 + y_offset,
                    "posZ": center_z,
                    "sizeX": size,
                    "sizeY": 2,
                    "sizeZ": size,
                    "colorR": colors[level % 3][0],
                    "colorG": colors[level % 3][1],
                    "colorB": colors[level % 3][2],
                    "anchored": True,
                    "material": theme["structure_material"]
                }
            })
    
    elif structure_type == "sanctuary":
        # Base
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 5,
                "posZ": center_z,
                "sizeX": 50,
                "sizeY": 8,
                "sizeZ": 50,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Columns
        for dx in [-15, -5, 5, 15]:
            for dz in [-15, -5, 5, 15]:
                steps.append({
                    "action": "spawnPart",
                    "args": {
                        "partType": "Normal",
                        "posX": center_x + dx,
                        "posY": center_y + 20,
                        "posZ": center_z + dz,
                        "sizeX": 4,
                        "sizeY": 30,
                        "sizeZ": 4,
                        "colorR": colors[1][0],
                        "colorG": colors[1][1],
                        "colorB": colors[1][2],
                        "anchored": True,
                        "material": theme["accent_material"]
                    }
                })
        
        # Roof
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 37,
                "posZ": center_z,
                "sizeX": 52,
                "sizeY": 4,
                "sizeZ": 52,
                "colorR": colors[2][0],
                "colorG": colors[2][1],
                "colorB": colors[2][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
    
    elif structure_type == "platform":
        # Main platform
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 10,
                "posZ": center_z,
                "sizeX": 45,
                "sizeY": 5,
                "sizeZ": 45,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Gears
        for angle in range(0, 360, 90):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 18
            z = center_z + math.sin(rad) * 18
            
            steps.append({
                "action": "floatPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 15,
                    "posZ": z,
                    "sizeX": 8,
                    "sizeY": 2,
                    "sizeZ": 8,
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": "Metal",
                    "amplitude": 1.5,
                    "speed": 0.3
                }
            })
    
    elif structure_type == "reef":
        # Glowing coral formations
        for i in range(8):
            angle = (360 / 8) * i
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 20
            z = center_z + math.sin(rad) * 20
            height = random.uniform(15, 30)
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Crystal",
                    "posX": x,
                    "posY": center_y + height / 2,
                    "posZ": z,
                    "sizeX": random.uniform(4, 8),
                    "sizeY": height,
                    "sizeZ": random.uniform(4, 8),
                    "colorR": colors[i % 3][0],
                    "colorG": colors[i % 3][1],
                    "colorB": colors[i % 3][2],
                    "anchored": True,
                    "material": "ForceField"
                }
            })
    
    elif structure_type == "grove":
        # Trees with trunks and canopies
        for i in range(10):
            angle = (360 / 10) * i
            rad = math.radians(angle)
            radius = random.uniform(18, 25)
            x = center_x + math.cos(rad) * radius
            z = center_z + math.sin(rad) * radius
            
            # Trunk
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 15,
                    "posZ": z,
                    "sizeX": 4,
                    "sizeY": 25,
                    "sizeZ": 4,
                    "colorR": 101,
                    "colorG": 67,
                    "colorB": 33,
                    "anchored": True,
                    "material": "Wood"
                }
            })
            
            # Canopy
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 30,
                    "posZ": z,
                    "sizeX": 15,
                    "sizeY": 12,
                    "sizeZ": 15,
                    "colorR": colors[i % 3][0],
                    "colorG": colors[i % 3][1],
                    "colorB": colors[i % 3][2],
                    "anchored": True,
                    "material": "Fabric"
                }
            })
    
    elif structure_type == "zen":
        # Central platform
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 3,
                "posZ": center_z,
                "sizeX": 20,
                "sizeY": 2,
                "sizeZ": 20,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Rocks
        for i in range(7):
            angle = (360 / 7) * i + random.uniform(-15, 15)
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 18
            z = center_z + math.sin(rad) * 18
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + random.uniform(3, 7),
                    "posZ": z,
                    "sizeX": random.uniform(5, 10),
                    "sizeY": random.uniform(6, 12),
                    "sizeZ": random.uniform(5, 10),
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": theme["accent_material"]
                }
            })
    
    elif structure_type == "observatory":
        # Base
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 10,
                "posZ": center_z,
                "sizeX": 40,
                "sizeY": 15,
                "sizeZ": 40,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Middle tier
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 25,
                "posZ": center_z,
                "sizeX": 30,
                "sizeY": 12,
                "sizeZ": 30,
                "colorR": colors[1][0],
                "colorG": colors[1][1],
                "colorB": colors[1][2],
                "anchored": True,
                "material": theme["accent_material"]
            }
        })
        
        # Dome
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Crystal",
                "posX": center_x,
                "posY": center_y + 38,
                "posZ": center_z,
                "sizeX": 22,
                "sizeY": 18,
                "sizeZ": 22,
                "colorR": colors[2][0],
                "colorG": colors[2][1],
                "colorB": colors[2][2],
                "anchored": True,
                "material": "Glass"
            }
        })
        
        # Telescope
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 42,
                "posZ": center_z,
                "sizeX": 4,
                "sizeY": 15,
                "sizeZ": 4,
                "colorR": 100,
                "colorG": 100,
                "colorB": 100,
                "anchored": True,
                "material": "Metal"
            }
        })
    
    elif structure_type == "palace":
        # Main hall
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 18,
                "posZ": center_z,
                "sizeX": 35,
                "sizeY": 30,
                "sizeZ": 35,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Side wings
        for dx in [-30, 30]:
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x + dx,
                    "posY": center_y + 12,
                    "posZ": center_z,
                    "sizeX": 20,
                    "sizeY": 20,
                    "sizeZ": 25,
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": theme["accent_material"]
                }
            })
        
        # Pagoda roof
        for i in range(3):
            size = 40 - (i * 5)
            y = center_y + 35 + (i * 4)
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x,
                    "posY": y,
                    "posZ": center_z,
                    "sizeX": size,
                    "sizeY": 2,
                    "sizeZ": size,
                    "colorR": colors[2][0],
                    "colorG": colors[2][1],
                    "colorB": colors[2][2],
                    "anchored": True,
                    "material": "WoodPlanks"
                }
            })
    
    elif structure_type == "nexus":
        # Central prism
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Crystal",
                "posX": center_x,
                "posY": center_y + 20,
                "posZ": center_z,
                "sizeX": 15,
                "sizeY": 35,
                "sizeZ": 15,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": "ForceField"
            }
        })
        
        # Orbiting prisms
        for i in range(6):
            angle = (360 / 6) * i
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 20
            z = center_z + math.sin(rad) * 20
            
            steps.append({
                "action": "floatPart",
                "args": {
                    "partType": "Crystal",
                    "posX": x,
                    "posY": center_y + 20,
                    "posZ": z,
                    "sizeX": 8,
                    "sizeY": 20,
                    "sizeZ": 8,
                    "colorR": colors[i % 3][0],
                    "colorG": colors[i % 3][1],
                    "colorB": colors[i % 3][2],
                    "anchored": True,
                    "material": "Neon",
                    "amplitude": 3,
                    "speed": 0.6
                }
            })
    
    elif structure_type == "temple":
        # Base platform
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 8,
                "posZ": center_z,
                "sizeX": 45,
                "sizeY": 12,
                "sizeZ": 45,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Temple structure
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 22,
                "posZ": center_z,
                "sizeX": 30,
                "sizeY": 18,
                "sizeZ": 30,
                "colorR": colors[1][0],
                "colorG": colors[1][1],
                "colorB": colors[1][2],
                "anchored": True,
                "material": theme["accent_material"]
            }
        })
        
        # Fire pillars
        for angle in range(0, 360, 60):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 20
            z = center_z + math.sin(rad) * 20
            
            steps.append({
                "action": "floatPart",
                "args": {
                    "partType": "LightOrb",
                    "posX": x,
                    "posY": center_y + 20,
                    "posZ": z,
                    "sizeX": 4,
                    "sizeY": 4,
                    "sizeZ": 4,
                    "colorR": colors[2][0],
                    "colorG": colors[2][1],
                    "colorB": colors[2][2],
                    "anchored": True,
                    "material": "Neon",
                    "amplitude": 2.5,
                    "speed": 0.8
                }
            })
    
    elif structure_type == "spire":
        # Main spire
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Crystal",
                "posX": center_x,
                "posY": center_y + 35,
                "posZ": center_z,
                "sizeX": 10,
                "sizeY": 60,
                "sizeZ": 10,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": "ForceField"
            }
        })
        
        # Rings at different heights
        for i, height in enumerate([15, 30, 45]):
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x,
                    "posY": center_y + height,
                    "posZ": center_z,
                    "sizeX": 25 - (i * 3),
                    "sizeY": 2,
                    "sizeZ": 25 - (i * 3),
                    "colorR": colors[i % 3][0],
                    "colorG": colors[i % 3][1],
                    "colorB": colors[i % 3][2],
                    "anchored": True,
                    "material": "Glass"
                }
            })
        
        # Aurora effect orbs
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 15
            z = center_z + math.sin(rad) * 15
            
            steps.append({
                "action": "floatPart",
                "args": {
                    "partType": "LightOrb",
                    "posX": x,
                    "posY": center_y + random.uniform(20, 50),
                    "posZ": z,
                    "sizeX": 2,
                    "sizeY": 2,
                    "sizeZ": 2,
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": "Neon",
                    "amplitude": 4,
                    "speed": 0.4
                }
            })
    
    elif structure_type == "pavilion":
        # Platform
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 5,
                "posZ": center_z,
                "sizeX": 30,
                "sizeY": 3,
                "sizeZ": 30,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Corner posts
        for dx, dz in [(-12, -12), (12, -12), (-12, 12), (12, 12)]:
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x + dx,
                    "posY": center_y + 15,
                    "posZ": center_z + dz,
                    "sizeX": 3,
                    "sizeY": 20,
                    "sizeZ": 3,
                    "colorR": 101,
                    "colorG": 67,
                    "colorB": 33,
                    "anchored": True,
                    "material": "Wood"
                }
            })
        
        # Roof
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 27,
                "posZ": center_z,
                "sizeX": 35,
                "sizeY": 2,
                "sizeZ": 35,
                "colorR": colors[1][0],
                "colorG": colors[1][1],
                "colorB": colors[1][2],
                "anchored": True,
                "material": "WoodPlanks"
            }
        })
        
        # Cherry blossom trees
        for i in range(8):
            angle = (360 / 8) * i
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 20
            z = center_z + math.sin(rad) * 20
            
            # Trunk
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 10,
                    "posZ": z,
                    "sizeX": 2,
                    "sizeY": 15,
                    "sizeZ": 2,
                    "colorR": 101,
                    "colorG": 67,
                    "colorB": 33,
                    "anchored": True,
                    "material": "Wood"
                }
            })
            
            # Blossom canopy
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 20,
                    "posZ": z,
                    "sizeX": 10,
                    "sizeY": 8,
                    "sizeZ": 10,
                    "colorR": colors[2][0],
                    "colorG": colors[2][1],
                    "colorB": colors[2][2],
                    "anchored": True,
                    "material": "Fabric"
                }
            })
    
    elif structure_type == "clocktower":
        # Base
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 8,
                "posZ": center_z,
                "sizeX": 20,
                "sizeY": 12,
                "sizeZ": 20,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Tower shaft
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 30,
                "posZ": center_z,
                "sizeX": 12,
                "sizeY": 35,
                "sizeZ": 12,
                "colorR": colors[1][0],
                "colorG": colors[1][1],
                "colorB": colors[1][2],
                "anchored": True,
                "material": theme["accent_material"]
            }
        })
        
        # Clock faces
        for angle in [0, 90, 180, 270]:
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 7
            z = center_z + math.sin(rad) * 7
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 35,
                    "posZ": z,
                    "sizeX": 6,
                    "sizeY": 6,
                    "sizeZ": 1,
                    "colorR": 255,
                    "colorG": 255,
                    "colorB": 255,
                    "anchored": True,
                    "material": "Neon"
                }
            })
        
        # Gears
        for i in range(6):
            angle = (360 / 6) * i
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 15
            z = center_z + math.sin(rad) * 15
            
            steps.append({
                "action": "floatPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 25,
                    "posZ": z,
                    "sizeX": 5,
                    "sizeY": 1,
                    "sizeZ": 5,
                    "colorR": colors[2][0],
                    "colorG": colors[2][1],
                    "colorB": colors[2][2],
                    "anchored": True,
                    "material": "Metal",
                    "amplitude": 1,
                    "speed": 0.5
                }
            })
    
    elif structure_type == "shrine":
        # Main shrine building
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 10,
                "posZ": center_z,
                "sizeX": 25,
                "sizeY": 15,
                "sizeZ": 25,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Torii gates
        for i, dz in enumerate([-30, -20, -10]):
            # Left post
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x - 8,
                    "posY": center_y + 12,
                    "posZ": center_z + dz,
                    "sizeX": 2,
                    "sizeY": 18,
                    "sizeZ": 2,
                    "colorR": 200,
                    "colorG": 50,
                    "colorB": 50,
                    "anchored": True,
                    "material": "Wood"
                }
            })
            
            # Right post
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x + 8,
                    "posY": center_y + 12,
                    "posZ": center_z + dz,
                    "sizeX": 2,
                    "sizeY": 18,
                    "sizeZ": 2,
                    "colorR": 200,
                    "colorG": 50,
                    "colorB": 50,
                    "anchored": True,
                    "material": "Wood"
                }
            })
            
            # Top beam
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x,
                    "posY": center_y + 22,
                    "posZ": center_z + dz,
                    "sizeX": 20,
                    "sizeY": 2,
                    "sizeZ": 2,
                    "colorR": 200,
                    "colorG": 50,
                    "colorB": 50,
                    "anchored": True,
                    "material": "Wood"
                }
            })
        
        # Water pool
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 1,
                "posZ": center_z - 20,
                "sizeX": 30,
                "sizeY": 2,
                "sizeZ": 30,
                "colorR": colors[1][0],
                "colorG": colors[1][1],
                "colorB": colors[1][2],
                "anchored": True,
                "material": "Glass"
            }
        })
    
    elif structure_type == "moongarden":
        # Central moon pool
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 2,
                "posZ": center_z,
                "sizeX": 25,
                "sizeY": 3,
                "sizeZ": 25,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": "Glass"
            }
        })
        
        # Moon pillars
        for angle in range(0, 360, 40):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 20
            z = center_z + math.sin(rad) * 20
            
            steps.append({
                "action": "floatPart",
                "args": {
                    "partType": "LightOrb",
                    "posX": x,
                    "posY": center_y + 15,
                    "posZ": z,
                    "sizeX": 4,
                    "sizeY": 4,
                    "sizeZ": 4,
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": "Neon",
                    "amplitude": 3,
                    "speed": 0.3
                }
            })
        
        # Smaller pools
        for i in range(6):
            angle = (360 / 6) * i
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 30
            z = center_z + math.sin(rad) * 30
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 1,
                    "posZ": z,
                    "sizeX": 8,
                    "sizeY": 2,
                    "sizeZ": 8,
                    "colorR": colors[2][0],
                    "colorG": colors[2][1],
                    "colorB": colors[2][2],
                    "anchored": True,
                    "material": "Glass"
                }
            })
    
    elif structure_type == "canopy":
        # Ground level
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 3,
                "posZ": center_z,
                "sizeX": 35,
                "sizeY": 2,
                "sizeZ": 35,
                "colorR": colors[0][0],
                "colorG": colors[0][1],
                "colorB": colors[0][2],
                "anchored": True,
                "material": theme["structure_material"]
            }
        })
        
        # Tree trunks
        for i in range(8):
            angle = (360 / 8) * i
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * 15
            z = center_z + math.sin(rad) * 15
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + 20,
                    "posZ": z,
                    "sizeX": 5,
                    "sizeY": 35,
                    "sizeZ": 5,
                    "colorR": 101,
                    "colorG": 67,
                    "colorB": 33,
                    "anchored": True,
                    "material": "Wood"
                }
            })
        
        # Canopy platforms
        for level in range(3):
            radius = 18 - (level * 3)
            y = center_y + 25 + (level * 10)
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Normal",
                    "posX": center_x,
                    "posY": y,
                    "posZ": center_z,
                    "sizeX": radius * 2,
                    "sizeY": 1,
                    "sizeZ": radius * 2,
                    "colorR": colors[level % 3][0],
                    "colorG": colors[level % 3][1],
                    "colorB": colors[level % 3][2],
                    "anchored": True,
                    "material": "Fabric"
                }
            })
        
        # Vines
        for i in range(10):
            angle = random.uniform(0, 360)
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * random.uniform(10, 22)
            z = center_z + math.sin(rad) * random.uniform(10, 22)
            
            steps.append({
                "action": "floatPart",
                "args": {
                    "partType": "Normal",
                    "posX": x,
                    "posY": center_y + random.uniform(15, 35),
                    "posZ": z,
                    "sizeX": 1,
                    "sizeY": random.uniform(8, 12),
                    "sizeZ": 1,
                    "colorR": colors[1][0],
                    "colorG": colors[1][1],
                    "colorB": colors[1][2],
                    "anchored": True,
                    "material": "Fabric",
                    "amplitude": 1,
                    "speed": 0.2
                }
            })
    
    elif structure_type == "geode":
        # Outer shell
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 15,
                "posZ": center_z,
                "sizeX": 45,
                "sizeY": 25,
                "sizeZ": 45,
                "colorR": 80,
                "colorG": 80,
                "colorB": 90,
                "anchored": True,
                "material": theme["accent_material"]
            }
        })
        
        # Inner cavity
        steps.append({
            "action": "spawnPart",
            "args": {
                "partType": "Normal",
                "posX": center_x,
                "posY": center_y + 16,
                "posZ": center_z,
                "sizeX": 35,
                "sizeY": 18,
                "sizeZ": 35,
                "colorR": 20,
                "colorG": 20,
                "colorB": 30,
                "anchored": True,
                "material": "Slate"
            }
        })
        
        # Crystal formations
        for i in range(15):
            angle = random.uniform(0, 360)
            rad = math.radians(angle)
            radius = random.uniform(10, 16)
            x = center_x + math.cos(rad) * radius
            z = center_z + math.sin(rad) * radius
            
            height = random.uniform(8, 16)
            
            steps.append({
                "action": "spawnPart",
                "args": {
                    "partType": "Crystal",
                    "posX": x,
                    "posY": center_y + 8 + (height / 2),
                    "posZ": z,
                    "sizeX": random.uniform(2, 5),
                    "sizeY": height,
                    "sizeZ": random.uniform(2, 5),
                    "colorR": colors[i % 3][0],
                    "colorG": colors[i % 3][1],
                    "colorB": colors[i % 3][2],
                    "anchored": True,
                    "material": "ForceField"
                }
            })
    
    # === CLUSTER (REQUIRED) ===
    steps.append({
        "action": "spawnCluster",
        "args": {
            "partType": random.choice(["LightOrb", "Crystal", theme["main_part"]]),
            "centerposX": center_x + random.randint(-30, 30),
            "centerposY": center_y + random.randint(5, 20),
            "centerposZ": center_z + random.randint(-30, 30),
            "count": random.randint(8, 15),
            "radius": random.randint(8, 15)
        }
    })
    
    # === PARTICLES (REQUIRED) ===
    particle_textures = [
        "rbxasset://textures/particles/sparkles_main.dds",
        "rbxasset://textures/particles/cloud_main.dds",
        "rbxasset://textures/particles/soft_smoke.dds"
    ]
    
    steps.append({
        "action": "addParticles",
        "args": {
            "posX": center_x,
            "posY": center_y + 25,
            "posZ": center_z,
            "texture": random.choice(particle_textures),
            "rate": random.randint(30, 60),
            "lifetime": random.randint(8, 14),
            "size": random.uniform(1.5, 4)
        }
    })
    
    # === DIALOGUE CHARACTER (REQUIRED) ===
    npc_x = center_x + random.randint(-40, 40)
    npc_z = center_z + random.randint(-40, 40)
    
    steps.append({
        "action": "addDialogueCharacter",
        "args": {
            "tone": random.choice(["Friendly", "Neutral"]),
            "posX": npc_x,
            "posY": center_y + 2,
            "posZ": npc_z,
            "initialdialogue": "Welcome traveler!",
            "dialogue1": "What is this place?",
            "dialogue1response": f"This is the {theme['name']}.",
            "dialogue2": "It's beautiful!",
            "dialogue2response": "I'm glad you like it!"
        }
    })
    
    # === ASSET PROP (REQUIRED) ===
    prop_list = ["Boat_01", "Cart_01", "Crate_01", "Fence_01", "Lantern_01", "Sign_01", "Tent_01", "Torch_01", "Well_01"]
    prop_x = center_x + random.randint(-35, 35)
    prop_z = center_z + random.randint(-35, 35)
    
    steps.append({
        "action": "addAssetProps",
        "args": {
            "prop": random.choice(prop_list),
            "posX": prop_x,
            "posY": center_y + 2,
            "posZ": prop_z
        }
    })
    
    # === BRAINROT (REQUIRED) ===
    brainrot_list = ["a1", "a2", "a3", "b1", "b2", "c1", "c2"]
    brainrot_x = center_x + random.randint(-35, 35)
    brainrot_z = center_z + random.randint(-35, 35)
    
    steps.append({
        "action": "addBrainRot",
        "args": {
            "rot": random.choice(brainrot_list),
            "posX": brainrot_x,
            "posY": center_y + 2,
            "posZ": brainrot_z
        }
    })
    
    scene = {
        "mood": theme["name"],
        "seed_hint": f"ultimate handcrafted {theme['name'].lower()}",
        "steps": steps
    }
    
    print(f"✨ Generated ULTIMATE world: {theme['name']}")
    print(f"📊 Total steps: {len(steps)}")
    print(f"🏗️  Structure type: {structure_type}")
    print(f"🎨 Theme colors: {colors}")
    
    return json.dumps(scene)