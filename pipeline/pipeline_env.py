"""
    该 pipeline 是用来区分生产还是开发环境的

    禁止重写 pipeline_save
"""
from typing import final
from abc import abstractmethod

from pipeline.pipeline_base import Pipeline


class PipelineEnv(Pipeline):

    @abstractmethod
    def is_produce(self) -> bool:
        """
        判断是否是生产环境

        :return:
        """

        return False

    @final
    def pipeline_save(self, spider, item):
        """
        区分生产环境和开发环境走不同的逻辑（禁止重写该方法）

        :param spider:
        :param item: 启用 item_buffer 将会是 List[item] 反之为 item
        :return: item
        """
        if self.is_produce():
            return self.pipeline_produce_save(spider=spider, item=item)
        else:
            return self.pipeline_develop_save(spider=spider, item=item)

    @abstractmethod
    def pipeline_produce_save(self, spider, item):
        """
        生产环境的保存

        :param spider:
        :param item: 启用 item_buffer 将会是 List[item] 反之为 item
        :return: item
        """

        return item

    @abstractmethod
    def pipeline_develop_save(self, spider, item):
        """
        开发环境的保存

        :param spider:
        :param item: 启用 item_buffer 将会是 List[item] 反之为 item
        :return: item
        """

        return item
