# 剑指 Offer

## 面试题2 单例模式

### Java 实现

- 饿汉式
	```java
	public class Singleton {
	  private static Singleton instance = new Singleton();
  private Singleton(){}
    public static Singleton getInstance() {
      return instance;
    }
  }
  ```
  
- 懒汉式

  - 双重加锁

  ```java
  public class Singleton {
    private volatile static Singleton instance;
    private Singleton(){}
    public static Singleton getInstance() {
      // 如果对象为空
      if (instance == null) {
        synchronized (Singleton.class) {
          // 如果获取到锁后对象仍然为空
          if (instance == null) {
            instance = new Singleton();
          }
        }
      }
      return instance;
    }
  }
  ```

  - 静态内部类

  ```java
  public class Singleton {
    // 加载一个类时，静态内部类不会被加载，直到调用该内部类
    public static class InstanceHolder {
      private static final Singleton INSTANCE = new Singleton();
    }
    private Singleton(){}
    public static Singleton getInstance() {
      return InstanceHolder.INSTANCE;
    }
  }
  ```

  - 枚举类

  ```java
  public enum Singleton {
    INSTANCE;
  }
  ```

### Python 实现

- 模块导入

  - 由于模块在第一次导入的时候会生成 .pyc 文件，第二次导入时会直接加载 .pyc

  ```python
  class Singleton(object):
    def foo():
      pass
    
  singlenton = Singleton()
  ```

- 装饰器

  ```python
  def singleton():
    _instance = {}
    def _singleton(*args, **kwargs):
      if cls not in _instance:
        _instance[cls] = cls(*args, **kwargs)
      return _instance[cls]
    return _singleton

  @singleton
  class Singleton(object):
    def __init__(self, name):
      self.name = name
  ```

- \__new__

  ```python
  class Singleton(object):
    _instance_lock = threading.Lock()
  
    def __new__(cls, *args, **kwargs):
      if not hasattr(Singleton, "_instance"):
        with Singleton._insatnce_lock:
          if not hasattr(Singleton, "_instance"):
            Singleton._instance = object.__new__(cls)
      return Singleton._instance
    
    def __init__(self):
      pass
  ```
  
- metaclass

  ```python
  class SingletonType(type):
    _instance_lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
      if not hasattr(cls, "_instance"):
        with SingletonType._insatnce_lock:
          if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
      return cls._instance
    
  class Singleton(metaclass=SingletonType):
    def __init__(self, name):
      self.name = name
  ```

## 面试题3 重复数字

- 

- 

- 将数字放到对应的 index 下，如 2 放到 array[2]，若交换前 array[i] == i，则 i 为重复数字

- 在长度为 n+1 的数组中，数字均为 1~n，找出数组中的重复数字，但不改变输入的数组

  将数字分为 1~m、m+1~n 两部分，若哪一部分的数字个数大于应有个数，则重复数字在哪一部分，知道无法分割，则为重复数字

  当然也可以新建一个数组然后采用上一题的方法

## 面试题4 二维数组中的查找

- 在一个每一行都递增且每一列都递增的二维数组中查找一个整数

  从右上角开始查起，先确定列号，在确定行号

## 面试题5 替换空格

- 将字符串中的空格替换成 %20

  这道题感觉和 c 语言的字符串特性有关系

  先统计字符串的空格总数，算出总长度，再从总长的末尾遍历和拷贝，关键点在于从后往前，这样可以利用原空间，不用开辟新空间

## 面试题6 倒序打印链表

- 倒序打印链表

  将链表节点放入栈中，然后进行弹栈

## 面试题7 重建二叉树

- 重建二叉树

  前序遍历的第一个数字为根节点，后序遍历找到根节点数字，其两边分别为左子树和右子树，根据这个规则进行递归生成

  ```python
  def helper(pre_order, in_order, pre_start, pre_end, in_start, in_end)
  ```

## 面试题8 二叉树的下一个节点

