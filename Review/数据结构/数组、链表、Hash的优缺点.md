### 数组、链表、Hash、二叉树的优缺点

1、数组是将元素连续存储在内存中，链表中的元素在内存中不是顺序存储的，而是通过存在元素中的指针联系到一起

2、数组必须实现定义固定的长度，不能适应数据动态增减的情况，当数据增加时，可能超过原先定义的元素个数，当数据减少时，就造成内存浪费。链表动态地进行存储分配，可以适应数据动态增减的情况。

3、（静态）数组从栈中分配空间，对于程序员方便便捷，但是自由度小，链表从堆中分配空间，自由度大但是申请管理比较麻烦。

数组和链表在存储数据方面到底孰优孰劣呢？根据数组和链表的特性，分两类情况讨论。

一、当进行数据查询时，数组可以直接通过下标迅速访问数组中的元素。而链表则需要从第一个元素开始一直找到需要的元素位置，显然，数组的查询效率更高

二、当进行增减或删除元素时，在数组中增加一个元素，需要移动大量元素，在内存中空出一个元素的空间，然后将要增加的元素放在其中。同样，如果想删除一个元素，需要移动大量元素去填掉被移动的元素。而链表只需改动元素中的指针即可实现增加或删除元素

那么，为了既能够具备数组的快速查找的有点又能融合链表方便快捷的删除元素的优势，就有了HAsh表

所谓的hash，简单的说就是散列，即将输入的数据通过hash函数得到一个key值，输入的数据存储到数组中下标为key值的数组单元中去。

二叉树也既有链表的好处，也有数组的好处，在处理大批量的动态的数据是比较有用，文件系统和数据库系统一般都采用树（特别是B树）的数据结构数据，主要为提高排序和检索的效率

那么对于哈希表和二叉树的对比

先说哈希表，理论来说，哈希表插入和查找操作的时间复杂度都是O（1），这是他的优点，但是当有更多的饿数插入时，哈希表冲突的可能性就更大。

```bash
哈希表通常有两种解决方案：第一种是线性探索，相当于在冲突的槽后建立一个单链表，这种情况下，插入和查找以及删除操作消耗的时间会达到O(n)，且该哈希表需要更多的空间进行储存。第二种方法是开放寻址，他不需要更多的空间，但是在最坏的情况下（例如所有输入数据都被map到了一个index上）的时间复杂度也会达到O(n)。

所以，在决定建立哈希表之前，最好可以估计输入的数据的size。否则，resize哈希表的过程将会是一个非常消耗时间的过程。例如，如果现在你的哈希表的长度是100，但是现在有第101个数要插入。这时，不仅哈希表的长度可能要扩展到150，且扩展之后所有的数都需要重新rehash。

哈希表中的元素是没有被排序的。然而，有些情况下，我们希望储存的数据是有序的。
```



对于二叉树，

```bash
二叉树不会有冲突（collision），这意味着我们能够保证二叉树的插入和查找操作一直都是O(log(n))的时间复杂度。

二叉树的空间占用跟输入的输入数据一致。所以我们不需要为二叉树预先分配固定的空间。所以，你也不需要预先知道输入数据的size。
```