import collections

class TreeStore:

    def __init__(self, obj_list):
        self._obj_list = obj_list
        self.parents_dict = collections.defaultdict(list)
        self.items_id = dict()

    def _create_indexes_parents_dict(self):
        for item_dict in self._obj_list:
            self.parents_dict[item_dict['parent']].append(item_dict)
            self.items_id[item_dict['id']] = item_dict

    def get_all(self):
        """ Получение изначального массива элементов """

        return self._obj_list

    def get_item(self, id: int) -> dict:
        """ Получение элемента по id """
        try:
            print(self.items_id[id])
            return self.items_id[id]
        except KeyError:
            return None

    def get_children(self, id: int):
        """ Получение дочерних элементов элемента по id """

        children_item_ids = self.parents_dict.get(id)
        if not children_item_ids:
            return []

        return children_item_ids


    def get_all_parents(self, id: int):
        """ Получение массива из цепочки родительских элементов """

        item: dict = self.get_item(id)

        if not item:
            return []

        parent_items = list()
        while item["parent"] != "root":
            item: dict = self.get_item(item["parent"])
            parent_items.append(item)


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

Ts = TreeStore(items)
Ts._create_indexes_parents_dict()
Ts.get_all()
Ts.get_item(8)
Ts.get_children(8)
Ts.get_all_parents(8)
