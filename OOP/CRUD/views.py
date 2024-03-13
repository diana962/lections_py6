# CRUD - C:create, R:read(listing,detail), U : upgrade , D: delete

class CreateMixin:
    def _get_or_set_objects(self):
        try:
            self.id
            self.objects
        except (NameError,AttributeError):
            self.objects = []
            self.id = 0
    def  __init__(self):
        self._get_or_set_objects()
    
    def post(self, **kwargs):
        self.id +=1
        obj = dict(id = self.id, **kwargs)
        self.objects.append(obj)
        return {'status': '201 created', 'msg': obj}

class ReadMixin:
    def list(self):
        res = [{'id': obj['id'], 'title': obj['title']} for obj in self.objects]
        return {'status': '200 Ok', 'msg': res}
    
    def detail(self, id, **kwargs):
        objects_id = [x['id'] for x in self.objects] 
        left = 0
        right = len(objects_id) - 1
        mid = len(objects_id) // 2
    
        # count = 0
        while objects_id[mid] != id and left <= right:
            if id < objects_id[mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
            # count += 1

        if left > right:
            return {'status': '404 Not found'}
        return {'status': '200 Ok', 'msg': self.objects[mid]}
    


    