- 找到二叉树的下一个节点

  如果有右子节点，那么下一个节点应为右子节点的最左子节点

  如果没有右子节点，且为父节点的左子节点，那么下一个节点应为父节点

  如果没有右子节点，且为父节点的右子节点，需要向上寻找，找到一个节点为父节点的左子节点，那么下一个节点应为这个节点的父节点

## 面试题9 用两个栈实现队列

- 用两个栈实现队列

  一个栈为存入栈 S1，一个栈为辅助栈 S2

  存数据时，数据进入 S1

  取数据时，将 S1 中的数据弹栈并压栈进入 S2，返回 S2 的顶端数据

## 面试题10 斐波那契数列

- 输出第 n 个斐波那契数列的值
  - 递归解法： f(n) = f(n-1) + f(n-2)
  - 非递归解法：用两个变量记录前两个值

## 面试题11 旋转数组的最小数字

- 旋转数组的最小数字（旋转数组的定义是一个递增数组将前 m 个数放到后面）

  类似于二分查找

  找到中间元素，判断这个数字是否处于被旋转的后半部分，即判断中间数字是否*大于等于*（这里一定是大于等于）最左数字，如果是，那么最小数字肯定处于右半部分，不是，则处于左半部分。直到只剩下两个数字，那么后一个数字为最小数字

  特殊情况有

  ​	一个顺序数组，直接返回索引为 0 的数字

  ​	中间数字和两端数字都相同时，需要遍历数组寻找

## 面试题12 矩阵中的路径

- 矩阵中的路径

  递归，对上下左右进行递归，结束条件为超出数组范围、不等于要求的字符、已访问过，返回 false，递归到字符串末尾返回 true

## 面试题 13 机器人的运动范围

- 机器人的运动范围

  递归，和上题很相似，但需要注意的是回溯时不需要讲已经访问过的坐标变为未访问，因为被访问过他就已经算到可访问的格子中了

## 面试题14 剪绳子

- 剪绳子

  需要注意的是求得其实是长度为 n 的绳子剪任意刀的各段长最大乘积，看题目容易理解为需要输入剪多少段

  动态规划，f(n) = max(f(i) * f(n-i))

  贪婪算法，当 n >= 5 时，应该尽可能的多剪长度为 3 的绳子，特殊情况是当最后剩余 1 时，应当将最后 4 剪成 2 * 2

## 面试题15 二进制中 1 的个数

- 二进制中 1 的个数

  通过与 1 进行 & 运算，并进行右移，需要注意的是负数情况

  一个数与自己

  这道题感觉对于 python 不太适用，在 python 中 bin() 一个负数，输出的是负号加原码，要获取补码需要这个数与 0xffffffff 进行 & 操作

  ## 面试题16 数值的整数次方

- 实现 power 函数

  利用动态规划 f(n) = f(n/2) * f(n/2)，f(n) 代表一个数的 n 次方

  需要注意的是要考虑底数等于 0，指数等于 0，和底数等于负数的特殊情况

  判断奇偶可以用 n & 1 == 1

  除以 2 可以用位运算 n >> 1，乘 2 可以用位运算 n << 1

## 面试题17 打印从 1 到最大的 n 位数

- 打印从 1 到最大的 n 位数

  注意 n 是没有范围的，可能会出现溢出

  这道题对 python 也不太适用，python 不会存在溢出情况

  由于溢出，需要将数字转为字符串，等同于字符串加法

  由于是打印全部数字，也可以看成是一个 0-9 在 n 位上的全排列，可以用递归实现

## 面试题18 删除链表的节点

- 在 O(1) 时间内删除链表节点

  通过赋值被删除节点的下一个节点到被删除节点，达到删除的效果

  需要注意的是当被删除节点为最后一个节点时，需要遍历顺序删除

  被删除节点为头节点时直接删除

- 删除排序链表中的重复节点

  顺序遍历删除就好

  可以加一个 dummy 节点，预防很多 null 错误，然后用 former、latter 一前一后两个节点进行遍历

## 面试题 19 正则表达式

