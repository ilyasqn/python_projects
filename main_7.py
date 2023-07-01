class Project:
	def __init__(self, name, tasks):
		if isinstance(name, str) and isinstance(tasks, list):
			self.name = name
			self.tasks = tasks
		else:
			raise TypeError("Неверный тип данных")
		
	def get_project(self):
		return self.name, self.tasks
	def get_info(self):
		return task.condition
		

class Task():
	def __init__(self):
		self.condition = []
		
	def check_name(self, name):
		for dict in self.condition:
			if name in dict.values():
				raise TypeError("Вы пытаетесь добавить существующую задачу")
			
	def check_list(self, name):
		if name not in project.tasks:
			project.tasks.append(name)
		
	def add_task(self, name, executor, status):
		if isinstance(name, str) and isinstance(executor, str) and isinstance(status, str):
			self.check_name(name)
			self.check_list(name)
			self.new_task = {
				"Название задачи": name,
				"Исполнитель": executor,
				"Статус": status
			}
			self.condition.append(self.new_task)
		else:
			raise TypeError("Не может быть использованы числа")
		
	def change_status(self, name, new_status):
		for dict in self.condition:
			if name in dict.values():
				if dict['Статус'] != new_status:
					dict['Статус'] = new_status
					print("Статус успешно изменен")
					break
				else:
					raise TypeError("Вы не изменили статус")
				
				
	def change_exec(self, name, new_exec):
		for dict in self.condition:
			if name in dict.values():
				if dict['Исполнитель'] != new_exec:
					dict['Исполнитель'] = new_exec
					print("Исполнитель успешно изменен")
					break
				else:
					raise TypeError("Вы не изменили исполнителя")
				

project = Project('Company', ['1', '2', '12'])


task = Task()
task.add_task('10', 'Iliyas', 'process')
task.add_task('12', 'Iliyas', 'in process')


task.change_status('10', 'done')
task.change_exec('10', 'Aknazar')
task.change_status('12', 'almost done')


print(project.get_project())
print(project.get_info())


