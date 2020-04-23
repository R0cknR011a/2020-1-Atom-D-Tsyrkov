import logging


class ProductArray:
    def __init__(self, array):
        logging.basicConfig(filename='product_array.log', level=logging.DEBUG)
        logging.info('Type assertion engaged...')
        if not isinstance(array, list):
            logging.warning('FAILED')
            raise TypeError('Input array should be type of [list]')
        logging.info('OK')
        logging.info('Empty input list assertion engaged...')
        if len(array) == 0:
            logging.warning('FAILED')
            raise ValueError('Input array should be NOT empty')
        logging.info('OK')
        logging.info('Element type assertion engaged...')
        for x in array:
            if not isinstance(x, int):
                logging.warning('FAILED')
                raise TypeError('Every element in input array should be type of [int]')
        logging.info('OK')
        self.array = array
        self.length = len(array)
        self.log_step = self.length // 100 if self.length > 100 else 1

    def get_array(self):
        if self.length == 1:
            return 0
        tmp = 1
        result = []
        logging.info('Unitary array initialization engaged...')
        for i in range(self.length):
            result.append(1)
        logging.info('DONE')
        logging.info('Right side of multiplication calculation engaged...')
        for i in range(self.length):
            result[i] = tmp
            tmp *= self.array[i]
            if i % self.log_step == 0:
                logging.info('CURRENT STATE: INDEX = {}, VALUE = {}'.format(i, result[i]))
        tmp = 1
        logging.info('Left side of multiplication calculation engaged...')
        for i in range(self.length - 1, -1, -1):
            result[i] *= tmp
            tmp *= self.array[i]
            if i % self.log_step == 0:
                logging.info('CURRENT STATE: INDEX = {}, VALUE = {}'.format(i, result[i]))
        return result
