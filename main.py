import operator 

class Tree:

  def __init__(self, data, left=None, right = None):
    self.data = data
    self.left = left
    self.right = right   
    self.ops = {
      '+' : operator.add,
      '-' : operator.sub,
      '*' : operator.mul,
      '/' : operator.truediv, 
      '**' : operator.xor,
    }
    self.priority = {
      '+': 0,
      '-': 0,
      '*': 1,
      '/': 1,
      '**':2,
    }

  def get_height(self):

    height = 0
    if self.left:
      height = self.left
    if self.right and self.right.get_height() > height:
      height.right.get_height()
    
    return height

  def get_leaves(self):

    if self.left == None and self.right == None: 
      return [self.data]

    left_leaves = []
    right_leaves = []
    if self.left:
      left_leaves = self.left.get_leaves()

    if self.right: 
      right_leaves = self.right.get_leaves()

    return left_leaves + right_leaves

  def evaluate(self):
    if type(self.data) == int:
      return self.data
    elif self.data in self.ops:
      if (type(self.right) == Tree) and (type(self.left) == int):
        return self.ops[self.data](self.left,self.right.evaluate())
      elif (type(self.right) == int) and (type(self.left) == Tree):
        return self.ops[self.data](self.left.evaluate(),self.right)
      else:
        return self.ops[self.data](self.left,self.right)
      

  def unwrap_list(self,li):
    for element in li:
      if type(element) is list:
        index = li.index(element)
        for i in range(len(element)):
          li.insert(index, element.pop())
        li.remove([])
    return li


def printTree(tree):
  try:
    if str(tree.data).startswith("<__main"):
      return printTree(tree.data)
    if tree.left:
      printTree(tree.left)
    if tree.right:
      printTree(tree.right)
    print(tree.data)
  except AttributeError:
    print(tree)


rpl = [1,2,'+',3,'*']

def rpl_tree(exp):
  s = []
  for element in exp:
    if type(element) == int:
      s.append(element)
    else:
      a = s.pop()
      b = s.pop()
      t = Tree(element, a, b)
      s.append(t)
  return s.pop()

exptree = rpl_tree(rpl)
printTree(exptree)
equation = Tree('+', 2, Tree('*',3,4))
print(equation.evaluate())

def get_tree_height(tree):
  if not tree: 
    return -1

  return max(get_tree_height(tree.left), get_tree_height(tree.right))+1
#Tree(node, child,child,...)
t = Tree('C',Tree('A'), Tree ('B'))
s = Tree ('D', Tree('E'), t)

expression = Tree('*',1,Tree('+',2,3))


