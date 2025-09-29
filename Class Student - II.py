class student:
	grade = 12
	name = "codingal"
	
	def introduction(self):
		print("Hello  I am a student")

	def details(self):
		print("My name is", self.name)
		print("I am in Grade", self.grade)

ob = student()
ob.introduction()
ob.details()
