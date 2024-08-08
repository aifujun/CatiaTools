from pathlib import Path
import time


BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent
LOG_DIR = ROOT_DIR / 'logs'
DATABASE_DIR = ROOT_DIR / 'db'


################################
# 日志配置
################################
LOG_ALL_FILE = LOG_DIR / f'all.log'
LOG_DEBUG_FILE = LOG_DIR / f'debug.log'
LOG_ERROR_FILE = LOG_DIR / f'error.log'
LOG_FORMAT = ('[%(asctime)s][%(levelname)s]'
              '[%(filename)s:%(lineno)d][%(module)s:%(funcName)s] %(message)s')


################################
# 数据库配置
################################
LOCAL_DB_FILE = DATABASE_DIR / 'local.db'


################################
# 测试信息
################################
TEST_DB = r'E:\env\database\XinDu3X\test.sqlite'


if __name__ == '__main__':
    print(BASE_DIR)
    print(ROOT_DIR)
