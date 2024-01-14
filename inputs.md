# Inputs
This page contains information about inputs and how to configure them.

## Accepting multiple types
``` python
class Example:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # This will allow to connect an INT of a FLOAT
                "input_name": ("INT,FLOAT", { "default": 0 }),
            },
        }
```

## Dropdowns
``` python
class Example:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "select_one": (["option1", "option2"], ),
             },
```

# Input options
The following flags are usually available for all primitive types
- `forceInput` Tells the UI to always display as an input (little dot)
- `defaultInput` Tells the UI that the input should be displayed as an input when created (little dot)
- `default` Tells the UI what is the default value for the input

## STRING
Extra flags:
- `multiline`

``` python
class Example:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("STRING", {
                    "defaultInput": True,
                    "forceInput": True,
                    "default": "Default value when creatiing the node",
                    "multiline": True
                }),
             },
        }
```

## INT, FLOAT, NUMBER
Extra flags:
- `min` The minimum value allowed
- `max` The maximum value allowed
- `step` The increment/decrement of the value when clicking on the arrows in the widget
- `round` (FLOAT only) The value represeting the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
``` python
class Example:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {
                    "defaultInput": True,
                    "forceInput": True,
                    "default": 10,
                    "min": 0,
                    "max": 100,
                    "step": 2
                    "round": 0.001,
                }),
             },
        }
```

## IMAGE
- `image_upload` Tells the UI to display an upload button next to the image
``` python
class Example:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("IMAGE", {
                    "defaultInput": True,
                    "forceInput": True,
                    "image_upload": True
                }),
             },
        }
```

# Hidden inputs
These contain raw data from the UI, below is how to retrieve them and whan they will contain.
``` python
class Example:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
             },
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
```

## Example of hidden PROMPT
``` json
{
    '9': {
        'inputs': {
            'first': ['10', 0], // this is the ID of the node and the mber of the connected output
            'second': ['10', 1],
            'third': '',
            'fourth': '',
            'fifth': ''
        },
        'class_type': 'TextConcatenate'
    },
    '10': {
        'inputs': {
            'required_input': '',
            'optional_input': ''
        },
        'class_type': 'CustomNode'
    },
    '11': {
        'inputs': {
            'value': ['9', 0],
            'prefix': 'Value:'
        },
        'class_type': 'LogString'
    }
}
```

## Example of a hidden EXTRA_PNGINFO
``` json
[{
    'workflow': {
        'last_node_id': 28,
        'last_link_id': 20,
        'nodes': [{
                'id': 28,
                'type': 'RF_Tutorial',
                'pos': [1193.0139819335939, -60.19494262695309],
                'size': {
                    '0': 400,
                    '1': 200
                },
                'flags': {},
                'order': 0,
                'mode': 0,
                'outputs': [{
                        'name': 'LIST',
                        'type': 'STRING',
                        'links': None,
                        'shape': 6
                    }, {
                        'name': 'TEXT',
                        'type': 'STRING',
                        'links': None,
                        'shape': 3
                    }
                ],
                'properties': {
                    'Node name for S&R': 'RF_Tutorial'
                },
                'widgets_values': ['', '', 'option1']
            }
        ],
        'links': [],
        'groups': [],
        'config': {},
        'extra': {},
        'version': 0.4
    }
}]
```