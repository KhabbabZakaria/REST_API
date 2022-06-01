import requests
 
#########################GET##################################
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

x = response.json()
print(x)


#########################POST##################################
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
x = response.json()
print(x)



#########################PUT##################################
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
x = response.json()
print(x)

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
x = response.json()
print(x)


#########################PATCH##################################
api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
x = response.json()
print(x)




#########################DELETE##################################
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
x = response.json()
print(x)