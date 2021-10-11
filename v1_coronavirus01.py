import asyncio
import aiohttp
import datetime
#https://docs.aiohttp.org/en/stable/whats_new_3_0.html#aiohttp-whats-new-3-0
url = "https://exchange.vcoud.com/coronavirus/latest"

inicio = datetime.datetime.now()
import queue
async def main(url):
    async with aiohttp.ClientSession() as start:
            async with start.get(url) as resp:
                conteudo = await resp.json()
                for elem in conteudo:
                    print("%s    %s "%(elem['name'],elem['totalCases']))


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(url))
  
  

tempo_atual = datetime.datetime.now() - inicio
print(f'Tempo de duração foi de {tempo_atual.total_seconds():.5f} segundos')


#https://rickandmortyapi.com/