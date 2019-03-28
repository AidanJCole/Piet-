from PIL import Image



def getStack(stack, depth):
    temp = stack
    for x in range(depth):
        if isinstance(temp[0], list):
            temp = temp[0]
        else:
            return

    return temp