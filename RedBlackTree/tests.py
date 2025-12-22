from redblacktree import RedBlackTree

# ---------------- TEST ----------------
if __name__ == "__main__":
    rbt = RedBlackTree()
    values = [20, 15, 25, 10, 5, 1, 30, 28]

    for v in values:
        rbt.insert(v)

    print("Inorder after insert:")
    rbt.inorder(rbt.root)

    rbt.delete(10)
    print("\nInorder after delete 10:")
    rbt.inorder(rbt.root)