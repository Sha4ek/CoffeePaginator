import disnake

class Paginator(disnake.ui.View):
    def __init__(self, message: disnake.Message, embeds: list):
        self.message = message
        self.embeds = embeds
        self.page = 0

        super().__init__(timeout=30)

    @disnake.ui.button(style=disnake.ButtonStyle.primary, emoji='⬅️')
    async def button_left(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if self.page == 0:
            self.page = len(self.embeds) - 1
        else:
            self.page -= 1

        await self.button_callback(interaction)

    @disnake.ui.button(style=disnake.ButtonStyle.primary, emoji='➡️')
    async def button_right(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if self.page == len(self.embeds) - 1:
            self.page = 0
        else:
            self.page += 1

        await self.button_callback(interaction)

    async def start(self):
        await self.message.edit(embed=self.embeds[self.page], view=Paginator(self.message, self.embeds))

    async def button_callback(self, interaction: disnake.Interaction):
        await interaction.response.edit_message(embed=self.embeds[self.page])