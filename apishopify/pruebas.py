
class Pruebas:

    def recorrido2(self):
        a = []

        a.append({'id_product' : '123456', 'inventory_item_id' : 66655434})
        a.append({'id_product' : '68217678123', 'inventory_item_id' : 789147983274})
        for x in a:
            print(x['inventory_item_id'])