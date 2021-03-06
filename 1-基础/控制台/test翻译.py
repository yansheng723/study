import unittest
from 解释器 import 中文报错控制台

class test功能(unittest.TestCase):

    控制台 = 中文报错控制台()
    
    def test_报错信息(self):
        self.assertEqual(self.控制台.中文化("Traceback (most recent call last):"), "回溯 (最近的调用在最后):")
        self.assertEqual(self.控制台.中文化("NameError: name '学' is not defined"), "命名错误: 命名'学'未定义")
        self.assertEqual(self.控制台.中文化("SyntaxError: invalid syntax"), "语法错误: 不正确的语法")
        self.assertEqual(self.控制台.中文化("ZeroDivisionError: division by zero"), "除零错误: 不能被0除")
        self.assertEqual(self.控制台.中文化("NameError: free variable 'type' referenced before assignment in enclosing scope"), "命名错误: 在闭合作用域中, 自由变量'type'在引用之前未被赋值")
        self.assertEqual(self.控制台.中文化("UnboundLocalError: local variable '学生' referenced before assignment"), "本地变量未定义错误: 本地变量'学生'在引用之前未被赋值")
        self.assertEqual(self.控制台.中文化("TypeError: must be str, not int"), "类型错误: 不能将整数自动转换为字符串")
        self.assertEqual(self.控制台.中文化("TypeError: unsupported operand type(s) for /: 'str' and 'str'"), "类型错误: 不支持/的操作数: 'str'和'str'")
        self.assertEqual(self.控制台.中文化("TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'"), "类型错误: 不支持**或pow()的操作数: 'str'和'int'")
        self.assertEqual(self.控制台.中文化("TypeError: can't multiply sequence by non-int of type 'str'"), "类型错误: 不能用非整数的类型--'str'对序列进行累乘")
        self.assertEqual(self.控制台.中文化('TypeError: can only concatenate list (not "str") to list'), '类型错误: 只能将list(而非"str")联结到list')
        self.assertEqual(self.控制台.中文化("AttributeError: 'list' object has no attribute 'length'"), "属性错误: 'list'个体没有'length'属性")

    def test_转换(self):
        self.assertEqual(self.控制台.转换("如果 True"), "if True")
        self.assertEqual(self.控制台.转换("打印('吃了么')"), "print('吃了么')")
        self.assertEqual(self.控制台.转换("打印('打印')"), "print('打印')")
        self.assertEqual(self.控制台.转换("学"), "学")

if __name__ == '__main__':
    unittest.main()