- 正则表达式匹配，'.' 代表任意字符，'*' 代表前面的字符出现任意次

  利用递归，主要处理的是带 * 的情况：

  ```python
  # 当前字符满足 * 前的字符，可能出现三种情况:
  # 1. * 结束了
  # 2. * 没结束，后面的字符还需要满足 *
  # 3. 这个字符也不属于 *
  # 当前字符不满足 * 的字符，那么一定是 * 结束了
  ```

## 面试题20 表示数值的字符串

- 判断字符串是否表示数值

  这道题个人感觉有些太繁杂了，面试不会出的

## 面试题21 分割奇偶

- 调整数组顺序使奇数位于偶数前面
  用两个指针指向收尾，满足要求则向中心移动，不满足要求就调换两个数的位置，直到两指针相遇

## 面试题22 链表中倒数第 k 个节点

- 链表中倒数第 k 个节点

  先将一个节点从头结点移动 k 位，在将头结点和这个节点一起移动，直到这个节点到链表末尾，此时头结点的位置就是倒数第 k 个

  需要注意的是代码的鲁棒性，即错误处理能力

## 面试题23 链表中环的入口节点

- 如果链表中有环，找到环的入口节点

  由于环的入口节点即为链表中倒数第环中节点的个数的节点，所以通过计算环中节点的个数和上一题的方法就能找到入口节点

  环中节点个数的计算可以通过，用一快一慢两指针从头结点出发，当两指针相遇时，他们一定指向环内的一个节点，这时候继续让一个指针走，并计数，两指针再次相遇时，计数器个数则为环中节点个数

## 面试题24 反转链表

- 反转链表

  通过三个指针进行，遍历中调换顺序

## 面试题25 合并两个排序的链表

- 合并两个排序的链表

  新建一个dummy节点，作为新链表的头结点，用两个节点分别指向两个头结点，然后进行遍历比较大小，注意最后需要处理一条链表已经处理完但另一条链表还未结束的情况

## 面试题26 树的子结构

- 判断树 A 是否为 树 B 的子树

  利用中序遍历递归，对每一个节点当做根节点并判断是否为子树

## 面试题27 二叉树的镜像

- 将二叉树转为它的镜像

  通过前序遍历，每当遍历到一个有子节点的节点，将子节点互换位置

## 面试题28  对称的二叉树

- 判断一棵二叉树是否是对称的

  通过前序遍历，定义一个新的前序遍历为 中、右、左，如果为对称二叉树，那么这两种前序遍历的结果应为相同

## 面试题29 顺时针打印矩阵

- 顺时针打印矩阵

  把每一个圈当成单独的进行递归，难点在于每一行和列的起始位置的计算

  ```python
  """
  rows: 当前圈总行数
  cols: 当前圈总列数
  row: 起始行
  col: 起始列
  """
  def print_matrix(matrix, rows, cols, row, col):
    	# 当总行数或者总列数小于等于 0 时，说明打印结束了
      if rows <= 0 or cols <= 0:
          return
      for i in range(col, col + cols):
          print matrix[row][i]
      if rows > 1:
          for i in range(row + 1, row + rows):
              print matrix[i][row + rows - 1]
          if cols > 1:
              for i in range(col + cols - 2, col - 1, -1):
                  print matrix[row + rows - 1][i]
              if rows > 2:
                  for i in range(row + rows - 2, row, -1):
                      print matrix[i][row]
      print_matrix(matrix, rows - 2, cols - 2, row + 1, col + 1)
  ```

## 面试题30 包含 min 函数的栈

- 实现一个能在 O(1) 时间内找到栈的最小元素的栈

  用两个栈来实现，一个栈为数据栈，另一个栈存放数据栈元素每一层对应的最小值，每当存入一个数据时，判断当前值是否小于最小值栈的栈顶元素，若小于则将该元素存入最小值栈，若大于则将最小值栈栈顶元素在存入一次

## 面试题31 栈的压入弹出序列

- 判断弹出序列是否满足压入序列

  用一个模拟栈进行操作，对于弹出序列中的数字依次遍历，若数字在栈顶，直接弹出，若不在，对压入序列中的数字进行遍历，直到找到数字或序列结束，若此时栈顶元素不是弹出序列中的元素，则不满足

## 面试题32 从上到下打印二叉树

