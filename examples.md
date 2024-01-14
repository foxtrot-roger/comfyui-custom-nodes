# Examples
Below are a few examples that can be used as base for nodes

## Minimal custom node
This example contains only the minimum needed to make a node
``` python
class Example:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # customize this
                "required_input": ("STRING", { "default": "", "multiline": True }),
             },
            "optional": {
                # customize this
            },
        }

    # customize this
    CATEGORY = "path/to/node"
    
    # customize this
    RETURN_NAMES = ("name",)
    RETURN_TYPES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, required_input):
        # customize this
        # when returning a single value, make sure to end with a come eg. (value,)
        return ("John Smith", )

NODE_CLASS_MAPPINGS = {
    "Example": Example,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example": "The name of the node in the UI",
}
```

## All options
This example contains all options, just remove what you don't need
``` python
class Example:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "required_input": ("STRING", { "default": "", "multiline": True }),
             },
            "optional": {
            },
        }

    # Keep this only if you process lists manually
    INPUT_IS_LIST = True

    # Keep this only if you need to validate input
    @classmethod
    def VALIDATE_INPUTS(cls, required_input):
        return True

    # Keep this only if the output can change with outside of the UI
    @classmethod
    def IS_CHANGED(cls, required_input):
        return time.time()

    CATEGORY = "path/to/node"

    RETURN_NAMES = ("LIST","TEXT")
    RETURN_TYPES = ("STRING", "STRING")

    # Keep this only if outputs can be lists (and update to match the order of the outputs)
    OUTPUT_IS_LIST = (True, False)

    # Keep this only if the node should allow a prompt to be queued
    OUTPUT_NODE = True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, required_input):
        # when returning a single value, make sure to end with a come eg. (value,)
        return (["john", "smith"], "text",)
```