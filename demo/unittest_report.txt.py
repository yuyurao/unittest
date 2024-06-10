# 模块导入
from unittestreport.HTMLTestRunnerNew import HTMLTestRunner
# 报告存放路径
report_path = os.path.join(root_path,'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)
#  报告名称
ts = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
file_name = 'api_test_{}.html'.format(ts)
file_path = os.path.join(report_path,file_name)
with open(file_path,'w',encoding='utf8') as f:
    #  初始化运行器,以普通文本生成测试报告 TextTestRunner
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='xxx系统测试报告',
        description='接口自动化测试报告',
        tester='jsonLiu'
    #  6.运行测试用例 runner.run(suite)
    runner.run(total_suite)
    )
