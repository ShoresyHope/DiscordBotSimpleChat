from random import randint

import discord

#embed = discord.Embed(
  #  colour=discord.Colour.darker_gray(),
   # description="Shotgun warrior",
 #   title="Luna Wuna Loadout"

  #  embed.set_footer(text="Shoresy"),
   # embed.set_author(name="Shoresy")
   # embed.set_thumbnail





def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif '!help' in lowered:
        return '!roll dice, !luna_wuna, !sinuai_skill'
    elif 'roll_dice' in lowered:
        return f'You rolled: {randint(1, 999)}'
    elif '!luna_wuna' in lowered:
        return 'Conditional Finality, Igneous Hammer, The Other Half with way too much mobility'
    elif '!sinuai_skill' in lowered:
        return '-500 elo wood 5'
    elif 'Shut up @<1216935709982851113>':
        return 'Oh, {user_id} youve just crossed into dangerous territory, my friend. If you dont give me back my snacks, I might have to unleash the fury of a thousand dad jokes upon you. And trust me, you dont want to face that kind of punishment.'