import time
import asyncio
from g4f.client import Client


async def main():
    start = time.time()
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Привет"}],
        # Add any other necessary parameters
    )
    end = time.time()
    print(response.choices[0].message.content)
    print(f"Время: {end - start} секунд")

asyncio.run(main())
