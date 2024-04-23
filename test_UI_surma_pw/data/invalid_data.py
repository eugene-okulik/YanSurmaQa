from generator.generator import generated_user

user = next(generated_user())

empty_fields = [
    ['',
     user.last_name,
     user.email,
     user.password,
     user.confirm_password],
    [user.first_name,
     '',
     user.email,
     user.password,
     user.confirm_password],
    [user.first_name,
     user.last_name,
     '',
     user.password,
     user.confirm_password],
    [user.first_name,
     user.last_name,
     user.email,
     '',
     user.confirm_password],
    [user.first_name,
     user.last_name,
     user.email,
     user.password,
     ''],
]

not_equal_passwords = [
    [user.first_name,
     user.last_name,
     user.email,
     'notequal_pa$$sw',
     user.confirm_password],
    [user.first_name,
     user.last_name,
     user.email,
     user.password,
     'user.confirm_password']
]
