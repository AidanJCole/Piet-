from PIL import Image


# Piet++ often travers stacks of stacks. This function returns the stack at a given depth.
def getStack(stack, depth):
    temp = stack
    for x in range(depth):
        if len(temp) > 0 and isinstance(temp[-1], list):
            temp = temp[-1]
        else:
            return

    return temp

# Function to determine maximum depth of recursive stacks.
def getDepth(stack):
    depth = 0
    temp = stack
    while len(temp) > 0 and isinstance(temp[-1], list):
        depth+=1
        temp = temp[-1]

    return depth