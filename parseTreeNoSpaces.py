from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    currentNumber = ''
    fplist = []
    for token in fpexp:
        if(token not in ['(','+', '-', '*', '/',')']):
            currentNumber = currentNumber + token
        if token == '(':
            fplist.append(token)
        if token in ['(','+', '-', '*', '/',')']:
            if(currentNumber != ''):
                fplist.append(currentNumber)
                currentNumber = ''
                fplist.append(token)
            if token == '/' or token == '*':
                fplist.append(token)
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            if i != '':
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("((10+5)*3)")
pt.postorder()  #defined and explained in the next section