- 不分行从上到下打印二叉树

  用一个队列保存节点，并按序输出

- 分行从上到下打印二叉树

  用两个变量分别记录当前行的节点数和下一行的节点数，每次只输出当前行节点数个节点

- 之字形打印二叉树

  用一个队列和一个栈分别记录，达到之字形效果

## 面试题 33 二叉搜索树的后序遍历序列

- 判断输入序列是否是一个二叉搜索树的后序遍历序列

  后序遍历序列的最后一个值为根节点，从头遍历直到遇到比根节点大的值，这些节点均为左子树，后面的节点都为右子树，判断后面的节点是否存在比根节点小的，存在则不是后序遍历序列

## 面试题34 二叉树中和为某一值的路径

- 打印出二叉树中节点值的和为某一值的所有路径，路径指的是从根节点到叶节点

  中序遍历递归，并储存经过节点，到达叶节点时判断是否等于要求值，等于则输出，回溯时弹出之前的节点

## 面试题35 复杂链表的复制

- 复制复杂链表，复杂链表指的是链表既指向下一个节点，也指向一个兄弟节点

  将链表的每个节点复制一份并插在原来两个节点之间

  然后顺序遍历复制sibling

  然后拆开两条链表

## 面试题36 二叉搜索树与双向链表

- 将二叉搜索树转换成一个排序的双向链表

  通过中序遍历达到有序的目的，通过一个全局变量记录上一个节点，在遍历到最左节点时赋初值，之后遍历到任一节点，他的左节点是上一个节点，同时把上一节点的右节点赋成当前节点

## 面试题37 序列化二叉树

- 实现两个函数，分别用来序列化和反序列化二叉树

  通过前序遍历，并记录 null 节点，实现序列化

  遍历序列化，按前序遍历的顺序创建节点

## 面试题38 字符串的排列

- 打印出字符串的所有排列

  递归排列就好

  个人用的是将字符串转为一个数组，每遍历一层就去掉一个字符，回溯时在加回去，当然也可以不用数组而是将字符改为特定标识

  解析给的是将当前位与后面每一位进行交换，回溯时在放回原位

## 面试题39 数组中出现次数超过一半的数字

- 数组中有一个数字超过数组长度的一半，找出这个数字

  可以用快排中获取一个元素正确下标的方法，这个数字的个数由于超过数组长度的一半，所以这个数组的中位数肯定是这个数字，所以只需要找到下标位置为中位的数字

  也可以利用数组特性，对数组顺序遍历，如果当前数等于前一个数，那么计数器加一，不等则减一，每当计数器等于 0 时，记下当前数，由于出现次数超过数组长度的一般，所以最后记下的数肯定是要求的数

## 面试题40 最小的 k 个数

- 输出最小的 k 个数

  同上题，找到下标恰好为k的数字，并输出前面的所有数

  利用一个最大堆，每次比较堆顶数据和遍历到的数据，若堆顶数据大于当前数据，则交换

  在 Java 中，最大堆的实现可以通过 PriorityQueue

  ```java
  PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(((o1, o2) -> (o2 - o1)));
  ```

  在 Python 中，最大堆实现可以通过引入 heapq（最小堆），并对数据取反插入

## 面试题41 数据流中的中位数

- 找到数据流的中位数

  主要是考虑用什么数据结构，考虑他们的效率

  最好的是用最大堆和最小堆结合，需要注意的是如何保证两个堆中元素相差最多为 1，以及最大堆中的所有元素都需要小于最小堆

  通过轮回插入，奇数插最大，偶数插最小

  插入数据时，先和另一个堆中的堆顶数据比较，在进行数据交换

## 面试题42 连续子数组的最大和

- 连续子数组的最大和

  利用动态规划，f(i) 代表前i项的子数组最大和，f(i+1) = f(i)+ array[i+1] 如果 f(i)>0，否则 = arrayp[i+1]

  也可以利用规律，但代码其实和上面一样

## 面试题43 1~n 整数中 1 出现的次数

- 1~n 整数中 1 出现的次数

  这道题纯粹找规律，有时间了再看吧

