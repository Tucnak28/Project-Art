import io
from PIL import Image
# define the colors and their names
LBonemeal = (242, 249, 252)
Bonemeal = (208, 214, 217)
DBonemeal = (170, 175, 178)
DDBonemeal = (127, 131, 133)

LInk_sac = (25, 25, 25)
Ink_sac = (21, 21, 21)
DInk_sac = (17, 17, 17)
DDInk_sac = (13, 13, 13)

LEmerald = (57, 214, 0)
Emerald = (49, 185, 0)
DEmerald = (39, 151, 0)
DDEmerald = (30, 113, 0)

LYellow_dye = (50, 226, 226)
Yellow_dye = (43, 195, 195)
DYellow_dye = (36, 159, 159)
DDYellow_dye = (27, 120, 120)

LPink_dye = (163, 125, 239)
Pink_dye = (140, 108, 206)
DPink_dye = (115, 88, 168)
DDPink_dye = (86, 66, 126)

LLapis_lazuli = (176, 75, 50)
Lapis_lazuli = (151, 64, 43)
DLapis_lazuli = (124, 52, 36)
DDLapis_lazuli = (93, 39, 27)

LMagenta_dye = (213, 75, 176)
Magenta_dye = (184, 64, 151)
DMagenta_dye = (150, 52, 124)
DDMagenta_dye = (113, 39, 93)

LChorus_fruit = (87, 72, 121)
Chorus_fruit = (74, 61, 104)
DChorus_fruit = (61, 50, 85)
DDChorus_fruit = (45, 38, 63)

LLime_dye = (25, 202, 125)
Lime_dye = (21, 174, 108)
DLime_dye = (17, 142, 88)
DDLime_dye = (13, 107, 66)

LApple = (45, 59, 140)
Apple = (39, 50, 121)
DApple = (32, 41, 99)
DDApple = (24, 31, 74)

LGold_nugget = (76, 235, 247)
Gold_nugget = (65, 203, 212)
DGold_nugget = (53, 166, 174)
DDGold_nugget = (39, 125, 130)

LGlowstone_dust = (36, 131, 184)
Glowstone_dust = (31, 113, 158)
DGlowstone_dust = (25, 92, 129)
DDGlowstone_dust = (19, 69, 97)

LOrange_dye = (50, 125, 213)
Orange_dye = (43, 108, 184)
DOrange_dye = (36, 88, 150)
DDOrange_dye = (27, 66, 113)

LLight_blue_dye = (213, 151, 101)
Light_blue_dye = (213, 151, 101)
DLight_blue_dye = (150, 107, 71)
DDLight_blue_dye = (113, 80, 53)

LRed_dye = (0, 0, 252)
Red_dye = (0, 0, 217)
DRed_dye = (0, 0, 178)
DDRed_dye = (0, 0, 133)

LOak_leaves = (0, 123, 0)
Oak_leaves = (0, 105, 0)
DOak_leaves = (0, 86, 0)
DDOak_leaves = (0, 64, 0)

LPoisonous_potato = (41, 81, 75)
Poisonous_potato = (36, 69, 64)
DPoisonous_potato = (29, 56, 52)
DDPoisonous_potato = (22, 42, 39)

LDark_oak_log = (71, 118, 141)
Dark_oak_log = (61, 101, 122)
DDark_oak_log = (49, 83, 99)
DDDark_oak_log = (38, 62, 74)

LMagma_cream = (36, 81, 157)
Magma_cream = (31, 69, 135)
DMagma_cream = (25, 56, 111)
DDMagma_cream = (19, 42, 83)

LPurple_dye = (176, 62, 125)
Purple_dye = (151, 53, 108)
DPurple_dye = (124, 43, 88)
DDPurple_dye = (93, 33, 66)

LNether_wart = (0, 2, 111)
Nether_wart = (0, 1, 95)
DNether_wart = (0, 1, 78)
DDNether_wart = (0, 1, 58)

LPumpkin_seeds = (161, 230, 244)
Pumpkin_seeds = (138, 199, 210)
DPumpkin_seeds = (114, 162, 172)
DDPumpkin_seeds = (85, 122, 128)

LIce = (252, 158, 158)
Ice = (217, 136, 136)
DIce = (178, 111, 111)
DDIce = (133, 83, 83)

