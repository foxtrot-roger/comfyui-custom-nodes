# Disable string interpretation on multiline text
ComfyUI text support an random string injection, any text input in the form of {a|b} will rendomly be replaced by either a or b when running the prompt.

See [dynamicPrompts](https://github.com/comfyanonymous/ComfyUI/blob/master/web/extensions/core/dynamicPrompts.js)

To disable that, delete the file *.\\web\\extensions\\core\\dynamicPrompts.js*