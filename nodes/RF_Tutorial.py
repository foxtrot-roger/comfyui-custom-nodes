import time

# Below is my notes as I was investigating the behaviour of custom nodes, it can serve as a good base for anything and see what is doing what.
# The node in itself only prints some stuff in the console of the server.

# NOTE: To make it available in the UI, we will need to add things in __init__.py
class RF_Tutorial:
    
    # Use this method to tell the UI what inputs are expected by the node
    @classmethod
    def INPUT_TYPES(cls):
        return {
            # required: These are the required inputs, the UI will show an error if they are not filled or connected
            # NOTE: This MUST be defined in the return
            "required": {
                "required_input": ("STRING", { "default": "", "multiline": True }),
             },

            # optional: These are the optional inputs, no check will be done on them by the UI
            "optional": {
                "optional_input": ("STRING", { "default": "", "multiline": True }),
                
                # NOTE: don't forget the coma after the array of options or it will not work
                "optional_oneof": (["option1", "option2"], ),
            },

            # hidden: These input contain raw data from the UI and are not displayed in the UI
            # NOTE: You'll probably never need to use these, they are here for completion
            "hidden": {
                # A unique ID for the prompt
                "hidden_uniqueid": ("UNIQUE_ID"),

                # an object containing the nodes of the prompts and their values
                "hidden_prompt": ("PROMPT"),
                
                # contains what will be saved to a file when pressing save 
                # (probably also what is sent to the server to execute a prompt)
                # NOTE: for some reason, this one is ignored in the VALIDATE_INPUTS
                "hidden_pnginfo": ("EXTRA_PNGINFO"),
            },
        }

    # Use this to tell the UI to provide you ALL inputs in lists
    # This can be used to process the get the whole list of output with OUTPUT_IS_LIST instead of one at a time (see below)
    INPUT_IS_LIST = True

    # Implement this method to perform custom validation of the inputs.
    # - The parameters must match the names from INPUT_TYPES
    # - The parameters order do not need to match the order of INPUT_TYPES
    # - Thep parameters of type EXTRA_PNGINFO cannot be validated and will produce an error
    # - Return `True` to indicate success, anything else will be forwarded to the UI as an error for the node
    # - It is not possible to define multiple VALIDATE_INPUTS methods, if you do, only the last one will be used and the others will be ignored
    # - The error message will be the same for all inputs (bug?)
    @classmethod
    def VALIDATE_INPUTS(cls, required_input, optional_input, optional_oneof, hidden_prompt, hidden_uniqueid):
        return True

    # Use this method to tell the UI that a value has changed
    # You only need this if you want to reevaluate the node based on something that is not in the UI
    # NOTE:
    # - The name is misleading, you need to return a value DIFFERENT from the last one to tell the UI to refresh
    #   (this can be achieved by returning the current time, ...)
    # - do not include inputs of type EXTRA_PNGINFO as they will not be mapped and create an error
    @classmethod
    def IS_CHANGED(cls, required_input, optional_input, optional_oneof, hidden_prompt,  hidden_uniqueid):
        LogToConsole("IS_CHANGED", "IS_CHANGED")
        return time.time()

    # The UI will create a menu that matches this path to let the user create the node
    CATEGORY = "path/to/node"

    # The names of the outputs of this node
    RETURN_NAMES = ("LIST","TEXT")
    # The "types" of the outputs of this node
    # NOTE: These are not validated by the UI, they are only used to know what can connect to what
    RETURN_TYPES = ("STRING", "STRING")
    # Use this to indicate which outputs are lists
    # When True, return a list in the processing, the output will be processed once per item
    # in this example, if we connect LIST to another node, it will run once per item in LIST
    OUTPUT_IS_LIST = (True, False)

    # It tells the UI that this node is a final output
    # NOTE: At least one node in the whole prompt must have this flag otherwise the UI will show an error
    OUTPUT_NODE = True

    # Which method is called for processing
    FUNCTION = "NodeProcess"
    # Use this method to process inputs and produce output
    # All the parameters names must match the names in INPUT_TYPES but the order can change
    # NOTE: The name must match the value in FUNCTION
    # NOTE: When returning only one value, make sure that you either return (value, ) or return value,
    def NodeProcess(self, required_input, optional_input, optional_oneof, hidden_prompt, hidden_pnginfo, hidden_uniqueid):
        LogToConsole("required_input", required_input)
        LogToConsole("optional_input", optional_input)
        LogToConsole("optional_oneof", optional_oneof)
        LogToConsole("hidden_prompt", hidden_prompt)
        LogToConsole("hidden_pnginfo", hidden_pnginfo)
        LogToConsole("hidden_uniqueid", hidden_uniqueid)

        return (["john", "smith"], "text",)

# Ignore this method, it is only used to display text in color in the console of the server
def LogToConsole(prefix, value):
    print(f"\033[96m{prefix}: {value}\033[0m\n")
