from PIL import Image
import copy

stack = []
stackStack = [stack]
depth = 0

def isStack(u):
    return isinstance(u, list)

def pushInt(stack, value):
    stack.append(value)

def pushStack(stack):
    stack.append([])

def pop(stack):
    if len(stack) > 0:
        return stack.pop()

def dup(stack):
    stack.append(copy.deepcopy(stack[-1]))

def roll(x, y, stack):
    return 0

def rolc(x,y,stackStack):
    return 0

def pushUp(stackStack):
    if len(stackStack) >= 2 and len(stackStack[-1]) > 0:
        current = stackStack[-1]
        stackStack[-2].append(pop(current))

def pushDown(stackStack):
    if len(stackStack[-1]) >= 2 and isStack(stackStack[-1][-2]):
        temp = stackStack[-1][-2]
        temp.append(pop(stackStack[-1]))

def pullUp(stackStack):
    if len(stackStack[-1]) >= 1 and isStack(stackStack[-1][-1]):
        stackStack[-1].append(pop(stackStack[-1][-1]))

def up(stackStack):
    if len(stackStack) > 1:
        pop(stackStack)

def down(stackStack):
    if isStack(stackStack[-1][-1]):
        stackStack.append(stackStack[-1][-1])

