import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord import Interaction
from itertools import cycle
import os

intents = discord.Intents.default()
intents.members = False

client = commands.Bot(command_prefix=',', intents=intents)


bot_status = cycle(["/help for help", "/help for help", "/help for help", "/help for help"])


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))


@client.event
async def on_ready():
    await client.tree.sync()
    print("the bot is now ready for use!")
    change_status.start()
    print("-----------------------------")


#/help
@client.tree.command(name="help")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title="To Calculate", description=
                                            f"\n**----------------------| BOOM COST |-------------------------**"
                                            f"\n"
                                            f"\n**Rocket :**"
                                            f"\n/rocket (amount of Rockets)"
                                            f"\n"
                                            f"\n**Timed Explosive Charge :**"
                                            f"\n/c4 (amount of Timed Explosive Charge)"
                                            f"\n"
                                            f"\n**Explosive Ammo :**"
                                            f"\n/explosive_ammo (amount of Explosive Ammo)"
                                            f"\n"
                                            f"\n**Satchel Charge :**"
                                            f"\n/satchel_charge (amount of Satchel Charges)"
                                            f"\n"
                                            f"\n**Beancan Grenade :**"
                                            f"\n/beancan_grenade (amount of Beancan Grenade)"
                                            f"\n"
                                            f"\n**F1 Grenade :**"
                                            f"\n/f1_grenade (amount of F1 Grenade)"
                                            f"\n"
                                            f"\n**Molotov Cocktails :**"
                                            f"\n/molotov_cocktails (amount of molotov cocktails)"
                                            f"\n"
                                            f"\n**High Velocity Rockets :**"
                                            f"\n/high_velocity_rocket (amount of High Velocity Rocket)"
                                            f"\n"
                                            f"\n**Explosive :**"
                                            f"\n/explosive (amount of Explosives)"
                                            f"\n"
                                            f"\n**Incendiary Rocket :**"
                                            f"\n/incendiary_rocket (amount of Incendiary Rockets)"
                                            f"\n"
                                            f"\n**Torpedo**"
                                            f"\n/torpedo (ammount of Torpedoes)"
                                            f"\n"
                                            f"\n**----------------------| DURABILITY |-------------------------**"      
                                            f"\n"
                                            f"\n**Wooden Walls :**"
                                            f"\n/wooden_wall (layers of Wooden Walls)"
                                            f"\n"
                                            f"\n**Stone Walls :**"
                                            f"\n/stone_wall (layers of Stone Walls)"
                                            f"\n"
                                            f"\n**Metal Walls :**"
                                            f"\n/metal_wall (layers of Metal Walls)"
                                            f"\n"
                                            f"\n**Armored Walls :**"
                                            f"\n/armored_wall (layers of Armored Walls)"
                                            f"\n"
                                            f"\n**Wooden Doors :**"
                                            f"\n/wooden_door (layers of Wooden Doors)"
                                            f"\n"
                                            f"\n**Sheet Metal Door :**"
                                            f"\n/sheet_metal_door (layers of Sheet Metal Doors)"
                                            f"\n"
                                            f"\n**Garage Doors :**"
                                            f"\n/garage_door (layers of Garage Doors)"
                                            f"\n"
                                            f"\n**Armored Doors :**"
                                            f"\n/armored_door (layers of Armored Doors)"
                                            f"\n"
                                            f"\n**High External Wooden Walls :**"
                                            f"\n/high_external_wooden_wall (layers of High External Wooden Walls)"
                                            f"\n"
                                            f"\n**High External Stone Walls :**"
                                            f"\n/high_external_stone_wall (layers of High External Stone Walls)"
                                            f"\n"
                                            f"\n**------------------| VEHICLE DURABILITY |---------------------**"
                                            f"\n"
                                            f"\n**Bradley APC**"
                                            f"\n/bradley_apc (number of Bradley APC)"
                                            f"\n"
                                            f"\n**Tugboat**"
                                            f"\n/tugboat (number of Tugboats)"
                                            f"\n"
                                            f"\n"
                                            f"\n"
                                            f"\n*made by Nomad 1-1*"))


#Boom Cost : -----------------------------------------------------------------------------------------------------------


