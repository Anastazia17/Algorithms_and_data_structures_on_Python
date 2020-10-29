"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

class BinaryTree:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Функция для вставки потомков:

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Функция для сравнения значения с узлами:

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" не найдено!"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" не найдено!"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + " найдено.")

# Функция для вывода дерева:

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = BinaryTree(12)
root.insert(6)
print(root.left.PrintTree())
print(root.left.findval)
root.insert(14)
root.insert(3)
print(root.right.PrintTree())
print(root.right.findval)
print(root.findval(7))
print(root.findval(29))
print(root.findval(14))


# Результат:
# 6
# None
# <bound method BinaryTree.findval of <__main__.BinaryTree object at 0x00000212D76462B0>>
# 14
# None
# <bound method BinaryTree.findval of <__main__.BinaryTree object at 0x00000212D7646670>>
# 7 не найдено!
# 29 не найдено!
# 14 найдено.
# None