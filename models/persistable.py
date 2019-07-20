class Persistable:
    """ Small base model for all queries """
    def __init__(self, Model):
        self.Model = Model

    def create(self, **kwargs):
        return self.Model(**kwargs).save()

    def fetch(self, page=1, per_page=10, **kwargs):
        documents = self.Model.objects(**kwargs).paginate(page, per_page)
        return { "data": documents.items, "has_next": documents.has_next,  "has_prev": documents.has_prev }
        