#Rockets
@client.tree.command(name="rocket")
@app_commands.describe(amount = "Number of rockets")
async def rocket(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 1400)
    lowgrade = (amount * 30)
    metal = (amount * 100)
    charcoal = (amount * 1950)
    metal_pipes = (amount * 2)
    explosives = (amount * 10)
    gun_powder = (amount * 150)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x Rockets", description=
                                            f"**RAW COST OF {amount}X ROCKETS**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nLowgrade : {lowgrade}"
                                            f"\nMetal : {metal}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nMetal Pipes : {metal_pipes}"
                                            f"\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X ROCKETS**"
                                            f"\n"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nMetal Pipes : {metal_pipes}"
                                            f"\nExplosives : {explosives}"))


#C4
@client.tree.command(name="c4")
@app_commands.describe(amount = "Number of C4")
async def c4(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 2200)
    lowgrade = (amount * 60)
    metal = (amount * 200)
    charcoal = (amount * 3000)
    techtrash = (amount * 2)
    explosives = (amount * 20)
    cloth = (amount * 5)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x Timed Explosive Charge", description="\n"
                                            f"**RAW COST OF {amount}X TIMED EXPLOSIVE CHARGE**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nLowgrade : {lowgrade}"
                                            f"\nMetal : {metal}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nCloth : {cloth}"
                                            f"\nTech Trash : {techtrash}"
                                            f"\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X TIMED EXPLOSIVE CHARGE**"
                                            f"\n"
                                            f"\nTech Trash : {techtrash}"
                                            f"\nExplosives : {explosives}"
                                            f"\nCloth : {cloth}"))


#explo ammo
@client.tree.command(name="explosive_ammo")
@app_commands.describe(amount = "Number of explosive ammo")
async def explosive_ammo(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 15)
    csulfur = (amount * 5)
    metal = (amount * 5)
    charcoal = (amount * 15)
    gun_powder = (amount * 10)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x Explosive Ammo", description="\n"
                                            f"**RAW COST OF {amount}X EXPLOSIVE AMMO**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nMetal : {metal}"
                                            f"\nCharcoal : {charcoal}"
                                            "\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X EXPLOSIVE AMMO**"
                                            f"\n"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nMetal : {metal}"
                                            f"\nSulfur : {csulfur}"))


#satchel charge
@client.tree.command(name="satchel_charge")
@app_commands.describe(amount = "Number of satchel charge")
async def explosive_ammo(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 480)
    charcoal = (amount * 720)
    gun_powder = (amount * 240)
    rope = (amount * 1)
    beancan_grenade = (amount * 4)
    small_stash = (amount * 1)
    cloth = (amount * 10)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x Satchel Charges", description="\n"
                                            f"**RAW COST OF {amount}X SATCHEL CHARGES**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nCloth : {cloth}"
                                            f"\nRope : {rope}"
                                            "\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X SATCHEL CHARGES**"
                                            f"\n"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nRope : {rope}"
                                            f"\nBeancan Granade : {beancan_grenade}"
                                            f"\nSmall Stash : {small_stash}"))


#beancan grenade
@client.tree.command(name="beancan_grenade")
@app_commands.describe(amount = "Number of beancan grenades")
async def beancan_grenade(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 120)
    charcoal = (amount * 180)
    gun_powder = (amount * 60)
    metal = (amount * 20)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x Beancan Grenades", description="\n"
                                            f"**RAW COST OF {amount}X BEANCAN GRENADES**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nMetal : {metal}"
                                            "\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X BEANCAN GRENADES**"
                                            f"\n"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nMetal : {metal}"))


#hv rocket
@client.tree.command(name="high_velocity_rocket")
@app_commands.describe(amount = "Number of high velocity rocket")
async def high_velocity_rocket(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 200)
    charcoal = (amount * 300)
    gun_powder = (amount * 100)
    metal_pipes = (amount * 1)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x High Velocity Rockets", description="\n"
                                            f"**RAW COST OF {amount}X HIGH VELOCITY ROCKETS**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nMetal Pipes : {metal_pipes}"
                                            "\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X HIGH VELOCITY ROCKETS**"
                                            f"\n"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nMetal Pipes : {metal_pipes}"))


