"""
seed.py
"""
import model

db = model.connect_db()
user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian")
task = model.new_task(db, "Complete this task list", user_id)
user_id = model.new_user(db, "findme@meganspeir.com", "securepassword", "Megan")
task = model.new_task(db, "Put together camping supplies", user_id)
user_id = model.new_user(db, "me@brianspeir.com", "thisisapassword", "Brian")
task = model.new_task(db, "Subscribe to city car service", user_id)
task = model.new_task(db, "Reserve a vehicle", user_id)
task = model.new_task(db, "Reserve a camping space", user_id)
task = model.new_task(db, "Confirm number of guest", user_id)
task = model.new_task(db, "Print directions to Big Sur", user_id)