LMycelium = (136, 107, 111)
Mycelium = (118, 92, 95)
DMycelium = (96, 75, 78)
DDMycelium = (72, 56, 58)

LGrass = (55, 176, 125)
Grass = (47, 151, 108)
DGrass = (39, 124, 88)
DDGrass = (29, 93, 66)

LPrismarine_crystals = (210, 216, 91)
Prismarine_crystals = (181, 186, 78)
DPrismarine_crystals = (148, 152, 63)
DDPrismarine_crystals = (111, 114, 47)

LCocoa_beans = (50, 75, 101)
Cocoa_beans = (43, 64, 87)
DCocoa_beans = (36, 52, 71)
DDCocoa_beans = (27, 39, 53)

LPurpur_block = (91, 61, 75)
Purpur_block = (78, 52, 64)
DPurpur_block = (63, 42, 52)
DDPurpur_block = (47, 32, 39)

LLapis_lazuli_ore = (252, 126, 73)
Lapis_lazuli_ore = (217, 109, 62)
DLapis_lazuli_ore = (178, 89, 51)
DDLapis_lazuli_ore = (133, 66, 39)

LLapis_lazuli_block = (252, 63, 63)
Lapis_lazuli_block = (217, 54, 54)
DLapis_lazuli_block = (178, 44, 44)
DDLapis_lazuli_block = (133, 33, 33)

LGray_dye = (182, 166, 162)
Gray_dye = (156, 142, 139)
DGray_dye = (127, 117, 114)
DDGray_dye = (96, 87, 85)

LEgg = (159, 175, 207)
Egg = (136, 150, 178)
DEgg = (112, 123, 145)
DDEgg = (84, 92, 109)

LCyan_Dye = (151, 125, 75)
Cyan_Dye = (130, 108, 64)
DCyan_Dye = (107, 88, 52)
DDCyan_Dye = (80, 66, 39)

LMelon_seeds = (76, 108, 149)
Melon_seeds = (65, 93, 128)
DMelon_seeds = (53, 75, 105)
DDMelon_seeds = (39, 56, 78)