#explosives
@client.tree.command(name="explosive")
@app_commands.describe(amount = "Number of explosives")
async def explosive(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 110)
    charcoal = (amount * 150)
    gun_powder = (amount * 50)
    low_grade = (amount * 3)
    nsulfur = (amount * 10)
    metal = (amount * 10)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x Explosives", description="\n"
                                            f"**RAW COST OF {amount}X EXPLOSIVES**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nLow Grade Fuel : {low_grade}"
                                            f"\nMetal : {metal}"
                                            "\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X EXPLOSIVES**"
                                            f"\n"
                                            f"\nSulfur : {nsulfur}"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nLow Grade Fuel : {low_grade}"
                                            f"\nMetal : {metal}"))


#Torpedo
@client.tree.command(name="torpedo")
@app_commands.describe(amount = "Number of torpedoes")
async def torpedo(interaction: discord.Interaction, amount:int):
    sulfur = ((amount * 20) * 3)
    charcoal = ((amount * 30) * 3)
    metalpipes = (amount * 1)
    gun_powder = ((amount * 10) * 3)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount * 3}x Torpedoes", description="\n"
                                            f"**RAW COST OF {amount * 3}X TORPEDOES**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nMetal Pipes : {metalpipes}"
                                            "\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount * 3}X TORPEDOES**"
                                            f"\n"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nMetal Pipes : {metalpipes}"))


#incen rocket
@client.tree.command(name="incendiary_rocket")
@app_commands.describe(amount = "Number of incendiary rocket")
async def incendiary_rocket(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 610)
    charcoal = (amount * 900)
    gun_powder = (amount * 250)
    metal_pipes = (amount * 2)
    low_grade = (amount * 250)
    explosives = (amount * 1)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x Incendiary Rockets", description="\n"
                                            f"**RAW COST OF {amount}X INCENDIARY ROCKETS**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nMetal Pipes : {metal_pipes}"
                                            f"\nLow Grade Fuel : {low_grade}"
                                            "\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X INCENDIARY ROCKETS**"
                                            f"\n"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nMetal Pipes : {metal_pipes}"
                                            f"\nExplosives : {explosives}"
                                            f"\nLow Grade Fuel : {low_grade}"))


#F1 Grenade
@client.tree.command(name="f1_grenade")
@app_commands.describe(amount = "Number of f1 grenades")
async def f1_grenade(interaction: discord.Interaction, amount:int):
    sulfur = (amount * 60)
    charcoal = (amount * 90)
    gun_powder = (amount * 30)
    metal = (amount * 25)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x F1 Grenades", description="\n"
                                            f"**RAW COST OF {amount}X F1 GRENADES**"
                                            "\n"
                                            f"\nSulfur : {sulfur}"
                                            f"\nCharcoal : {charcoal}"
                                            f"\nMetal : {metal}"
                                            "\n"
                                            f"\n**MATERIALS YOU NEED TO CRAFT {amount}X F1 GRENADES**"
                                            f"\n"
                                            f"\nGun Powder : {gun_powder}"
                                            f"\nMetal : {metal}"))


#Molotov
@client.tree.command(name="molotov_cocktail")
@app_commands.describe(amount = "Number of molotov cocktails")
async def molotov_cocktail(interaction: discord.Interaction, amount:int):
    low_grade = (amount * 50)
    cloth = (amount * 10)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{amount}x Molotov Cocktails", description="\n"
                                            f"**COST OF {amount}X MOLOTOV COCKTAILS**"
                                            "\n"
                                            f"\nLow Grade Fuel : {low_grade}"
                                            f"\nCloth : {cloth}"))


#DURABILITY PART : -----------------------------------------------------------------------------------------------------


#stone wall
@client.tree.command(name="stone_wall")
@app_commands.describe(layers = "number of stone walls?")
async def stone_wall(interaction: discord.Interaction, layers:int):
    #hard side
    rocket = (layers * 4)
    c4 = (layers * 2)
    explo_ammo = (layers * 185)
    mlrs = (layers * 3)
    satchel_charge = (layers * 10)
    beancan_grenade = (layers * 46)
    hv_rocket = (layers * 32)
    f1 = (layers * 182)
    he = (layers * 29)
    #soft side
    sorocket = (layers * 4)
    soc4 = (layers * 2)
    soexplo_ammo = (layers * 173)
    somlrs = (layers * 3)
    sosatchel_charge = (layers * 10)
    sobeancan_grenade = (layers * 46)
    sohv_rocket = (layers * 31)
    sof1 = (layers * 182)
    sohe = (layers * 27)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x Stone Walls", description="\n"
                                            f"**HARD SIDE**"
                                            "\n"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"
                                            "\n"
                                            f"\n**SOFT SIDE**"
                                            f"\n"
                                            f"\nJack Hammer : 1"
                                            f"\nRockets : {sorocket}"
                                            f"\nTimed Explosive Charge : {soc4}"
                                            f"\nExplosive Ammo : {soexplo_ammo}"
                                            f"\nSatchel Charge : {sosatchel_charge}"
                                            f"\nBeancan Grenade : {sobeancan_grenade}"
                                            f"\nMLRS Rockets : {somlrs}"
                                            f"\nHV Rockets : {sohv_rocket}"
                                            f"\nF1 Grenade : {sof1}"
                                            f"\nHE Grenade : {sohe}"))


