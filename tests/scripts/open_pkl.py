import pickle

with open("../data/test_tasks/prepare_meal/controller_action_list.pkl", "rb") as f:
    data = pickle.load(f)

print(data)