# CoffeePaginator
Простой модуль для создания страниц на [Disnake](https://github.com/EQUENOS/disnake)

### Поддержка
[Sha4ek#3306](https://discord.com/users/546502974499717122)

### Установка
```py
pip install CoffeePaginator
```

### Параметры

| Название | Тип | По умолчанию | Описание |
|:-:|:-:|:-:|:-:|
| message | `discord.Message` | | Сообщение для страниц |
| embeds | `list` | | Список эмбедов |
| author | `discord.abc.User` | | Автор команды (`ctx.author`) |
| footer | `bool` | `False` | Включить или же отключить [Footer](https://disnake.readthedocs.io/en/latest/api.html?#disnake.Embed.footer) с номером страниц |
| timeout | `int` | `30` | Время для управления кнопками, в секундах |

### Пример использования

**1.** Без показа номера страниц

```py
import disnake
from disnake.ext import commands
from CoffeePaginator import Paginator

Bot = commands.Bot(command_prefix='^')

@Bot.command()
async def test(ctx):
    emb1 = disnake.Embed(title='1 страница')
    emb2 = disnake.Embed(title='2 страница')
    emb3 = disnake.Embed(title='3 страница')
    emb4 = disnake.Embed(title='4 страница')
    
    embs = [emb1, emb2, emb3, emb4]
    message = await ctx.send(embed=emb1)
    
    pages = Paginator(message, embs, ctx.author)
    await pages.start()

Bot.run('токен')
```

**2.** С показом номера страниц

```py
import disnake
from disnake.ext import commands
from CoffeePaginator import Paginator

Bot = commands.Bot(command_prefix='^')

@Bot.command()
async def test(ctx):
    emb1 = disnake.Embed(title='1 страница')
    emb2 = disnake.Embed(title='2 страница')
    emb3 = disnake.Embed(title='3 страница')
    emb4 = disnake.Embed(title='4 страница')
    
    embs = [emb1, emb2, emb3, emb4]
    message = await ctx.send(embed=emb1)
    
    pages = Paginator(message, embs, ctx.author, footer=True)
    await pages.start()

Bot.run('токен')
```
