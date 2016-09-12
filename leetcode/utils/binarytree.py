# coding=utf-8
# Definition for a binary tree node.


class TreeNode:
    """
    OJ's Binary Tree Serialization:
    The serialization of a binary tree follows a level order traversal,
    where '#' signifies a path terminator where no node exists below.

    Here's an example:
       1
      / \
     2   3
        /
       4
        \
         5
    The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.val)

    @staticmethod
    def build(seq):
        """
        从列表形成一个二叉树，此节点作为根节点
        列表构造实际上是一颗满二叉树
        :param seq: binary tree serialization
        :return: tree root node
        """
        if not seq:
            return None

        root = TreeNode(seq[0])
        Q = [root]  # 初始化根节点
        for i in range(2, len(seq), 2):  # 步长是2
            node = Q.pop(0)

            if seq[i-1] != '#':
                node.left = TreeNode(seq[i-1])
                Q.append(node.left)

            if seq[i] != '#':
                node.right = TreeNode(seq[i])
                Q.append(node.right)
        return root

    def __str__(self):
        """
        书结构转为字符串表示法
        :return: 字符串表示书结构
        """
        val = []

        Q = [self]  # 当前节点作为根节点构造序列
        while Q:
            q = Q  # 当前处理序列
            Q = []  # 新的待处理队列
            for i in q:
                if i:
                    val.append(i.val)

                    Q.append(i.left)
                    Q.append(i.right)
                else:
                    val.append('#')

        while val[-1] == '#':
            val.pop()  # 删除末尾的结束符

        return str(val)

    def copy(self):
        """
        复制二叉树，从当前节点开始复制
        :return:
        """

    def __reversed__(self):
        """
        二叉树逆序
        :return: 当前节点
        """

    def preorder(self, node=None, seq=None):
        """
        前序遍历
        :param node: 当前树节点
        :param seq: 存储遍历后的结果
        :return: seq
        """
        if seq is None:  # seq为空是作为入口初始化node
            node = self
            seq = []

        if node:  # 非空
            seq.append(node.val)
            self.preorder(node.left, seq)
            self.preorder(node.right, seq)
        return seq

    def inorder(self, node=None, seq=None):
        """
        中序遍历
        :param node: 当前树节点
        :param seq: 存储遍历后的结果
        :return: seq
        """
        if seq is None:  # seq为空是作为入口初始化node
            node = self
            seq = []

        if node:  # 非空
            self.inorder(node.left, seq)
            seq.append(node.val)
            self.inorder(node.right, seq)
        return seq

    def postorder(self, node=None, seq=None):
        """
        后序遍历
        :param node: 当前树节点
        :param seq: 存储遍历后的结果
        :return: seq
        """
        if seq is None:  # seq为空是作为入口初始化node
            node = self
            seq = []

        if node:  # 非空
            self.postorder(node.left, seq)
            self.postorder(node.right, seq)
            seq.append(node.val)
        return seq


if __name__ == '__main__':
    root = TreeNode.build([1, 2, 3, '#', '#', 4, '#', '#', 5])
    print root

    root = TreeNode.build('1234567')
    print root
    print root.preorder()
    print root.inorder()
    print root.postorder()
