# 合同管理系统

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-green)](https://flask.palletsprojects.com/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15.4-red)](https://pypi.org/project/PyQt5/)

基于Flask和PyQt5的合同管理系统，提供本地化合同管理解决方案，支持分类管理、Excel导入导出等功能。

## 功能特性

- **合同管理**
  - 创建/编辑/删除合同
  - 合同状态跟踪（进行中/已完成/逾期）
  - 支持PDF/Word附件上传
  - 到期提醒功能

- **分类管理**
  - 多级分类体系
  - 分类颜色标记
  - 分类快速筛选

- **数据交互**
  - Excel模板导入/导出
  - 合同数据批量操作
  - 数据备份与恢复

- **用户界面**
  - 混合桌面应用体验
  - 响应式网页布局
  - 本地化数据存储

## 技术架构

```
├── app/              # Flask应用核心
│   ├── models.py     # 数据模型
│   ├── routes.py     # 路由控制
│   ├── forms.py      # 表单处理
│   └── templates/    # 网页模板
├── instance/         # 数据存储
│   ├── contracts.db  # SQLite数据库
│   └── uploads/      # 文件上传目录
├── config.py         # 配置参数
├── run.py            # 服务启动入口
└── contract_manager_gui.py  # 桌面GUI入口
```

## 安装运行

1. 克隆仓库
```bash
git clone https://github.com/your-repo/contract-manager.git
cd contract-manager
```

2. 安装依赖
```bash
pip install Flask==2.0.1 Flask-SQLAlchemy==2.5.1 Flask-Migrate==3.1.0 PyQt5==5.15.4 PyQtWebEngine==5.15.5 openpyxl==3.0.9 python-dotenv==0.19.0
```

3. 初始化数据库
```bash
flask db upgrade
```

4. 启动系统
```bash
# 桌面模式
python contract_manager_gui.py

# 或纯Web模式
flask run
```

## 许可协议
MIT License