#wooden wall
@client.tree.command(name="wooden_wall")
@app_commands.describe(layers = "number of wooden walls?")
async def wooden_wall(interaction: discord.Interaction, layers:int):
    #hard side
    incen_rocket = (layers * 1)
    molotov = (layers * 4)
    fire_arrow = (layers * 125)
    flame_thrower = (layers * 206)
    rocket = (layers * 2)
    c4 = (layers * 1)
    explo_ammo = (layers * 49)
    mlrs = (layers * 1)
    satchel_charge = (layers * 3)
    beancan_grenade = (layers * 13)
    hv_rocket = (layers * 9)
    f1 = (layers * 59)
    he = (layers * 8)
    #soft side
    soincen_rocket = (layers * 1)
    somolotov = (layers * 4)
    sofire_arrow = (layers * 125)
    soflame_thrower = (layers * 206)
    sorocket = (layers * 2)
    soc4 = (layers * 1)
    soexplo_ammo = (layers * 44)
    somlrs = (layers * 1)
    sosatchel_charge = (layers * 3)
    sobeancan_grenade = (layers * 13)
    sohv_rocket = (layers * 8)
    sof1 = (layers * 59)
    sohe = (layers * 8)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x Wooden Walls", description="\n"
                                            f"**HARD SIDE**"
                                            "\n"
                                            f"\nIncendiary Rocket : {incen_rocket}"
                                            f"\nMolotov Cocktail : {molotov}"
                                            f"\nFire Arrow : {fire_arrow}"
                                            f"\nFlame Thrower : {flame_thrower}"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"
                                            "\n"
                                            f"\n**SOFT SIDE**"
                                            f"\n"
                                            f"\nSalvaged Sword : 1"
                                            f"\nIncendiary Rocket : {soincen_rocket}"
                                            f"\nMolotov Cocktail : {somolotov}"
                                            f"\nFire Arrow : {sofire_arrow}"
                                            f"\nFlame Thrower : {soflame_thrower}"
                                            f"\nRockets : {sorocket}"
                                            f"\nTimed Explosive Charge : {soc4}"
                                            f"\nExplosive Ammo : {soexplo_ammo}"
                                            f"\nSatchel Charge : {sosatchel_charge}"
                                            f"\nBeancan Grenade : {sobeancan_grenade}"
                                            f"\nMLRS Rockets : {somlrs}"
                                            f"\nHV Rockets : {sohv_rocket}"
                                            f"\nF1 Grenade : {sof1}"
                                            f"\nHE Grenade : {sohe}"))


#metal wall
@client.tree.command(name="metal_wall")
@app_commands.describe(layers = "number of metal walls")
async def metal_walls(interaction: discord.Interaction, layers:int):
    #hard side
    rocket = (layers * 8)
    c4 = (layers * 4)
    explo_ammo = (layers * 400)
    mlrs = (layers * 6)
    satchel_charge = (layers * 23)
    beancan_grenade = (layers * 112)
    hv_rocket = (layers * 67)
    f1 = (layers * 993)
    he = (layers * 57)
    #soft side
    sorocket = (layers * 8)
    soc4 = (layers * 4)
    soexplo_ammo = (layers * 399)
    somlrs = (layers * 6)
    sosatchel_charge = (layers * 23)
    sobeancan_grenade = (layers * 112)
    sohv_rocket = (layers * 67)
    sof1 = (layers * 993)
    sohe = (layers * 56)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x Metal Walls", description="\n"
                                            f"**HARD SIDE**"
                                            "\n"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"
                                            "\n"
                                            f"\n**SOFT SIDE**"
                                            f"\n"
                                            f"\nRockets : {sorocket}"
                                            f"\nTimed Explosive Charge : {soc4}"
                                            f"\nExplosive Ammo : {soexplo_ammo}"
                                            f"\nSatchel Charge : {sosatchel_charge}"
                                            f"\nBeancan Grenade : {sobeancan_grenade}"
                                            f"\nMLRS Rockets : {somlrs}"
                                            f"\nHV Rockets : {sohv_rocket}"
                                            f"\nF1 Grenade : {sof1}"
                                            f"\nHE Grenade : {sohe}"))


