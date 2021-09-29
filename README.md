# CoffeePaginator
Простой модуль для создания страниц на [Disnake](https://github.com/EQUENOS/disnake)

## Особая благодарность
[Одинокий Кустик#5555](https://discord.com/users/289779709292838913) - исправление ошибки, которая не меняла страницы


## Установка
```py
pip install CoffeePaginator
```

## Параметры
|           Имя             |                     Тип                     |                           Информация                                |
|:-------------------------:|:-------------------------------------------:|:-------------------------------------------------------------------:|
|         message           |              `discord.Message`              |       Ваше сообщение для страниц        |
|          embeds           |                    `list`                   |                        Список эмбедов                              |

## Пример использования

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
    
    pages = Paginator(message, embs)
    await pages.start()
    
Bot.run('токен')
```
