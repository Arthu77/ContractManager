from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, DateField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional

class ContractForm(FlaskForm):
    title = StringField('合同标题', validators=[DataRequired()])
    number = StringField('合同编号', validators=[DataRequired()])
    party_a = StringField('甲方', validators=[DataRequired()])
    party_b = StringField('乙方', validators=[DataRequired()])
    sign_date = DateField('签订日期', format='%Y-%m-%d', validators=[Optional()])
    effective_date = DateField('生效日期', format='%Y-%m-%d', validators=[Optional()])
    expiry_date = DateField('到期日期', format='%Y-%m-%d', validators=[Optional()])
    value = FloatField('合同金额', validators=[Optional()])
    status = SelectField('合同状态', choices=[
        ('draft', '草稿'),
        ('active', '生效中'),
        ('completed', '已完成'),
        ('terminated', '已终止')
    ])
    category_id = SelectField('合同分类', coerce=int)
    description = TextAreaField('合同描述')
    attachments = FileField('附件', validators=[
        FileAllowed(['pdf', 'doc', 'docx', 'jpg', 'png'], '只允许上传文档和图片!')
    ])
    submit = SubmitField('保存')

class CategoryForm(FlaskForm):
    name = StringField('分类名称', validators=[DataRequired()])
    description = TextAreaField('分类描述')
    submit = SubmitField('保存')

class ContractItemForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired()])
    specification = StringField('规格')
    unit = StringField('单位')
    quantity = FloatField('数量', validators=[DataRequired()])
    unit_price = FloatField('单价', validators=[DataRequired()])
    amount = FloatField('金额', validators=[Optional()])

class SearchForm(FlaskForm):
    keyword = StringField('关键词')
    category = SelectField('分类', coerce=int)
    status = SelectField('状态', choices=[
        ('', '全部'),
        ('draft', '草稿'),
        ('active', '生效中'),
        ('completed', '已完成'),
        ('terminated', '已终止')
    ])
    start_date = DateField('开始日期', format='%Y-%m-%d', validators=[Optional()])
    end_date = DateField('结束日期', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('搜索')

class ImportContractForm(FlaskForm):
    excel_file = FileField('Excel文件', validators=[
        FileRequired(),
        FileAllowed(['xlsx', 'xls'], '只允许上传Excel文件!')
    ])
    submit = SubmitField('导入')
