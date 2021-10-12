import asyncio
import aiohttp
from asyncio.queues import Queue
import datetime
inicio = datetime.datetime.now()

async def gestor(url:str, queue: asyncio.Queue):
    print("Adicionado a fila")
    await queue.put(url)

async def processar_dados(queue: asyncio.Queue):
     print(".... processando")
     rest = await queue.get()
     async with aiohttp.ClientSession() as start:
            async with start.get(rest) as resp:
                conteudo = await resp.json()
                for elem in conteudo:
                    print("%s    %s "%(elem['name'],elem['totalCases']))

     #   await asyncio.sleep(2)
     print(".... processado!!!")

    
   


async def main():
    url_api=["https://exchange.vcoud.com/coronavirus/latest"]
    queue = asyncio.Queue()
    for endreco in url_api:
        await gestor(endreco, queue)
        await processar_dados(queue)

if __name__ == "__main__":
    queue = asyncio.Queue()
    el = asyncio.get_event_loop()
    el.run_until_complete(main())
    el.close()

tempo_atual = datetime.datetime.now() - inicio
print(f'Tempo de duração foi de {tempo_atual.total_seconds():.5f} segundos')