#Armored Wall
@client.tree.command(name="armored_wall")
@app_commands.describe(layers = "number of armored wall")
async def armored_wall(interaction: discord.Interaction, layers:int):
    #hard side
    rocket = (layers * 15)
    c4 = (layers * 8)
    explo_ammo = (layers * 799)
    mlrs = (layers * 12)
    satchel_charge = (layers * 46)
    beancan_grenade = (layers * 223)
    hv_rocket = (layers * 134)
    f1 = (layers * 1986)
    he = (layers * 114)
    #soft side
    sorocket = (layers * 15)
    soc4 = (layers * 8)
    soexplo_ammo = (layers * 798)
    somlrs = (layers * 12)
    sosatchel_charge = (layers * 46)
    sobeancan_grenade = (layers * 223)
    sohv_rocket = (layers * 134)
    sof1 = (layers * 1986)
    sohe = (layers * 111)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x Armored Wall", description="\n"
                                            f"**HARD SIDE**"
                                            "\n"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"
                                            "\n"
                                            f"\n**SOFT SIDE**"
                                            f"\n"
                                            f"\nRockets : {sorocket}"
                                            f"\nTimed Explosive Charge : {soc4}"
                                            f"\nExplosive Ammo : {soexplo_ammo}"
                                            f"\nSatchel Charge : {sosatchel_charge}"
                                            f"\nBeancan Grenade : {sobeancan_grenade}"
                                            f"\nMLRS Rockets : {somlrs}"
                                            f"\nHV Rockets : {sohv_rocket}"
                                            f"\nF1 Grenade : {sof1}"
                                            f"\nHE Grenade : {sohe}"))


#Sheet Metal Door
@client.tree.command(name="sheet_metal_door")
@app_commands.describe(layers = "number of sheet metal doors")
async def sheet_metal_door(interaction: discord.Interaction, layers:int):
    rocket = (layers * 2)
    c4 = (layers * 1)
    explo_ammo = (layers * 63)
    mlrs = (layers * 1)
    satchel_charge = (layers * 4)
    beancan_grenade = (layers * 18)
    hv_rocket = (layers * 11)
    f1 = (layers * 50)
    he = (layers * 9)
    torpedoes = (layers * 35)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x Sheet Metal Doors", description="\n"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"
                                            f"\nTorpedoes : {torpedoes}"))


#Garage Door
@client.tree.command(name="garage_door")
@app_commands.describe(layers = "number of garage doors")
async def garage_door(interaction: discord.Interaction, layers:int):
    rocket = (layers * 3)
    c4 = (layers * 2)
    explo_ammo = (layers * 150)
    mlrs = (layers * 3)
    satchel_charge = (layers * 9)
    beancan_grenade = (layers * 42)
    hv_rocket = (layers * 25)
    f1 = (layers * 120)
    he = (layers * 22)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x Garage Doors", description="\n"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"))


#Armored Door
@client.tree.command(name="armored_door")
@app_commands.describe(layers = "number of armored doors")
async def armored_door(interaction: discord.Interaction, layers:int):
    rocket = (layers * 5)
    c4 = (layers * 3)
    explo_ammo = (layers * 250)
    mlrs = (layers * 4)
    satchel_charge = (layers * 15)
    beancan_grenade = (layers * 69)
    hv_rocket = (layers * 42)
    f1 = (layers * 200)
    he = (layers * 36)
    torpedoes = (layers * 125)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x Armored Doors", description="\n"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"
                                            f"\nTorpedoes : {torpedoes}"))


