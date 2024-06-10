import os
import time
import unittest
# 1. 初始化testloader(加载器）
loader = unittest.TestLoader()
# 2.1 加载方式1： 加载全部测试用例
# 2.1 suite = testloader.discover(文件夹路径,'test_*.py) 发现(加载)用例
# 2.2 加载方式2：加载多个模块测试用例
# 加载多个模块的测试用例,保存到测试套件当中
suite1 = loader.loadTestsFromModule(模块名)
suite2= loader.loadTestsFromTestCase(类名) 
suite3 = loader.loadTestsFromName(name,模块名) # name：传入一个模块或测试用例类或测试方法，或一个可调用的对象 
suite_list = [suite1,suite2,suite3]
# 将多个测试套件合并添加第一个总的测试套件中,初始化一个空的测试套件
total_suite = unittest.TestSuite()
total_suite.addTests(suite_list)
# suite.addTests([类名1('函数名1'),类名1('函数名2'),类名1('函数名3'),类名2,模块名1,模块名2,....])
# 加载方式3：加载指定测试类
# suite = loader.loadTestsFromTestCase(测试用例类名)
# 3. 初始化运行器
runner = unittest.TextTestRunner()
# 4. 运行测试用例 runner.run(suite)
runner.run(total_suite)