## 面试题44 数字序列中某一位的数字

- 数字序列中某一位的数字

  这道题和上一题差不多，都在于找规律


## 面试题45 把数组排成最小的数

- 输入一个正整数数组，把里面的所有数重新排列，数组中所有数连起来形成的数最小

  由于位数固定，要数字最小则高位最小，所以只需要将小的数字放在前面，但需要注意的是，这里比较大小的方法有所不同，因为虽然 4 比 32 小，但 432 会比 324 大，所以还需要考虑位的因素

  比较大小的方法应该改为，将两个数扩展成同样长度，若一个数不够长则将他的最后一位拷贝，直到两树一样长，然后进行比较

## 面试题46 把数字翻译成字符串

- 数字 0~25 代表 a~z，将一串数字翻译成字符串，计算有多少种翻译方法

  倒序动态规划

  f(n) = f(n+1) if n 和 n+1 位的数字连起来不能组成字符

  f(n) = f(n+1) + f(n+2) if n 和 n+1 位的数字连起来可以组成字符

## 面试题 47 礼物的最大价值

- m x n 的棋盘内放着礼物，从左上角开始，每次向下或向右移动移动到右下角，计算能获得的最大礼物价值

  动态规划，节约空间的解法是用一行数组来进行规划，比较的时候前一个值代表左边的值，当前值代表上面的值

## 面试题48 最长不含重复字符的子字符串

- 输出最长不含重复字符的字符串的长度

  动态规划

  如果当前字符没有出现过，或者 *出现的位置距离现在位置超过了当前正在统计的字符串长度*， 也就是说现在在统计的子字符串并不包括之前出现的这个字符，长度加一

  如果不满足上述条件，计算最大长度，并重新计算当前统计字符串长度，即从之前出现的字符串的下一个字符开始计算

## 面试题49 丑数

- 这道题也是数学题，以后再看

## 面试题50 第一个只出现一次的字符

- 输出字符串中第一个只出现一次的字符的值

  统计字符出现次数，可以用一个哈希表来存，对于英文字符的话可以用一个长为256的数组储存

## 面试题51 数组中的逆序对

- 如果前面的数字大于后面的数字，这两个数字组成一个逆序对

  用归并排序的方法，每次比较两部分的值，由于归并排序的两部分都是排好序的，所以可以一次计算出当前数字的所有逆序对

## 面试题52 两个链表的第一个公共节点

- 找到两个链表的第一个公共节点

  有公共节点的两个链表，只要找到一条链表比另一条链表长多少，并使两个链表从同一时刻开始遍历，那么第一个相同节点就是第一个公共节点

## 面试题53 在排序数组中查找数字

- 计算数字在排序数组中出现的次数

  通过二分查找找到该数字第一次出现的位置和最后一次出现的位置

  重点在于处理中间数字等于被查找数字的情况，这时候需要判断是否找到指定下标，找到的标志是相邻的数字不等于指定数字

- 长度为 n-1 的数组中，数字唯一且大小在 0~n-1，找出缺失的数字

  由于题目要求，数字下标应该与数字相等，所以用二分查找法，若下标与数字不等，则说明缺失数字在当前数字之前，相等则在之后，找到的标志是当前数字、下标不等，但前一个数字相等

- 在递增数组中，有一个数字与下标相等，找到这个数字

  简单的二分查找

## 面试题54 二叉搜索树的第 k 大节点

- 找出二叉搜索树的第 k 大节点

  中序遍历

## 面试题55 二叉树深度

- 从根节点到叶节点的最长路径长度为深度

  前序遍历

- 判断是否为平衡二叉树

  后序遍历

## 面试题56 数组中数字出现的次数

- 数组中除了两个数字只出现一次，另外所有数字都出现两次，找到出现一次的两个数字

  两个相同数字异或的结果为0，所以将数组中的所有数字进行异或，找到结果中的第一个 1，这个 1 就是分类数组中两种数字的标准，可以确保两个出现一次的数字分在不同组，然后分组异或，结果就是两个数字

