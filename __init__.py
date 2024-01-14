from .nodes.RF_Tutorial import *


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique (including other modules, this is why you might see error messages in the Manage)
NODE_CLASS_MAPPINGS = {
    "RF_Tutorial": RF_Tutorial,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "RF_Tutorial": "A custom name to display in th UI",
    "Example": "Example"
}