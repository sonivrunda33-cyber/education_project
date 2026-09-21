class User:
    def __init__(self, id, name, email, role="student"):
        self.id = id
        self.name = name
        self.email = email
        self.role = role

    def is_admin(self):
        return self.role == "admin"

    def is_student(self):
        return self.role == "student"