- 数组中除了一个数字出现一次，其他数字都出现了三次，找到出现一次的数字

  由于所有数字都出现了三次，那么所有数字的每一位相加一定是三的倍数，所以用所有数字按位相加，每位模 3，每位的余数组成的数就是出现一次的数

## 面试题57 和为 s 的数字

- 递增排序的数组中求两个数的和为s

  用两个指针指向数组的开始和末尾，若当前和小于s则移动开始指针，大于则移动末尾指针

- 打印所有和为 s 的连续正数序列

  同上题一样，用两个指针作为滑动窗口，若当前窗口和小于 s，扩大窗口，大于则缩小窗口

## 面试题58 翻转字符串

- 翻转句子中单词的顺序（单词内部不翻转）

  先对句子中的每个单词都进行翻转，然后再逐一翻转每个单词

- 左旋转字符串（将前 n 个字符放到最后去）

  先翻转前 n 个字符，再翻转后面的所有字符，然后翻转整个字符串

## 面试题 59 队列的最大值

- 获取一个数组中每个长为 n 的滑动窗口中的最大值

  用一个队列记录可能的最大值*下标*，队首的下标对应的值就是当前滑动窗口的最大值。所以当当前下标与队首下标差距超过滑动窗口大小时，要出队，且在确定最大值之前，需要把队列中所有比当前值小的下标去除，因为他们不可能是当前也不可能是后面的窗口的最大值了。

- 用 O(1) 时间获取最大值的队列

  同之前的栈

## 面试题60 n 个骰子的点数

- 输出投 n 个骰子，能出现的所有点数的概率

  动态规划，投出 n 个骰子出现的点数为 n~6*n，以 n 为例，抛出 n 的概率为，当抛 n-1 个骰子时，抛出 n-6 ~ n-1 的概率的和，因为多一个骰子可能抛出 1~6

## 面试题61 扑克牌中的顺子

- 判断输入的数组是否是顺子，0 代表任意值

  排序，数 0 的个数，数剩下的数的间隔个数，需要注意的是如果存在相等的数，算间隔的话会是 -1，影响结果，由于两数相等，肯定存在对子，所以可以直接返回 false

## 面试题62 圆圈中最后剩下的数字

- 约瑟夫环，每次从 1 开始计数，删除第 m 个数字

  数组或链表直接模拟

  数学解法，可以背下来

  ```
  private static int getLastNumberWithMath(int n, int m) {
      if (n < 1 || m < 1)
          return -1;
      int last = 0;
      for (int i = 2; i <= n; i++)
          last = (last + m) % i;
      return last;
  }
  ```

## 面试题63 股票的最大利润

- 给定一个数组代表股票在某些时间节点的价格，计算最大利润

  遍历到 i 时，只要知道前 i-1 个数的最小值，就能算出当前的最大利润

## 面试题64 1 + 2 + ... + n

- 不用乘除法和循环、条件语句计算 1 + 2 + ... + n

  直接用公式和 pow 函数

  用判断语句

  ```
  private static int accumulate(int n) {
      int sum = n;
      boolean b = n > 0 && (sum += accumulate(n - 1)) > 0;
      return sum;
  }
  ```

## 面试题65 不用加减乘除做加法

- 不用加减乘除做加法

  转成位运算，位运算的加法可以当成是两步，先做异或运算，计算出不含进位的结果，再将两数相与并向左移位进行进位，再将这两个运算结果当成两个新的数继续运算，直到进位等于0

- 交换两个数字的值

- ```
  private static void swap(int num1, int num2) {
      num1 = num1 ^ num2;
      num2 = num1 ^ num2;
      num1 = num1 ^ num2;
      System.out.println("num1: " + num1 + " num2: " + num2);
  }
  ```

## 面试题66 构建乘积数组

- 给定一个数组 A[0,1,...,n-1]，请构建一个数组 B[0,1,...,n-1]，B[i] = A[0] * A[1] * ... * A[i-1] * A[i+1] * ... * A[n-1]

  定义 C[i] = A[0] * ... * A[i-1]，D[i] = A[i+1] * ... * A[n-1]

  上述两个数组都可以通过递归计算出来

