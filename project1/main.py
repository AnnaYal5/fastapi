import asyncio
import httpx


async def get_todos(client):
    return await client.get('https://jsonplaceholder.typicode.com/todos').json()


# add error handling
# for example:
# async def get_todos_json(сlient) -> list:
#    response = await client.get("https://jsonplaceholder.typicode.com/todos")
#    if response.status_code != 200:
#       return [False, response.status_code]
#    return [True, response.json()]

async def get_user_info(client, user_id):
    return await client.get(f'https://jsonplaceholder.typicode.com/users/{user_id}').json()


async def main():
    async with httpx.AsyncClient() as client:
        todos = await get_todos(client)

        user_task_count = {}
        user_completed_count = {}

        for todo in todos:
            user_id = todo['userId']
            if user_id not in user_task_count:
                user_task_count[user_id] = 0
            if user_id not in user_completed_count:
                user_completed_count[user_id] = 0

            user_task_count[user_id] += 1
            if todo['completed'] is True:  # Михайло: if todo['completed'] is True: ++
                user_completed_count[user_id] += 1

        user_reports = []

        async def report_user(user_id):  # Михайло: Я не впевнений, але я не бачив функцію в функції
            user_info = await get_user_info(client, user_id)
            name = user_info['name']
            total_tasks = user_task_count.get(user_id)
            completed_tasks = user_completed_count.get(user_id)
            incomplete_tasks = total_tasks - completed_tasks
            completed_percentage = (completed_tasks / total_tasks * 100)

            user_reports.append({
                "name": name,
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks,
                "incomplete_tasks": incomplete_tasks,
                "completed_percentage": completed_percentage,
            })

        tasks = [report_user(user_id) for user_id in user_task_count.keys()]
        await asyncio.gather(*tasks)

        for report in user_reports:
            print(f"Користувач: {report['name']}")
            print(f"Загальна кількість завдань: {report['total_tasks']}")
            print(f"Кількість виконаних завдань: {report['completed_tasks']}")
            print(f"Кількість невиконаних завдань: {report['incomplete_tasks']}")
            print(f"Відсоток виконаних завдань: {report['completed_percentage']}%")
            print("------------------------------------")


asyncio.run(main())
