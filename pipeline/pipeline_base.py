"""
    所有的 Pipeline 的基类
"""


class Pipeline:
    def pipeline_in(self, spider, item):
        """
        入库之前的操作，一般是清洗、转换

        :param spider:
        :param item: 单条 item
        :return: item
        """

        return item

    def pipeline_save(self, spider, item):
        """
        入库

        :param spider:
        :param item: 启用 item_buffer 将会是 List[item] 反之为 item
        :return: item
        """

        return item

    def pipeline_error(self, spider, item, exception: Exception):
        """
        出错时的操作
        如果没有返回，将会直接被送到 pipeline_failed

        :param spider:
        :param item: 启用 item buffer 时是 List[item]
        :param exception: 错误的详细信息
        :return: item
        """

        return item

    def pipeline_failed(self, spider, item) -> None:
        """
        超过最大重试次数时的操作

        :param spider:
        :param item: 启用 item buffer 时是 List[item]
        :return:
        """

    def pipeline_close(self, spider) -> None:
        """
        spider 结束时的操作

        :param spider:
        :return:
        """
