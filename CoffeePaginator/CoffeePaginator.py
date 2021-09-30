import disnake


class Paginator(disnake.ui.View):
    def __init__(
            self,
            message: disnake.Message,
            embeds: list,
            author: disnake.abc.User,
            footer: bool = False,
            timeout: int = 30
        ):
        self.message = message
        self.embeds = embeds
        self.author = author
        self.footer = footer
        self.timeout = timeout
        self.page = 0

        super().__init__(timeout=self.timeout)

        if self.footer == True:
            for emb in self.embeds:
                emb.set_footer(text=f'Страница: {self.embeds.index(emb) + 1}/{len(self.embeds)}')


    @disnake.ui.button(style=disnake.ButtonStyle.secondary, emoji='⬅️')
    async def button_left(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if self.author.id == interaction.author.id:
            if self.page == 0:
                self.page = len(self.embeds) - 1
            else:
                self.page -= 1
        else:
            return

        await self.button_callback(interaction)


    @disnake.ui.button(style=disnake.ButtonStyle.secondary, emoji='➡️')
    async def button_right(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if self.author.id == interaction.author.id:
            if self.page == len(self.embeds) - 1:
                self.page = 0
            else:
                self.page += 1
        else:
            return

        await self.button_callback(interaction)


    async def start(self):
        await self.message.edit(embed=self.embeds[self.page], view=Paginator(self.message, self.embeds, self.author))


    async def button_callback(self, interaction: disnake.Interaction):
        if self.author.id == interaction.author.id:
            await interaction.response.edit_message(embed=self.embeds[self.page])
        else:
            return
