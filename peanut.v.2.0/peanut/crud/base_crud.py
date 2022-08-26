from abc import ABCMeta, abstractmethod
from typing import Generic, Type, TypeVar

from sqlalchemy import or_

from peanut.core.error import ClientError
from peanut.core.ext import db

ModelType = TypeVar("ModelType")


class BaseCrud(Generic[ModelType]):
    __metaclass__ = ABCMeta

    def __init__(self, model: Type[ModelType]):
        self.session = db.session
        self.model = model
        self.query = self.model.query

    @classmethod
    @abstractmethod
    def get_instance(cls):
        """ 类方法，用来创建对象"""
        pass

    def get(self, entity_id):
        """ 根据ID查询实体数据"""

        return self.query.filter(self.model.id == entity_id).first()

    def all(self):
        """ 查询全部数据"""
        return self.query.filter(self.model.is_active.isnot(False)).all()

    def get_all_name(self, keyword):
        """ 根据码表的name字段查询数据，注意：仅适用于码表"""
        return self.query.filter(self.model.name.like(keyword)).all()

    def delete(self, entity):
        """ 直接删除数据实体"""
        self.session.delete(entity)

    def delete_by_id(self, todo_id):
        """
        通过ID删除对应数据
        """
        self.query.filter_by(id=todo_id).delete()

    def update(self, todo_id, entity):
        self.query.filter_by(id=todo_id).update(entity)

    def save(self, entity):
        self.session.add(entity)

    def paging(self, page, per_page, keyword=None, cols=None):

        """ 分页查询数据
        :page: 页码
        :per_page: 每页大小
        :cols: 模糊查询的列
        :keyword: 关键字
        """
        query = self.model.query
        if not keyword:
            return query.paginate(page=page, per_page=per_page)

        if not cols:
            raise AttributeError("cols参数不能为空")

        conditions = []
        key = '%{}%'.format(keyword)
        for col in cols:
            attr_col = getattr(self.model, col, None)
            if not attr_col:
                raise AttributeError(col + "不存在")
            conditions.append(attr_col.like(key))

        query = query.filter(or_(*conditions))
        return query.paginate(page=page, per_page=per_page)

    def __get_by_callable(self, item, *args, **kwargs):
        """ get_by_ 通用方法
        所有以get_by_名称开头的方法，都将自动按by_条件查询。
        例子:get_by_username，将会以username为条件查询；get_by_email，将会以email为条件查询
        """
        if len(args) != 1:
            raise AttributeError(item + "方法必须有一个参数")
        condition_name = item.replace("get_by_", "")
        condition = dict()
        condition[condition_name] = args[0]
        return self.query.filter_by(**condition).first()

    def __has_exist_callable(self, item, *args, **kwargs):
        """ xxx_exist 通用方法
        所有xxx_exist形式的方法，都会以xxx为条件，判断是否存在相关值
        :@param1 必选参数，判断该条数据是否存在
        :@param2 可选参数，排除要比较的ID
        :return entity if exist, otherwise None
        """
        if len(args) < 1:
            raise AttributeError(item + "方法至少有一个参数")
        condition_name = item.replace("_exist", "")
        condition = dict()
        condition[condition_name] = args[0]
        query = self.query.filter_by(**condition)
        entity = query.first()
        if entity and len(args) == 2:
            if entity.id == args[1]:
                return None
        return entity

    def __getattr__(self, item):
        if item in dir(self):
            return getattr(self, item)
        if item.startswith("get_by_") or item.endswith("_exist"):
            def _func(*args, **kwargs):
                if item.startswith("get_by_"):
                    return self.__get_by_callable(item, *args, *kwargs)
                if item.endswith("_exist"):
                    return self.__has_exist_callable(item, *args, *kwargs)

            return _func

        raise AttributeError(item)

    def __base_data_validator(self, field, value, exclude_id=None):
        """ 验证某个字段的数据是否存在
        :model 要验证的模型
        :field 要验证的字段
        :value 要验证的值
        :exclude_id 要排除的id
        """

        field_validator = getattr(self, field + '_exist')
        if exclude_id:
            obj_in_db = field_validator(value, exclude_id)
        else:
            obj_in_db = field_validator(value)

        return obj_in_db

    def exist_validator(self, entity, fields, exclude_id=None):
        """ 批量验证数据是否存在，如果存在抛出异常"""
        for field in fields:
            if isinstance(entity, dict):
                field_value = entity.get(field)
            else:
                field_value = getattr(entity, field)

            validate_result = self.__base_data_validator(field, field_value, exclude_id)

            # 如果存在，则引发异常
            if validate_result:
                columns = self.model.__mapper__.columns  # 获取model中的注释字段
                field_name = columns.get(field).comment
                if not field_name:
                    field_name = field
                raise ClientError("%s 已存在" % field_name)