#Wooden Door
@client.tree.command(name="wooden_door")
@app_commands.describe(layers = "number of wooden doors")
async def wooden_door(interaction: discord.Interaction, layers:int):
    incen_rocket = (layers * 1)
    molotov = (layers * 2)
    flame_thrower = (layers * 83)
    fire_arrow = (layers * 50)
    rocket = (layers * 1)
    c4 = (layers * 1)
    explo_ammo = (layers * 19)
    mlrs = (layers * 1)
    satchel_charge = (layers * 2)
    beancan_grenade = (layers * 6)
    hv_rocket = (layers * 4)
    f1 = (layers * 23)
    he = (layers * 3)
    torpedoes = (layers * 6)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x Wooden Doors", description="\n"
                                            f"\nIncendiary Rocket : {incen_rocket}"
                                            f"\nMolotov Cocktail : {molotov}"
                                            f"\nFlame Thrower : {flame_thrower}"
                                            f"\nFire Arrow : {fire_arrow}"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"
                                            f"\nTorpedoes : {torpedoes}"))


#High External Wooden Wall
@client.tree.command(name="high_external_wooden_wall")
@app_commands.describe(layers = "number of high external wooden walls")
async def high_external_wooden_wall(interaction: discord.Interaction, layers:int):
    incen_rocket = (layers * 1)
    molotov = (layers * 7)
    flame_thrower = (layers * 412)
    fire_arrow = (layers * 250)
    rocket = (layers * 3)
    c4 = (layers * 2)
    explo_ammo = (layers * 98)
    mlrs = (layers * 2)
    satchel_charge = (layers * 6)
    beancan_grenade = (layers * 26)
    hv_rocket = (layers * 18)
    f1 = (layers * 118)
    he = (layers * 16)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x High External Wooden Walls", description="\n"
                                            f"\nIncendiary Rocket : {incen_rocket}"
                                            f"\nMolotov Cocktail : {molotov}"
                                            f"\nFlame Thrower : {flame_thrower}"
                                            f"\nFire Arrow : {fire_arrow}"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"))


#High External Stone Wall
@client.tree.command(name="high_external_stone_wall")
@app_commands.describe(layers = "number of high external stone walls")
async def high_external_stone_wall(interaction: discord.Interaction, layers:int):
    rocket = (layers * 4)
    c4 = (layers * 2)
    explo_ammo = (layers * 185)
    mlrs = (layers * 3)
    satchel_charge = (layers * 10)
    beancan_grenade = (layers * 46)
    hv_rocket = (layers * 32)
    f1 = (layers * 182)
    he = (layers * 29)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{layers}x High External Stone Walls", description="\n"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nF1 Grenade : {f1}"
                                            f"\nHE Grenade : {he}"))


#Vehicle----------------------------------------------------------------------------------------------------------------


#Bradley APC
@client.tree.command(name="bradley_apc")
@app_commands.describe(number = "number of bradley APC")
async def bradley_apc(interaction: discord.Interaction, number:int):
    rocket = (number * 11)
    c4 = (number * 3)
    explo_ammo = (number * 571)
    mlrs = (number * 7)
    satchel_charge = (number * 20)
    beancan_grenade = (number * 191)
    hv_rocket = (number * 7)
    f1 = (number * 40)
    he = (number * 82)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{number}x Bradley APC", description="\n"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nF1 Grenade : {f1}"                                                                                                            
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHE Grenade : {he}"))


#TugBoat
@client.tree.command(name="tugboat")
@app_commands.describe(number = "number of tugboats")
async def tugboat(interaction: discord.Interaction, number:int):
    rocket = (number * 16)
    c4 = (number * 4)
    explo_ammo = (number * 769)
    mlrs = (number * 10)
    satchel_charge = (number * 27)
    beancan_grenade = (number * 261)
    hv_rocket = (number * 11)
    f1 = (number * 68)
    he = (number * 120)
    torpedoes = (number * 12)
    await interaction.response.send_message(embed = discord.Embed(colour=discord.Color.red(), title=f"{number}x Tugboats", description="\n"
                                            f"\nTorpedoes : {torpedoes}"
                                            f"\nHV Rockets : {hv_rocket}"
                                            f"\nRocket : {rocket}"
                                            f"\nTimed Explosive Charge : {c4}"
                                            f"\nExplosive Ammo : {explo_ammo}"
                                            f"\nF1 Grenade : {f1}"                                                                                                            
                                            f"\nSatchel Charge : {satchel_charge}"
                                            f"\nBeancan Grenade : {beancan_grenade}"
                                            f"\nMLRS Rockets : {mlrs}"
                                            f"\nHE Grenade : {he}"))


client.run("TOKEN")