colors = [LBonemeal, Bonemeal, DBonemeal, DDBonemeal, LInk_sac, Ink_sac, DInk_sac, DDInk_sac, LEmerald, Emerald, DEmerald, DDEmerald, LYellow_dye, Yellow_dye, DYellow_dye, DDYellow_dye, LPink_dye, Pink_dye, DPink_dye, DDPink_dye, LLapis_lazuli, Lapis_lazuli, DLapis_lazuli, DDLapis_lazuli, LMagenta_dye, Magenta_dye, DMagenta_dye, DDMagenta_dye,  LChorus_fruit, Chorus_fruit, DChorus_fruit, DDChorus_fruit,  LLime_dye, Lime_dye, DLime_dye, DDLime_dye,  LApple, Apple, DApple, DDApple,  LGold_nugget, Gold_nugget, DGold_nugget, DDGold_nugget, LGlowstone_dust, Glowstone_dust, DGlowstone_dust, DDGlowstone_dust,  LOrange_dye, Orange_dye, DOrange_dye, DDOrange_dye,  LLight_blue_dye, Light_blue_dye, DLight_blue_dye, DDLight_blue_dye,  LRed_dye, Red_dye, DRed_dye, DDRed_dye, LOak_leaves, Oak_leaves, DOak_leaves, DDOak_leaves, LPoisonous_potato, Poisonous_potato, DPoisonous_potato, DDPoisonous_potato,  LDark_oak_log, Dark_oak_log, DDark_oak_log, DDDark_oak_log,  LMagma_cream, Magma_cream, DMagma_cream, DDMagma_cream,  LPurple_dye, Purple_dye, DPurple_dye, DDPurple_dye, LNether_wart, Nether_wart, DNether_wart, DDNether_wart,  LPumpkin_seeds, Pumpkin_seeds, DPumpkin_seeds, DDPumpkin_seeds, LIce, Ice, DIce, DDIce, LMycelium, Mycelium, DMycelium, DDMycelium, LGrass, Grass, DGrass, DDGrass,  LPrismarine_crystals, Prismarine_crystals, DPrismarine_crystals, DDPrismarine_crystals, LCocoa_beans, Cocoa_beans, DCocoa_beans, DDCocoa_beans, LPurpur_block, Purpur_block, DPurpur_block, DDPurpur_block, LLapis_lazuli_ore, Lapis_lazuli_ore, DLapis_lazuli_ore, DDLapis_lazuli_ore, LLapis_lazuli_block, Lapis_lazuli_block, DLapis_lazuli_block, DDLapis_lazuli_block, LGray_dye, Gray_dye, DGray_dye, DDGray_dye, LEgg, Egg, DEgg, DDEgg,	 LCyan_Dye, Cyan_Dye, DCyan_Dye, DDCyan_Dye, LMelon_seeds, Melon_seeds, DMelon_seeds, DDMelon_seeds]
color_names = {
  LBonemeal: "LBonemeal",
  Bonemeal: "Bonemeal",
  DBonemeal: "DBonemeal",
  DDBonemeal: "DDBonemeal",
  LInk_sac: "LInk_sac",
  Ink_sac: "Ink_sac",
  DInk_sac: "DInk_sac",
  DDInk_sac: "DDInk_sac",
  LEmerald: "LEmerald",
  Emerald: "Emerald",
  DEmerald: "DEmerald",
  DDEmerald: "DDEmerald",
  LYellow_dye: "LYellow_dye",
  Yellow_dye: "Yellow_dye",
  DYellow_dye: "DYellow_dye",
  DDYellow_dye: "DDYellow_dye",
  LPink_dye: "LPink_dye",
  Pink_dye: "Pink_dye",
  DPink_dye: "DPink_dye",
  DDPink_dye: "DDPink_dye",
  LLapis_lazuli: "LLapis_lazuli",
  Lapis_lazuli: "Lapis_lazuli",
  DLapis_lazuli: "DLapis_lazuli",
  DDLapis_lazuli: "DDLapis_lazuli",
  LMagenta_dye: "LMagenta_dye",
  Magenta_dye: "Magenta_dye",
  DMagenta_dye: "DMagenta_dye",
  DDMagenta_dye: "DDMagenta_dye",
  LChorus_fruit: "LChorus_fruit",
  Chorus_fruit: "Chorus_fruit",
  DChorus_fruit: "DChorus_fruit",
  DDChorus_fruit: "DDChorus_fruit",
  LLime_dye: "LLime_dye",
  Lime_dye: "Lime_dye",
  DLime_dye: "DLime_dye",
  DDLime_dye: "DDLime_dye",
  LApple: "LApple",
  Apple: "Apple",
  DApple: "DApple",
  DDApple: "DDApple",
  LGold_nugget: "LGold_nugget",
  Gold_nugget: "Gold_nugget",
  DGold_nugget: "DGold_nugget",
  DDGold_nugget: "DDGold_nugget",
  LGlowstone_dust: "LGlowstone_dust",
  Glowstone_dust: "Glowstone_dust",
  DGlowstone_dust: "DGlowstone_dust",
  DDGlowstone_dust: "DDGlowstone_dust",
  LOrange_dye: "LOrange_dye",
  Orange_dye: "Orange_dye",
  DOrange_dye: "DOrange_dye",
  DDOrange_dye: "DDOrange_dye",
  LLight_blue_dye: "LLight_blue_dye",
  Light_blue_dye: "Light_blue_dye",
  DLight_blue_dye: "DLight_blue_dye",
  DDLight_blue_dye: "DDLight_blue_dye",
  LRed_dye: "LRed_dye",
  Red_dye: "Red_dye",
  DRed_dye: "DRed_dye",
  DDRed_dye: "DDRed_dye",
  LOak_leaves: "LOak_leaves",
  Oak_leaves: "Oak_leaves",
  DOak_leaves: "DOak_leaves",
  DDOak_leaves: "DDOak_leaves",
  LPoisonous_potato: "LPoisonous_potato",
  Poisonous_potato: "Poisonous_potato",
  DPoisonous_potato: "DPoisonous_potato",
  DDPoisonous_potato: "DDPoisonous_potato",
  LDark_oak_log: "LDark_oak_log",
  Dark_oak_log: "Dark_oak_log",
  DDark_oak_log: "DDark_oak_log",
  DDDark_oak_log: "DDDark_oak_log",
  LMagma_cream: "LMagma_cream",
  Magma_cream: "Magma_cream",
  DMagma_cream: "DMagma_cream",
  DDMagma_cream: "DDMagma_cream",
  LPurple_dye: "LPurple_dye",
  Purple_dye: "Purple_dye",
  DPurple_dye: "DPurple_dye",
  DDPurple_dye: "DDPurple_dye",
  LNether_wart: "LNether_wart",
  Nether_wart: "Nether_wart",
  DNether_wart: "DNether_wart",
  DDNether_wart: "DDNether_wart",
  LPumpkin_seeds: "LPumpkin_seeds",
  Pumpkin_seeds: "Pumpkin_seeds",
  DPumpkin_seeds: "DPumpkin_seeds",
  DDPumpkin_seeds: "DDPumpkin_seeds",
  LIce: "LIce",
  Ice: "Ice",
  DIce: "DIce",
  DDIce: "DDIce",
  LMycelium: "LMycelium",
  Mycelium: "Mycelium",
  DMycelium: "DMycelium",
  DDMycelium: "DDMycelium",
  LGrass: "LGrass",
  Grass: "Grass",
  DGrass: "DGrass",
  DDGrass: "DDGrass",
  LPrismarine_crystals: "LPrismarine_crystals",
  Prismarine_crystals: "Prismarine_crystals",
  DPrismarine_crystals: "DPrismarine_crystals",
  DDPrismarine_crystals: "DDPrismarine_crystals",
  LCocoa_beans: "LCocoa_beans",
  Cocoa_beans: "Cocoa_beans",
  DCocoa_beans: "DCocoa_beans",
  DDCocoa_beans: "DDCocoa_beans",
  LPurpur_block: "LPurpur_block",
  Purpur_block: "Purpur_block",
  DPurpur_block: "DPurpur_block",
  DDPurpur_block: "DDPurpur_block",
  LLapis_lazuli_ore: "LLapis_lazuli_ore",
  Lapis_lazuli_ore: "Lapis_lazuli_ore",
  DLapis_lazuli_ore: "DLapis_lazuli_ore",
  DDLapis_lazuli_ore: "DDLapis_lazuli_ore",
  LLapis_lazuli_block: "LLapis_lazuli_block",
  Lapis_lazuli_block: "Lapis_lazuli_block",
  DLapis_lazuli_block: "DLapis_lazuli_block",
  DDLapis_lazuli_block: "DDLapis_lazuli_block",
  LGray_dye: "LGray_dye",
  Gray_dye: "Gray_dye",
  DGray_dye: "DGray_dye",
  DDGray_dye: "DDGray_dye",
  LEgg: "LEgg",
  Egg: "Egg",
  DEgg: "DEgg",
  DDEgg: "DDEgg",
  LCyan_Dye: "LCyan_Dye",
  Cyan_Dye: "Cyan_Dye",
  DCyan_Dye: "DCyan_Dye",
  DDCyan_Dye: "DDCyan_Dye",
  LMelon_seeds: "LMelon_seeds",
  Melon_seeds: "Melon_seeds",
  DMelon_seeds: "DMelon_seeds",
  DDMelon_seeds: "DDMelon_seeds"
}

# open the image file
im = Image.open("image.png")

# get the width and height of the image
width, height = im.size

# create an empty list to store the names of the most similar colors
similar_color_names = []

# iterate over the pixels in the image
for y in range(height):
  for x in range(width):
    # get the pixel at position (x, y)
    pixel = im.getpixel((x, y))

    # find the most similar color
    min_distance = float("inf")
    min_color = None
    for color in colors:
      distance = sum((p - c) ** 2 for p, c in zip(pixel, color)) ** 0.5
      if distance < min_distance:
        min_distance = distance
        min_color = color

    # add the name of the most similar color to the list
    similar_color_names.append(color_names[min_color])

# open a file in write mode
with io.open("similar_colors.txt", "w") as f:
  # write the array of similar color names to the file
  f.write("{")
  for color_name in similar_color_names:
    f.write(color_name + ", ")
    
with io.open("similar_colors.txt", "r") as f: 
    text = f.read()[:-2]

with io.open("similar_colors.txt", "w") as f:
    f.write(text)
    f.write("}")