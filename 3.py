users = ['Admin', 'Guest', 'User', 'Bot']
print(f"ервоначальный список: {users}")

users[0] = 'Moderator'
users[-1] = 'SuperAdmin'
users.append('Newbie')

print(f"Изменённый список: {users}")
