from ai2thor.controller import Controller
from generate_test_task_data import generate_prepare_meal_data

OBJECT_TYPES = ["Apple", "Bowl", "Bread", "ButterKnife", "Cabinet", "CoffeeMachine", "CounterTop", "Cup", "DishSponge", "Egg", "Faucet", "Floor", "Fork", "Fridge", "GarbageCan",
                "Knife", "Lettuce", "LightSwitch", "Microwave", "Mug", "Pan", "PepperShaker", "Plate", "Pot", "Potato", "SaltShaker", "Sink", "SinkBasin", "SoapBottle",
                "Spatula", "Spoon", "StoveBurner", "StoveKnob", "Toaster", "Tomato"]

def main():

    for i in range(1, 2):

        controller = Controller(scene=f"FloorPlan{i}")
        
        # for obj in controller.last_event.metadata["objects"]:
        #     if obj["pickupable"]:
        #         print(obj["objectType"])
        # print()
        print(controller.last_event.metadata.get('inventoryObjects'))
        # print(controller.last_event.metadata["objects"])

        generate_prepare_meal_data(controller)

main()